import time
import sys

file_location = sys.argv[1]
with open(file_location, 'r') as f:
    input_data = []
    for line in f:
        line = line.replace("ÿþ", "")  # Remove specific unwanted characters
        line = ''.join(filter(str.isdigit, line))
        if line.strip():
            input_data.append([int(i) for i in line.split()])

def merge(arr, p, q1, q2, q3, r, comparision_counter):
    n1 = q1 - p + 1
    n2 = q2 - q1
    n3 = q3 - q2
    n4 = r - q3

    L = arr[p:q1+1]
    M = arr[q1+1:q2+1]
    N = arr[q2+1:q3+1]
    O = arr[q3+1:r+1]

    i = j = k = l = 0
    m = p

    while i < n1 and j < n2 and k < n3 and l < n4:
        comparision_counter[0] += 1
        if L[i] <= M[j] and L[i] <= N[k] and L[i] <= O[l]:
            arr[m] = L[i]
            i += 1
        elif M[j] <= L[i] and M[j] <= N[k] and M[j] <= O[l]:
            arr[m] = M[j]
            j += 1
        elif N[k] <= L[i] and N[k] <= M[j] and N[k] <= O[l]:
            arr[m] = N[k]
            k += 1
        else:
            arr[m] = O[l]
            l += 1
        m += 1

    while i < n1:
        arr[m] = L[i]
        i += 1
        m += 1

    while j < n2:
        arr[m] = M[j]
        j += 1
        m += 1

    while k < n3:
        arr[m] = N[k]
        k += 1
        m += 1

    while l < n4:
        arr[m] = O[l]
        l += 1
        m += 1

def mergeSort4(arr, p, r,comparision_counter):
    if r - p <= 3:
        arr[p:r+1] = sorted(arr[p:r+1])
        return

    q1 = p + (r - p) // 4
    q2 = p + 2 * (r - p) // 4
    q3 = p + 3 * (r - p) // 4

    mergeSort4(arr, p, q1,comparision_counter)
    mergeSort4(arr, q1+1, q2, comparision_counter)
    mergeSort4(arr, q2+1, q3, comparision_counter)
    mergeSort4(arr, q3+1, r, comparision_counter)
    merge(arr, p, q1, q2, q3, r, comparision_counter)

def mergeSort4way(arr):
    start = time.time()
    comparision_counter = [0]

    mergeSort4(input_data, 0, len(input_data)-1, comparision_counter)
    end = time.time()
    execution_time = end - start

    with open('4waymergeoutput.csv', 'a') as f:
        # writing the output in the output file
        f.write("\n" + str(len(input_data)) + "," + str(comparision_counter) + "," + str(execution_time))

    # print output
    return str(len(input_data)) + "," + str(comparision_counter) + "," + str(execution_time)

print(mergeSort4way(input_data))


