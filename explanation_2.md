# Udacity-SHOW-ME-THE-DATA-STRUCTURES

Submission to Udacity's SHOW-ME-THE-DATA-STRUCTURES Problems

Run time analysis (Worst Case Big-O Notation) of solution

Get Time Taken to run using : time python <filename>

- Why i used array list data structure to solve this problem ?

Because this problem requires me to search for files from a list of directories. my solution uses the 0(n) complexity to search through the directory and return matching files

- TASK 2 :

  - Algorithm for Find files Function :

    - get list of directories in path.0(n)
    - get list of files with suffix, within directory. 0(n)
    - Return the retrieved files

  - Algorithm For get_directories Function :

    - Traverse through list directory 0(n).
      - Return empty list if no directory found.
    - Return the retrieved directory list

  - Algorithm For get_files_with_suffix Function :
    - Sorted list of directory 0(n log n)
    - Traverse through sorted list of directory 0(n).
      - Return empty list if no file with suffix found.
    - Return the retrieved file list
