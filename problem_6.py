class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)
    
    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def isPresent(head, value):
    node = head
    # traverse linked list
    while node:
        # if value is in linked list
        if node.value == value:
            return True
        # set next node to current node
        node = node.next
    return False

def union(llist_1, llist_2):
    # Your Solution Here
    result = LinkedList()
    head1 = llist_1.head
    head2 = llist_2.head

    #  append all elements of list1 in the result
    while head1 :
        result.append(head1)
        head1 = head1.next
        
    #  append those elements of list2
    #  that are not present
    while head2 :
        if not isPresent(head1, head2.value):
            result.append(head2)
        head2 = head2.next
    return result

def intersection(llist_1, llist_2):
    # Your Solution Here
    result = LinkedList()
    head1 = llist_1.head

    # Traverse list1 
    while head1 :
        # search each element of it in list2.
        # If the element is present in list 2, 
        if (isPresent(llist_2.head, head1.value)):
            # then append the element to result
            result.append(head1.value)
        # move next head into current head
        head1 = head1.next
    return result



# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = set([3,2,4,35,6,65,6,4,3,21])
element_2 = set([6,32,4,9,6,1,11,21,1])
print(element_1)
print(element_2)

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()


element_1 = set([3,2,4,35,6,65,6,4,3,23])
element_2 = set([1,7,8,9,11,21,1])

print(element_1)
print(element_2)

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)


print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))
