# Udacity-SHOW-ME-THE-DATA-STRUCTURES

Submission to Udacity's SHOW-ME-THE-DATA-STRUCTURES Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Why i used Tree data structure to solve this problem ?

This problem requires me to encode characters into binary and decode it back into characters. 

This binaries will be represented in a tree like data structure where the left child node will be 0 and right child node will be 1

The tree data structure helps me keep track of the binary children of every parent node

- TASK 3 : Worst Case : 0(n log n) 
  
  - Space Complexities 

    - char and frequency dictionary = 0(n)
    - create new node = 0(1)
    - list of nodes = 0(n)
    - encoded data = 0(n)
    - decoded data = 0(n)

  - Algorithm for huffman_encoding Function :
    - get char and frequency dictionary data 0(n)
    - Traverse the data and append to list of nodes 0(n)
    - pop out the last two nodes and remove it from the list and append a single new node to that list 0(log n)
    - generate encoding data using the first element in the node list 0(1)
    - traverse through the codes dictionary and append corresponding encoding data to output list 0(n)
    - convert output list to string
    - return output string and node list first item 0(n)

  - Algorithm For huffman_decoding Function :

    - Declare a blank decoded string 0(1) space
    - Pick a bit from the encoded data, traversing the Huffman tree from the root. O(n)
    - If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1. 0(1)
    - If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string. 0(1)
    - Repeat until the encoded data is completely traversed.
    
