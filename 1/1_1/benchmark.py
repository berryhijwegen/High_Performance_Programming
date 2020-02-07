import time
import random
import sorting_algorithms

def time_algorithms(algorithms, lists):
    for algorithm in algorithms:
        item = getattr(sorting_algorithms, algorithm)
        if callable(item):
            print(item.__name__, time_function(item, lists))

def time_function(func, lists):
    results = {}
    for length, values in lists.items():
        time1 = time.time()
        func(values)
        time2 = time.time()
        results[length] = time2 - time1

    return results


if __name__ == "__main__":
    lenghts = ['1000', '10000', '30000']

    lists = {
        length: [random.randrange(1, 50, 1) for _ in range(int(length))] for length in lenghts}
    lists['30000sorted'] = list(sorted(lists['30000']))
    lists['30000reversed'] = list(reversed(lists['30000']))

    algorithms = [
        'selection_sort',
        'insertion_sort',
        'merge_sort',
		'bucket_sort'
    ]

    time_algorithms(algorithms, lists)