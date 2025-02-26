import random
import timeit
import matplotlib.pyplot as plt

def bubblesort(arr):       
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


def quicksort(arr, low, high):
    if low < high:
        pivot_index = bestPartition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)
    return arr

def bestPartition(arr, low, high):
    pivot = arr[(low + high) // 2]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def worstCaseQuicksort(arr, low, high):
    if low < high:
        pivot_index = worstPartition(arr, low, high)
        worstCaseQuicksort(arr, low, pivot_index - 1)
        worstCaseQuicksort(arr, pivot_index + 1, high)
    return arr

def worstPartition(arr, low, high):
    pivot = min(arr)
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right



#plot1 - sorted array
plot1_bubblesortTimes = []
plot1_bestquicksortTimes = []
plot1_worstquicksortTimes = []

#plot2 - reverse sorted array
plot2_bubblesortTimes = []
plot2_bestquicksortTimes = []
plot2_worstquicksortTimes = []

#plot3 - random array
plot3_bubblesortTimes = []
plot3_bestquicksortTimes = []
plot3_worstquicksortTimes = []


sizes = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]


for size in sizes:
    sorted_arr = sorted([random.randint(0, 10000) for x in range(size)])
    reverseSorted_arr = sorted([random.randint(0, 10000) for x in range(size)], reverse=True)
    random_arr = [random.randint(0, 10000) for x in range(size)]


    plot1_bubblesortTimes.append(timeit.timeit(lambda: bubblesort(sorted_arr.copy()), number=1))
    plot1_bestquicksortTimes.append(timeit.timeit(lambda: quicksort(sorted_arr.copy(), 0, len(sorted_arr)-1), number=1))
    plot1_worstquicksortTimes.append(timeit.timeit(lambda: worstCaseQuicksort(sorted_arr.copy(), 0, len(sorted_arr)-1), number=1))        

    plot2_bubblesortTimes.append(timeit.timeit(lambda: bubblesort(reverseSorted_arr.copy()), number=1))
    plot2_bestquicksortTimes.append(timeit.timeit(lambda: quicksort(reverseSorted_arr.copy(), 0, len(sorted_arr)-1), number=1))
    plot2_worstquicksortTimes.append(timeit.timeit(lambda: worstCaseQuicksort(reverseSorted_arr.copy(), 0, len(sorted_arr)-1), number=1))

    plot3_bubblesortTimes.append(timeit.timeit(lambda: bubblesort(random_arr.copy()), number=1))
    plot3_bestquicksortTimes.append(timeit.timeit(lambda: quicksort(random_arr.copy(), 0, len(sorted_arr)-1), number=1))
    plot3_worstquicksortTimes.append(timeit.timeit(lambda: worstCaseQuicksort(random_arr.copy(), 0, len(sorted_arr)-1), number=1))


fig, axs = plt.subplots(1, 3) 

axs[0].plot(sizes, plot1_bubblesortTimes, color='green', label="Bubble Sort")
axs[0].plot(sizes, plot1_bestquicksortTimes, color='red', label="Best Case Quick Sort")
axs[0].plot(sizes, plot1_worstquicksortTimes, color='blue', label="Worst Case Quick Sort")
axs[0].set_title("Sorted Array")
axs[0].set_xlabel("Input Size")
axs[0].set_ylabel("Time")
axs[0].set_ylim(0, 0.0008)
axs[0].legend()

axs[1].plot(sizes, plot2_bubblesortTimes, color='green', label="Bubble Sort")
axs[1].plot(sizes, plot2_bestquicksortTimes, color='red', label="Best Case Quick Sort")
axs[1].plot(sizes, plot2_worstquicksortTimes, color='blue', label="Worst Case Quick Sort")
axs[1].set_title("Reverse Sorted Array")
axs[1].set_xlabel("Input Size")
axs[1].set_ylabel("Time")
axs[1].set_ylim(0, 0.0008)
axs[1].legend()

axs[2].plot(sizes, plot3_bubblesortTimes, color='green', label="Bubble Sort")
axs[2].plot(sizes, plot3_bestquicksortTimes, color='red', label="Best Case Quick Sort")
axs[2].plot(sizes, plot3_worstquicksortTimes, color='blue', label="Worst Case Quick Sort")
axs[2].set_title("Random Array")
axs[2].set_xlabel("Input Size")
axs[2].set_ylabel("Time")
axs[2].set_ylim(0, 0.0008)
axs[2].legend()

plt.show()
plt.savefig("ex2.png")
