## Locally save and call this file ex.py ##

# Code to demonstrate the use of some of the OS modules in python

import os

# Let us print the files in the directory in which you are running this script
# print (os.listdir("."))
# print (len(os.listdir(".")))
# print(os.walk("./testdir"))

# Let us check if this file is indeed a file!
# print (os.path.isfile("./ex.py"))

# Does the file end with .py?
# print ("./ex.py".endswith(".py"))


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
      a list of paths
    """
    directories = list() # initialize directory list
    files = list() # initialize file list
    directories = get_directories(path) # get list of directories with path
    files = get_files_with_suffix(suffix, directories) # get list of files with suffix and list of directories
    return files

    

def get_directories(path):
  # declare empty directory list
  directories = list()
  # set recursive breakpoint if list of directory length is 0 return empty list
  if len(os.listdir(path)) == 0:
    return []
  # traverse list of directory
  for file in os.listdir(path):
      # is current file or path a directory
      if os.path.isdir(file) or os.path.isdir(os.path.join(path, file)):
        # get list of data in current directory
        new_directories = get_directories(os.path.join(path, file))
        # join new directories list with old
        directories += new_directories
      else:
        # append current path to directory
        directories.append(os.path.join(path, file))
  # return list of directories
  return directories

def get_files_with_suffix(suffix, directories):
  # declare empty file list
  files = list()
  # traverse through sorted directory 
  for file in sorted(directories):
    if file.endswith(suffix):
        # append file that ends with suffix to file list
        files.append(file)
  # return file list
  return files

# test case 1
suffix = ".c"
path = "."

data = find_files(suffix,path)
print(data)

# test case 2
suffix = ".h"
path = "."

data = find_files(suffix,path)
print(data)
