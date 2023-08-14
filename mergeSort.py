import os
import psutil
import tracemalloc
import cProfile
import random
from collections import defaultdict
import time
import matplotlib.pyplot as plt
#import pprint from pprint

class Merge_Sort:
    def mergeSort(self, arr):
        if len(arr) > 1:
    
            # Finding the mid of the array
            mid = len(arr)//2
    
            # Dividing the array elements
            L = arr[:mid]
    
            # into 2 halves
            R = arr[mid:]
    
            # Sorting the first half
            self.mergeSort(L)
    
            # Sorting the second half
            self.mergeSort(R)
    
            i = j = k = 0
    
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
    
            # Checking if any element was left
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
    
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
    
    # Code to print the list
    
    def printList(self, arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()
         
if __name__ == '__main__':
    start = time.time()
    merge_sort = Merge_Sort()
    dictionary = defaultdict()

    # RSS and VMS used by the process
    p = psutil.Process(os.getpid())

    dictionary["rss - mb(s)"] = round(p.memory_info().rss / (1024 * 1024), 2)
    dictionary["vms - mb(s)"] = round(p.memory_info().vms / (1024 * 1024), 2)
    
    # CPU utilization
    dictionary["cpu_usage - %"] = p.cpu_percent()

    # memory used by the process
    tracemalloc.start()
    arr = random.sample(range(1,100), 70)
    print("Given array is", end="\n")
    merge_sort.printList(arr)
    
    cProfile.run('merge_sort.mergeSort(arr)')
    print("Sorted array is: ", end="\n")
    merge_sort.printList(arr)
    
    traced_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()

    dictionary["memory_usage mb(s)"] = round(traced_mem[1] / 1024, 2)
    dictionary["exec_time - s"] = round(end - start, 2)
    print(dictionary)
    patches, texts = plt.pie(list(dictionary.values()), radius=0.5)
    labels = [f"{i} - {j}" for i,j in zip(list(dictionary.keys()), list(dictionary.values()))]
    plt.legend(patches, labels, loc="upper right", bbox_to_anchor = (0.4, 0.2))    
    plt.title("Merge Sort")
    plt.savefig("MergeSort.png")
    plt.show()
