import sys
import time
import math
from random import randint
import multiprocessing
import matplotlib.pyplot as plt


def recursive_merge_sort(arr):
    length = len(arr)

    if length < 2:
        return arr

    mid = int(length / 2)

    left = recursive_merge_sort(arr[:mid])
    right = recursive_merge_sort(arr[mid:])

    return merge_arrays(left, right)

def merge_arrays(*args):
    left, right = args[0] if len(args) == 1 else args

    len_left = len(left)
    len_right = len(right)

    left_index = 0
    right_index = 0
    new_arr = []
    while left_index < len_left and right_index < len_right:
        if left[left_index] <= right[right_index]:
            new_arr.append(left[left_index])
            left_index += 1
        else:
            new_arr.append(right[right_index])
            right_index += 1

    if left_index == len_left:
        new_arr.extend(right[right_index:])
    else:
        new_arr.extend(left[left_index:])

    return new_arr

def split_array(arr, pieces):
    size = math.ceil(len(arr) / pieces)
    for i in range(pieces):
        start = i * size
        end = (i + 1) * size
    return [arr[start:end] for i in range(pieces)]

def threaded_merge_sort(arr, number_of_processes=8):
    thread_pool = multiprocessing.Pool(processes=number_of_processes)

    splitted_arr = split_array(arr, number_of_processes)
    
    arr = thread_pool.map(recursive_merge_sort, splitted_arr)

    while len(arr) > 1:
        remain = arr.pop() if len(arr) % 2 == 1 else None

        arr = [(arr[i], arr[i + 1]) for i in range(0, len(arr), 2)]

        arr = thread_pool.map(merge_arrays, arr) + ([remain] if remain else [])
    
    return arr[0]


def test_sort_function(func_name, size=10000, *args):
    arr = [randint(0, size) for _ in range(size)]
  
    start = time.time()
    sorted_arr = func_name(arr, *args)
    end = time.time()

    total_time = end - start

    return total_time, sorted(arr) == sorted_arr

if __name__ == "__main__":
    SIZES = [1000, 2000, 4000, 8000, 16000, 32000, 64000]
    # SIZES = [10, 20, 40, 80, 160, 320, 640]
    NUMBER_OF_PROCESSES = [1,2,4]
    ITERATIONS = 3

    results = {}
    for processes in NUMBER_OF_PROCESSES:
        print(processes)
        results[processes] = {}

        for size in SIZES:
            running_total = 0

            for _ in range(ITERATIONS):
                total_time, valid = test_sort_function(threaded_merge_sort, size, processes)
                running_total += total_time

            results[processes][size] = running_total / ITERATIONS


    for result in results:
        plt.plot(SIZES, list(results[result].values()), label=result)
    plt.legend()
    plt.savefig('complexityThreadedMergeSort.png')
    plt.show()
