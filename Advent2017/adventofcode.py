import math

def advent1(data):
    num_str_list = list(data)
    while num_str_list[0] == num_str_list[-1]:
        # fucking circle
        num_str_list.append(num_str_list[0])
        num_str_list = num_str_list[1:]

    num_str_list.append("0")  # to ensure adding the last one

    total = 0
    last = -1
    order = 0
    for c_str in num_str_list:
        c = int(c_str)
        if c == last:
            order += 1
        else:
            if order >= 2:
                total += last * (order - 1)
            order = 1

        last = c

    return total


def get_circ_index(index, count):
    if index >= count:
        index = index - count
    if index < 0:
        index = index + count
    return index


def advent1_2(data):
    num_str_list = list(data)
    count = len(num_str_list)
    halfway = round(count / 2)
    total = 0

    for i in range(count):
        if num_str_list[i] == num_str_list[get_circ_index(i + halfway, count)]:
            total += int(num_str_list[i])
    return total


def advent2(data):
    row_list = data.split('\n')
    total = 0
    for row in row_list:
        item_list = row.split()
        row_total = 0
        highest = 0
        lowest = -1  # first number goes there
        for item in item_list:
            num = int(item)
            if lowest == -1 or num < lowest:
                lowest = num
            if num > highest:
                highest = num
        total += (highest - lowest)
    return total

def get_first_even_divide(number, divider_list):  # func returns 0 if not evenly
    for div in divider_list:
        div = int(div)
        if div == number: # easiest way
            continue
        if ((number % div) == 0):
            return number // div
    return 0

def advent2_2(data):
    row_list = data.split('\n')
    total = 0
    for row in row_list:
        item_list = row.split()
        for item in item_list: #yes, O(n^2), order matters!
            num = int(item)
            total += get_first_even_divide(num, item_list)
    return total

