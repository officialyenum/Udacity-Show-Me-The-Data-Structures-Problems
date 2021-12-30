# Udacity-SHOW-ME-THE-DATA-STRUCTURES

Submission to Udacity's SHOW-ME-THE-DATA-STRUCTURES Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Why i used DoublyLinkedList data structure to solve this problem ?

Because this problem requires me to keep track of what is at the top and bottom of the list and get sorted per function call to enable retrieval use a 0(1) complexity when deleting the least recently used cache data -

- TASK 1 :

  - Algorithm for LRU_CACHE :

    - create dataMap class with key and value argument.
    - create doubleNode class with dataMap argument.
    - create doublyLinkedList class to hold the nodes together.
    - create LRU_CACHE class to hold nodes, list and capacity
    - create get function for LRU_CACHE class with key argument.
    - create set function for LRU_CACHE class with no argument.
    - create size function for LRU_CACHE class with no argument.
    - move the retrieved node to the front of the list
    - Return the retrieved node data Mapped value

  - Algorithm For LRU_CACHE get Function :

    - Retrieve item from nodes list using provided key.
      - Return -1 if nonexistent.
    - move the retrieved node to the front of the list
    - Return the retrieved node data Mapped value

  - Algorithm For LRU_CACHE set Function :
    - Initialize class variables
    - Retrieve item from nodes list using provided key.
      - Return -1 if nonexistent.
    - move the retrieved node to the front of the list
    - Return the retrieved node data Mapped value
