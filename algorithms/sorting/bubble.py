import copy
import time
import random

""" Sorting algorithms """

list_1 = [4, 10, 6, 3, 2, 7, 8, 25, 22, 1]


def sort1(data):
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
        sort1(data)
    return data


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


# WORKING
def check_sorted(data):
    sort_status = False
    if len(data) <= 1:
        sort_status = True
        return data
    elif len(data) > 1 and sort_status is False:
        scope = len(data) - 1
        for n in range(scope - 1):
            if data[scope] > data[scope - 1]:
                scope -= 1
                sort_status = True
            else:
                sort_status = False
                break
        if scope == 1 and sort_status is True:
            print('Data is sorted')
            return data
        else:
            print('Data is not sorted')
            return data


# Default wiki algorithms
def bubble_sort(data):
    n = 1
    while n < len(data):
        for i in range(len(data) - n):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
        n += 1
    # print(f'Steps bubble: {n}')
    return data


# x = random.sample(range(1, 10000), 1000)
# x1 = copy.deepcopy(x)

start_4 = time.time()
check_sorted(list_1)
print(f'Calc time lol sort: {round(((time.time() - start_4) * 1000), 3)} milliseconds')
