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
            self.tail = Block(timestamp, data, 0)
            return

        # Move to the tail (the last node)
        # get tail hash and create new block node with it 
        previous_hash = self.tail.hash
        node = Block(timestamp, data, previous_hash)
        node.previous_block = self.tail
        # reset new block node to tail
        self.tail = node
        return
    
    def to_list(self):
        out_list = []

        node = self.tail
        while node:
            out_list.append(node.previous_hash)
            node = node.previous_block

        return out_list
    


timestamp = "13:12 4/2/2019"
data = "Some Information"
data2 = "We are going to encode this string of data!"

block_linked_list = BlockLinkedList()
block_linked_list.append(timestamp, data)
block_linked_list.append(timestamp, data2)
block_linked_list.append(timestamp, data)
block_linked_list.append(timestamp, data2)

print(block_linked_list.to_list())
