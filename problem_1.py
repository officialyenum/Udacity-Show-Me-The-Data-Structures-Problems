"""
DataMap Class 
This object class holds a key and value
"""
class DataMap():
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
"""
DoubleNode Class 
This object class holds a dataMap object points to the next and previous dataMap Object
"""
class DoubleNode:
    def __init__(self, dataMap):
        self.dataMap = dataMap
        self.next = None
        self.previous = None

"""
DoublyLinkedList Class 
This object class holds a DoubleNode Object points to the next and previous DoubleNode Object
"""
class DoublyLinkedList:
    def __init__(self):
        self.node = DoubleNode(None)
        self.len = 0

        self.node.next  = self.node
        self.node.previous = self.node

    def move_to_front(self, node):
        if node is None:
            return None
        elif node.previous is not None and node.next is not None:
            # previous and next node is not none
            node.next.previous = node.previous # move previous node into previous of the next node
            node.previous.next= node.next # move next node into next of the previous node
            node.next = None # set next node to none
            node.previous = None # set previous node to none
            # print('node next prev : {}'.format(node.next.previous))
            # print('node prev next: {}'.format(node.previous.next))
            # print(' is not None node next: {}'.format(node.next))
            # print(' is not None node prev : {}'.format(node.previous))
            return node
        else:
            # previous or next node is none
            node.previous = self.node # move object node to current previous node
            node.next = self.node.next # move object next node to current next node
            node.next.previous = node # move current node to next node then previous of that next node
            node.previous.next = node # move current node to previous node then next of that previous node
            # print('node prev : {}'.format(node.previous.dataMap))
            # print('node next: {}'.format(node.next.dataMap))
            # print('node next prev : {}'.format(node.next.previous.dataMap.value))
            # print('node prev next: {}'.format(node.previous.next.dataMap.value))
            return node

    def remove_bottom(self):
        return self.remove(self.node.previous)

    def remove(self, node):
        if self.len == 0:
            return None
        self.len -= 1
        node.next.previous = node.previous
        node.previous.next= node.next
        node.next = None
        node.previous = None
        return node

"""
LRU_Cache Class 
This object class holds a DoubleLinkedList, dictionary filled with DoubleNodesObject and capacity for cache length
"""
class LRU_Cache():

    def __init__(self, capacity=5):
        # Initialize class variables
        self.list = DoublyLinkedList()
        self.nodes = {} # dictionary
        # MAKE CAPACITY 5 IF NEGATIVE NUMBER OR ZERO IS PASSED
        if capacity < 1:
            self.capacity = 5
        else:
            self.capacity = capacity

    def get(self, key):
        # Retrieve item from nodes list using provided key.  
        node = self.nodes.get(key, None)
        if node is None:
            # Return -1 if nonexistent.
            # print(-1)
            return -1
        # move the retrieved node to the front of the list
        self.list.move_to_front(node)
        # print('node value : {}'.format(node.dataMap.value))
        # print('prev : {} -> node : {} -> next : {}'.format(node.next,node,node.previous))
        # Return the retrieved node data Mapped value
        return node.dataMap.value

    def size(self):
        return self.capacity

    def set(self, key, value):
        #get node from nodes list
        node = self.nodes.get(key, None)
        if node != None:
            node.dataMap.value = value
            # move the set node to the front of the list
            self.list.move_to_front(node)
            return
        
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.list.len == self.size():
            # Remove bottom node from list
            removed_node = self.list.remove_bottom()
            # Delete the removed bottom node from nodes dictionary
            del self.nodes[removed_node.dataMap.key]
        #if code gets here that means there is space in the cache to accept a new node data
        new_data_map = DataMap(key, value) # assign new key value data map
        node = DoubleNode(new_data_map) # create new double node using the new data map
        self.list.move_to_front(node) # move node to front of list
        self.list.len += 1 #increase list length by 1
        self.nodes[key] = node # add node to nodes dictionary using the key as reference
        # print(node.dataMap.value)
    
def test_function(case):
    data = case[0].get(case[1])
    if data == case[2]:
        print("Pass : returns {}".format(data))
    else:
        print("Fail : returns {}".format(data))
    pass




# Test Case 1

our_cache = LRU_Cache(3)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

test_function([our_cache, 1, 1])       # returns 1
test_function([our_cache,2, 2])       # returns 2
test_function([our_cache,9, -1])       # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.set(7, None)

test_function([our_cache,3, -1])  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

test_function([our_cache,7, None])  # returns None


# Test Case 2
our_cache2 = LRU_Cache(0)

our_cache2.set(1, 1)
our_cache2.set(2, 2)
our_cache2.set(3, 3)
our_cache2.set(4, 4)


test_function([our_cache2, 1, 1])       # returns 1
test_function([our_cache2,2, 2])       # returns 2
test_function([our_cache2,9, -1])       # returns -1 because 9 is not present in the cache

our_cache2.set(5, 5) 
our_cache2.set(6, 6)
our_cache2.set(7, None)

test_function([our_cache2,3, -1])  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

test_function([our_cache2,7, None])  # returns None


our_cache3 = LRU_Cache(-1)

# Test Case 3

our_cache3.set(1, 1)
our_cache3.set(2, 2)
our_cache3.set(3, 3)
our_cache3.set(4, 4)

test_function([our_cache3, 1, 1])       # returns 1
test_function([our_cache3,2, 2])       # returns 2
test_function([our_cache3,9, -1])       # returns -1 because 9 is not present in the cache

our_cache3.set(5, 5) 
our_cache3.set(6, 6)
our_cache3.set(7, None)

test_function([our_cache3,3, -1])  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

test_function([our_cache3,7, None])  # returns None



# For each test case, write the function call with the input you want to test and print it to the console".
# On the next line, comment out the output you expect to see from that function call. At least 2 of these must be edge cases, 
# testing inputs such as null values, empty inputs, unusually large values, etc.
