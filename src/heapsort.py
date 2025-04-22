import time
import sys

file_location = sys.argv[1]
#reading from file
with open(file_location, 'r') as f:
    input_data = []
    for line in f:
        line = line.replace("ÿþ", "")  # Remove specific unwanted characters
        line = ''.join(filter(str.isdigit, line))
        if line.strip():
            input_data.append([int(i) for i in line.split()])


def heapify(A, n, i, comparision_counter):
      
      largest = i
      l = 2 * i 
      r = 2 * i + 1
      
      comparision_counter[0] += 1
      if l < n and A[i] < A[l]:
          largest = l

      comparision_counter[0] += 1
      if r < n and A[largest] < A[r]:
          largest = r
  
      
      if largest != i:
          A[i], A[largest] = A[largest], A[i]
          heapify(A, n, largest, comparision_counter)
def heapSort(A):
      start_time = time.time()
      n = len(A)
      comparision_counter = [0]
  
      # Building max heap
      for i in range(n//2, -1, -1):
          heapify(A, n, i, comparision_counter)
  
      for i in range(n-1, 0, -1):
          # Swap
          A[i], A[0] = A[0], A[i] #swapping
  
          
          heapify(A, i, 0, comparision_counter)
          end_time = time.time()
          execution_time = (end_time - start_time)*1000   #converting execution time to milliseconds
          with open('heap_output.csv', 'a') as f:
            f.write("\n" + str(len(input_data)) + "," + str(comparision_counter) + "," + str(execution_time))


          return str(len(input_data)) + "," + str(comparision_counter) + "," + str(execution_time)

#printing output   
print(heapSort(input_data))




        

  
  
  
  