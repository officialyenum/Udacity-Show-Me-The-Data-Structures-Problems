# Udacity-SHOW-ME-THE-DATA-STRUCTURES

Submission to Udacity's SHOW-ME-THE-DATA-STRUCTURES Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Why i used Tree data structure to solve this problem ?

This problem requires me to encode characters into binary and decode it back into characters. my solution uses the 0(log n) complexity to search through the directory and return matching files

The tree data structure helps me keep track of the binary children of every parent node

- TASK 3 :

  - Algorithm for huffman_encoding Function :
    
    - get char and frequency dictionary data 0(n)
    - Traverse the data and append to list of nodes 0(n)
    - pop out the last two nodes and remove it from the list and append a single new node to that list
    - generate encoding data using the first element in the node list
    - traverse through the codes dictionary and append corresponding encoding data to output list
    - convert output list to string
    - return output string and node list first item 

  - Algorithm For huffman_decoding Function :

    - Declare a blank decoded string
    - Pick a bit from the encoded data, traversing from left to right.
    - Start traversing the Huffman tree from the root.
    - If the current bit of encoded data is 0, move to the left child, else move to the right child of the tree if the current bit is 1.
    - If a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string.
    - Repeat steps #2 and #3 until the encoded data is completely traversed.
    
