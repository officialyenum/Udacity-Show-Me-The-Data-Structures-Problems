# Udacity-SHOW-ME-THE-DATA-STRUCTURES

Submission to Udacity's SHOW-ME-THE-DATA-STRUCTURES Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Why i used LinkedList data structure to solve this problem ?

This problem requires me to check the union or intersection between two linked list.

- TASK 6 : 0(nk)

  - Space Complexities 
      linkedlist 1 = 0(n)
      linkedlist 2 = 0(k)
      union list = 0(n + k)
      intersection list = 0(n * k)

  - Algorithm for isPresent Function :

    - Traverse through linked list 0(n)
    - if value is in linked list return True else False
    - Return the boolean 0(1)

  - Algorithm for union Function :

    - Traverse through first linked and second linked list and append to result linked list 0(nk)
    - Return the out_list 0(1)

  - Algorithm for intersection Function :
    - Traverse through first linked list and append to result linked list 0(n)
    - Return the out_list 0(1)
