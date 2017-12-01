import math

def advent1(input):
    num_str_list = list(input)
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


def advent1_2(input):
    num_str_list = list(input)
    count = len(num_str_list)
    halfway = round(count / 2)
    total = 0

    for i in range(count):
        if num_str_list[i] == num_str_list[get_circ_index(i + halfway, count)]:
            total += int(num_str_list[i])
    return total
