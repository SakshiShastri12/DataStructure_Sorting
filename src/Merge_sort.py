import time
import sys

file_location = sys.argv[1]
#reading from file
with open(file_location, 'r') as f:
    input_data = []
    for line in f:
        line = line.replace("ÿþ", "")  # Remove specific unwanted characters
        line = ''.join(filter(str.isdigit, line))
         # Write the non-empty line to the output file
        if line.strip():
            input_data.append([int(i) for i in line.split()])


def merge_sort(A, comparison_counter):
    if len(A) <= 1:
        return A, 0

    mid = len(A) // 2
    left = A[:mid]
    right = A[mid:]

    left, comparisons_left = merge_sort(left, comparison_counter)
    right, comparisons_right = merge_sort(right, comparison_counter)
    comparisons = comparisons_left + comparisons_right

    return merge(left, right, comparisons)

#merge procedure
def merge(left, right, comparisons):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        comparisons += 1  
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    comparisons +=1

    result += left[i:]
    result += right[j:]
    return result, comparisons


def merge_sort1(input_data):
    comparison_counter = 0  
    start_time = time.time()  
    
    sorted_data, comparison_counter = merge_sort(input_data, comparison_counter)

    end_time = time.time()  
    #converting execution time into milliseconds
    execution_time = (end_time - start_time)*1000
    #writing in output file
    with open('merge_output.csv', 'a') as f: 
        
        f.write("\n" + str(len(input_data)) + "," + str(comparison_counter) + "," + str(execution_time))

    
    return str(len(input_data)) + "," + str(comparison_counter) + "," + str(execution_time)

#printing the output.
print(merge_sort1(input_data))







