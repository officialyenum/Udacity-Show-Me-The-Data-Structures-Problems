# Udacity-SHOW-ME-THE-DATA-STRUCTURES

Submission to Udacity's SHOW-ME-THE-DATA-STRUCTURES Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Why i used LinkedList data structure to solve this problem ?

This problem requires me to check if a user exists in a list of users from a group class. my solution uses the 0(1) complexity to append object to the linked list tail and 0(n) traverse through the nodes linked list to return list of blockchain hash

- TASK 5 :

  - Algorithm for BlockLinkedList append Function :

    - Move to the tail (the last node) 0(1)
    - get tail hash and create new block node with it 0(1)
    - reset new block node to tail it 0(1)

    - Algorithm for BlockLinkedList to_list Function :
      - Traverse through linked list of blocks and append to out_list 0(n)
      - Return the out_list 0(1)
