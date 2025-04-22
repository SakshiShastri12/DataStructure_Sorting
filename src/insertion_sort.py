#Name: Sakshi Shastri
#Class: DAA class CS-5120
#Algorithm name: Insertion sort
#Due date: 09-12-2023
#Description: This program is sorting data of 20 input files using insertion sort and calculating the size of input, comparisions and execution time.


import time
import sys

file_location = sys.argv[1]


def insertionSorting(array): 
    #recording the current time
    start = time.time()
    

#initializing the comparision_counter
    comparision_counter = 0
    
    for i in range(1, len(array)): 
        temp = array[i]
        j = i-1
        comparision_counter += 1
        while j >= 0 and temp < array[j]:
            comparision_counter += 1
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = temp

    end= time.time()
    #calculating execution time
    execution_time = (end - start)*1000
    
 #opening the output file in append mode
    with open('insertion_output.csv','a') as f:
        #writing the output in the output file
        f.write("\n" + str(len(array))+"," +str(comparision_counter)+"," +str(execution_time))
        
        

    #print output
    return str(len(array))+"," +str(comparision_counter)+ "," +str(execution_time)

    #reading from the file
with open(file_location,'r') as f:
    
    input_data = []
    for line in f:
        line = line.replace("ÿþ", "")  # Remove specific unwanted characters
        line = ''.join(filter(str.isdigit, line))
        # Write the non-empty line to the output file
        if line.strip():
            
            input_data.append([int(i) for i in line.split()])

#calling function insertionSorting
print(insertionSorting(input_data))

    
        
        
        
 
 
