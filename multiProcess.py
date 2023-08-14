from concurrent.futures import process
from multiprocessing import Process
from collections import defaultdict
from bucketSort import Bucket_Sort
from mergeSort import Merge_Sort
import matplotlib.pyplot as plt
import tracemalloc
import random
import psutil
import time
import os

def merge_sort():
    merge_sort = Merge_Sort()
    arr = random.sample(range(1,100), 70)
    print("Given array for merge sort is", end="\n")
    merge_sort.printList(arr)

    merge_sort.mergeSort(arr)
    
    print("Sorted array for merge sort is: ", end="\n")
    merge_sort.printList(arr)

def bucket_sort():
    bucket_sort = Bucket_Sort()
    arr = [0.20, 0.22, 0.43, 0.36, 0.39, 0.27]

    print("Given array for bucket sort is", end="\n")
    bucket_sort.printList(arr)
    
    bucket_sort.bucketSort(arr)
    
    print("Sorted Array for bucket sort is", end="\n")
    bucket_sort.printList(arr)

if __name__ == "__main__":
    start = time.time()
    dictionary = defaultdict()

    # RSS and VMS used by the process
    p = psutil.Process(os.getpid())

    dictionary["rss - mb(s)"] = round(p.memory_info().rss / (1024 * 1024), 2)
    dictionary["vms - mb(s)"] = round(p.memory_info().vms / (1024 * 1024), 2)
    
    # CPU utilization
    dictionary["cpu_usage - %"] = p.cpu_percent()

    # memory used by the process
    tracemalloc.start()
    process1 = Process(target=merge_sort())
    process2 = Process(target=bucket_sort())
    process1.start(), process2.start()
    
    traced_mem = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end = time.time()

    dictionary["memory_usage - mb(s)"] = round(traced_mem[1] / 1024, 2)
    dictionary["exec_time - s"] = round(end - start, 2)
    print(dictionary)
    patches, texts = plt.pie(list(dictionary.values()), radius=0.5)
    labels = [f"{i} - {j}" for i,j in zip(list(dictionary.keys()), list(dictionary.values()))]
    plt.legend(patches, labels, loc="upper right", bbox_to_anchor = (0.4,0.2))
    plt.title("Merge Sort and Bucket Sort")
    plt.savefig("MergeSort&BucketSort.png")
    plt.show()
