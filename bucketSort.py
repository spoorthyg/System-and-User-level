import os
import psutil
import tracemalloc
from collections import defaultdict
import cProfile
import time
import pandas as pd 
import matplotlib.pyplot as plt

class Bucket_Sort:
    def insertionSort(self, b):
        for i in range(1, len(b)):
            up = b[i]
            j = i - 1
            while j >= 0 and b[j] > up:
                b[j + 1] = b[j]
                j -= 1
            b[j + 1] = up    
        return b

    def bucketSort(self, x):
        arr = []
        slot_num = 10 # 10 means 10 slots, each
                    # slot's size is 0.1
        for i in range(slot_num):
            arr.append([])
            
        # Put array elements in different buckets
        for j in x:
            index_b = int(slot_num * j)
            arr[index_b].append(j)  
        
        # Sort individual buckets
        for i in range(slot_num):
            arr[i] = self.insertionSort(arr[i])
            
        # concatenate the result
        k = 0
        for i in range(slot_num):
            for j in range(len(arr[i])):
                x[k] = arr[i][j]
                k += 1
        
        return x

    def printList(self, arr):
        for i in range(len(arr)):
            print(arr[i], end=" ")
        print()

if __name__ == "__main__":
    start = time.time()
    bucket_sort = Bucket_Sort()
    dictionary = defaultdict()

    # RSS and VMS used by the process
    p = psutil.Process(os.getpid())
    dictionary["rss - mb(s)"] = round(p.memory_info().rss / (1024 * 1024), 2)
    dictionary["vms - mb(s)"] = round(p.memory_info().vms / (1024 * 1024), 2)
    
    # CPU utilization
    dictionary["cpu_usage - %"] = p.cpu_percent()

    # memory used by the process
    tracemalloc.start()
    x = [0.20, 0.22, 0.43, 0.36, 0.39, 0.27]
    print("Sorted Array is")
    cProfile.run("bucket_sort.bucketSort(x)")
    
    traced_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()

    dictionary["memory_usage - mb(s)"] = round(traced_mem[1] / 1024, 2)
    dictionary["exec_time - s"] = round(end - start, 2)
    print(dictionary)
    patches, texts = plt.pie(list(dictionary.values()), radius=0.5)
    labels = [f"{i} - {j}" for i,j in zip(list(dictionary.keys()), list(dictionary.values()))]
    plt.legend(patches, labels, loc="upper right", bbox_to_anchor = (0.4, 0.2))
    plt.title("Bucket sort")
    plt.savefig("BucketSort.png")
    plt.show()