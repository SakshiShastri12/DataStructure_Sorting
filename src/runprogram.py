from subprocess import call
import sys

def open_py_file():
    fileName = sys.argv[1]
    call(["python", "insertion_sort.py",fileName])
    call(["python", "Merge_sort.py",fileName])
    call(["python", "heapsort.py",fileName])
    call(["python", "4waymergesort.py",fileName])

open_py_file()    
