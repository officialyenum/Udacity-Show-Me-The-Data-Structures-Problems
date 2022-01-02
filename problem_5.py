import hashlib


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.previous_block = None
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
            sha = hashlib.sha256()

            hash_str = data.encode('utf-8')

            sha.update(hash_str)

            return sha.hexdigest()

class BlockLinkedList:
    def __init__(self):
        self.tail = None

    def append(self, timestamp, data):
        if self.tail is None:
            self.tail = Block(timestamp, data, '')
            return

        # Move to the tail (the last node)
        # get tail hash and create new block node with it 
        previous_hash = self.tail.hash
        node = Block(timestamp, data, previous_hash)
        node.previous_block = self.tail
        # reset new block node to tail
        self.tail = node
        return
    
    def to_list_hash(self):
        out_list = []

        node = self.tail
        while node:
            out_list.append(node.previous_hash)
            node = node.previous_block

        return out_list

    def to_list_timestamp(self):
        out_list = []

        node = self.tail
        while node:
            out_list.append(node.timestamp)
            node = node.previous_block

        return out_list
    


timestamp = "13:12 4/2/2019"
timestamp2 = "14:12 4/2/2021"
data = ""
data2 = "We are going to encode this string of data!"

# Test Case 1
block_linked_list = BlockLinkedList()
print(block_linked_list.to_list_hash())  # should print empty list because there is no block in BlockLinkedList chain


# Test Case 2
block_linked_list2 = BlockLinkedList()
block_linked_list2.append(timestamp, data) 
block_linked_list2.append(timestamp2, data)
print(block_linked_list2.to_list_hash()) # should print list of block hash
print(block_linked_list2.to_list_timestamp()) # should print list of block with different timestamp

# Test Case 3
block_linked_list3 = BlockLinkedList()# should print list with empty string as hash
block_linked_list3.append(timestamp, data2)
block_linked_list3.append(timestamp, data)
block_linked_list3.append(timestamp, data2)

print(block_linked_list3.to_list_hash()) # should print list of block hash
print(block_linked_list3.to_list_timestamp()) # should print list of blockwith same timestamp
