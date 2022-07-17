import copy
import time
import random
from algorithm.check.sorting import is_sorted

""" Sorting algorithms """


# My first algorithm
def sort_1(data):
    swap_counter = 0
    data_length = len(data)
    if len(data) <= 1:
        return data
    for number in data:
        # Sorting cycle
        this_place = data.index(number)
        next_place = this_place + 1
        if next_place == data_length:
            next_place = 0
        next_num = data[next_place]
        if next_place != 0 and number > next_num:
            data[this_place], data[next_place] = next_num, number
            swap_counter += 1
    # Repeat sorting when swaps more than 0
    if swap_counter > 0:
        sort_1(data)
    return data


# Buble sorting
def sort_2(data):
    data_length = len(data)
    step = 1
    while step < len(data):
        for item in range(data_length - step):
            if data[item] > data[item + 1]:
                data[item], data[item + 1] = data[item + 1], data[item]
        step += 1
    # print(f'Steps sort_2: {step}')
    return data


# NOT WORKING
# TODO: Refactor
def global_sorting(unsorted):
    full_list = is_sorted(unsorted)
    mid = len(full_list) // 2

    first_part = full_list[mid:]
    second_part = first_part[:mid]


# NOT WORKING
# TODO: Refactor
def sorting(data):
    for number in data:
        if number < data[0]:
            data.remove(number)
            data.insert(0, number)
        elif number > data[-1]:
            data.remove(number)
            data.append(number)
    return data


# Default Bubble sorting algorithm
def bubble_sort(data):
    n = 1
    while n < len(data):
        for i in range(len(data) - n):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        n += 1
    # print(f'Steps bubble: {n}')
    return data


# DATA PREPARATION ZONE
list_1 = [4, 10, 6, 3, 2, 7, 8, 25, 22, 1]
# x = random.sample(range(1, 10000), 1000)
# x1 = copy.deepcopy(x)
payload = list_1
algo = sort_1(data=payload)

# SORTING ZONE
is_sorted(payload)
print(f'Data for sorting: {payload} \n')

# Time calculation start
start = time.time()
x = algo
print(f'Calc sorting time: {round(((time.time() - start) * 1000), 3)} milliseconds \n')
# Time calculation end

is_sorted(x)
print(x)
