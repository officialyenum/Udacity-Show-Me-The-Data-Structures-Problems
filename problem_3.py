import sys
from typing import ItemsView

'''
Each row in the table above can be represented as a node having a character, frequency, left child, and right child. 
'''
class Node:
    def __init__(self, character, frequency, left = None, right = None):
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right
        self.bit = '' # 0 for left, 1 for right

    def get_character(self):
        return self.character
    
    def set_character(self, character):
        self.character = character
    
    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def set_left_child(self, value):
        self.left = value

    def set_right_child(self, value):
        self.right = value
    
    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

    def get_bit(self):
        return self.bit
    
    def set_bit(self, bit):
        self.bit = bit


class Tree():
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root
    
    def set_root(self, value):
        self.root = Node(value)




def get_char_and_frequency(data):
    '''
    Build and sort a list of nodes in the order lowest to highest frequencies. 
    Remember that a list preserves the order of elements in which they are appended.
    '''
    new_dict = dict()
    for element in data:
        if new_dict.get(element) == None:
            new_dict[element] = 1
        else:
            new_dict[element] +=1
    # return sorted dictionaries by values
    return dict(sorted(new_dict.items(), key=lambda item: item[1]))
'''
Pop-out two nodes with the minimum frequency from the priority queue created in the above step.
'''
def pop_out_two_nodes_with_minimum_frequency(nodes):
    nodes[0].bit = 0
    nodes[1].bit = 1
    return nodes[0], nodes[1]
'''
Create a new node with a frequency equal to the sum of the two nodes picked in the above step. 
This new node would become an internal node in the Huffman tree, 
and the two nodes would become the children. 
The lower frequency node becomes a left child, 
and the higher frequency node becomes the right child. 
Reinsert the newly created node back into the priority queue.
'''

def create_new_node(left, right):
    return Node(right.character + left.character, right.frequency + left.frequency, left, right)

def generate_encoded_data(node, old_bit=''):
    new_value = old_bit + str(node.bit)

    if node.left:
        generate_encoded_data(node.left, new_value)
    if node.right:
        generate_encoded_data(node.right, new_value)
    if not node.left and not node.right:
        codes[node.character] = new_value
    return codes

def huffman_encoding(data):
    if data == '':
        return '0', []
    codes = get_char_and_frequency(data)
    node_list = list()
    for item in codes:
        node_list.append(Node(item, codes[item]))

    while len(node_list) > 1:
        left_node, right_node = pop_out_two_nodes_with_minimum_frequency(node_list)

        new_node = create_new_node(left_node, right_node)

        node_list.remove(left_node)
        node_list.remove(right_node)
        node_list.append(new_node)
    
    encoding_data = generate_encoded_data(node_list[0])
    output_list = []
    for item in codes:
        output_list.append(encoding_data[item])
    output_string = ''.join([str(item) for item in output_list])
    return output_string, node_list[0]
    
def huffman_decoding(data,tree):
    '''
    Declare a blank decoded string
    Pick a bit from the encoded data, traversing from left to right.
    Start traversing the Huffman tree from the root.
    If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
    If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
    Repeat steps #2 and #3 until the encoded data is completely traversed.
    '''
    tree_top = tree
    decoded_output = []
    decoded_string = ''

    if tree_top == []:
        return decoded_string
        
    # for bit in data:
    #     if bit == '1':
    #         tree = tree.right   
    #     elif bit == '0':
    #         tree = tree.left
    #     try:
    #         if tree.left.character == None and tree.right.character == None:
    #             pass
    #     except AttributeError:
    #         decoded_output.append(tree.character)
    #         tree = tree_top
        
    # string = ''.join([str(item) for item in decoded_output])
    # return string

    for item in data:
        if item == "0":
            tree = tree.left
        else:
            tree = tree.right
        if tree.left == None and tree.right == None:
            # append character
            decoded_string += tree.character
            # reset tree to top
            tree = tree_top
    return decoded_string

if __name__ == "__main__":
    codes = {}

    # Test case 1
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 2
    a_great_sentence = ""

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Test case 3
    a_great_sentence = "The size of the decoded data is The bird"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
