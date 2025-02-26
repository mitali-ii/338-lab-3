import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def traditional_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > val:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = val
    return arr

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start + 1

    if start > end:
        return start

    mid = (start + end) // 2
    if arr[mid] < val:
        return binary_search(arr, val, mid + 1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid - 1)
    else:
        return mid

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i - 1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i + 1:]
    return arr


sizes = [100, 200, 300, 400, 500, 800, 1000, 1200, 1500, 1700, 2000, 2500, 3000, 3500]
traditional_insertion_times = []
binary_insertion_times = []

for size in sizes:
    arr = [random.randint(0, 10000) for i in range(size)]
    
    traditional_insertion_time = timeit.timeit(lambda: traditional_insertion_sort(arr.copy()), number=1)
    traditional_insertion_times.append(traditional_insertion_time)
    
    binary_insertion_time = timeit.timeit(lambda: binary_insertion_sort(arr.copy()), number=1)
    binary_insertion_times.append(binary_insertion_time)


def quadratic_func(x, a, b, c):
    return (a * (x**2)) + (b * x) + (c)

# Fit the curves to the data using curve_fit
interpolated_traditional, _ = curve_fit(quadratic_func, sizes, traditional_insertion_times)
interpolated_binary, y = curve_fit(quadratic_func, sizes, binary_insertion_times)


plt.plot(sizes, quadratic_func(np.array(sizes), *interpolated_traditional), label="Traditional Insertion Sort", color='blue')
plt.plot(sizes, quadratic_func(np.array(sizes), *interpolated_binary), label="Binary Insertion Sort", color='red')

plt.xlabel('Array Size')
plt.ylabel('Time')
plt.legend()
plt.title('Traditional and Binary Insertion Sorts')
plt.show()



#Discuss the results: which algorithm is faster? Why?

#Binary insertion sort is faster than traditional insertion sort because although both have the same time complexity of O(n²), 
#but binary insertion sort uses binary search to find the insertion point, reducing the number of comparisons compared to 
#the linear scan in traditional insertion sort. Both algorithms involve shifting elements but the reduced comparison part 
#makes binary insertion sort faster, especially for larger arrays.







