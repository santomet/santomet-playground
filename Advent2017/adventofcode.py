import math

# DAY 1 -------------------------------------------------------------
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

# DAY 2 ----------------------------------------------------------------
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

# DAY 3 -----------------------------------------------------------------------
def get_sum_near(matrix, x, y):  # matrix is dictionary/map
    total = 0
    for xx,yy in [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]:
        xx = xx + x
        yy = yy + y
        if (xx,yy) in matrix:
            total += matrix[(xx,yy)]
    return total

def advent3(data):
    num = int(data) - 1
    x = 0
    y = 0
    steps = 1
    used_steps = 0
    direction = 3  # 0:north 1:west 2:south 3:east
    turns = 0

    # for part 2:
    matrix = {(0,0): 1}  # for simplicity, we can easily address this with negative integers
    first_higher = 0
    # -----------------------
    for i in range(num):
        if direction == 0:
            y += 1
        elif direction == 1:
            x -= 1
        elif direction == 2:
            y -= 1
        elif direction == 3:
            x += 1

        used_steps += 1

        if used_steps == steps:
            direction = (direction + 1)%4
            turns += 1
            used_steps = 0
            if turns%2 == 0:
                steps += 1

        # for part 2:
        if first_higher == 0:
            val = get_sum_near(matrix, x, y)
            matrix[(x,y)] = val
            if val > num:
                first_higher = val
        # --------------------------------
    dist = abs(x) + abs(y)
    print("task 1: {}; task 2: {}".format(dist, first_higher))

# DAY 4 -----------------------------------------------------------
# note: i know that searching for duplicities can be slightly more effective
# buh in this case... fck it
def contains_anagrams(word_list):
    ltc_ml = []  # list of "letter to count" maps
    for word in word_list:
        word = list(word)
        dct = {}
        for c in word:
            if c not in dct:
                dct[c] = word.count(c)
        ltc_ml.append(dct)
    for dct in ltc_ml:
        if ltc_ml.count(dct) > 1:
            return True
    return False

def advent4(data):
    passp_list = data.split('\n')
    total = 0
    total_noana = 0
    for passp in passp_list:
        valid = True
        valid_noana = True
        word_list = passp.split()
        if len(word_list) < 2:
            valid = False
        for word in word_list:
            if word_list.count(word)>1:
                valid = False
        if contains_anagrams(word_list):
            valid_noana = False
            
        if valid:
            total += 1
            if valid_noana:
                total_noana += 1
    print("task 1: {}; task 2: {}".format(total, total_noana))

# DAY 5 -----------------------------------------------------------------------
def advent5(data):
    str_list = data.split('\n')
    int_list = list(map(int, str_list))
    int_list_2 = int_list[:]
    i = 0
    i2 = 0
    steps = 0
    steps_2 = 0
    length = len(int_list)
    first_running = True
    second_running = True
    while first_running or second_running:
        if i >= 0 and i < length:
            move = int_list[i]
            int_list[i] += 1
            i += move
            steps += 1
        else:
            first_running = False
        if i2 >= 0 and i2 < length:
            move = int_list_2[i2]
            if int_list_2[i2] >= 3:
                int_list_2[i2] -= 1
            else:
                int_list_2[i2] += 1
            i2 += move
            steps_2 += 1
        else:
            second_running = False
    print("task 1: {}; task 2: {}".format(steps, steps_2))

# DAY 6 ----------------------------------------------------------------------
def advent6(data):
    str_list = data.split()
    int_list = list(map(int, str_list))
    if not len(int_list) == 16:
        print("ERROR!, only 16 values are allowed for day 6")
        return
    steps = 0
    steps_2 = 0
    history_list = []
    second_part_list = []
    found_first_task = False
    while True:
        if not found_first_task:
            history_list.append(int_list[:])
        grt = max(int_list)
        i = int_list.index(grt)
        int_list[i] = 0
        for n in range(grt):
            i = (i+1)%16
            int_list[i] += 1
        if not found_first_task:
            if history_list.count(int_list) == 0:
                steps += 1
            else:
                found_first_task = True
                steps += 1  # add one step
                second_part_list = int_list[:]
        else:
            steps_2 += 1
            if second_part_list == int_list:
                break

    print("task 1:{}; task 2: {}".format(steps, steps_2))


def main():
    last_solved = 6
    txt = """
      __   ____  _  _  ____  __ _  ____       ____   __    __  ____ 
     / _\ (    \/ )( \(  __)(  ( \(_  _)     (___ \ /  \  /  \(__  )
    /    \ ) D (\ \/ / ) _) /    /  )(  ____  / __/(  0 )(_/ /  / / 
    \_/\_/(____/ \__/ (____)\_)__) (__)(____)(____) \__/  (__) (_/
                                             github.com/santomet

    Hello and welcome! For exit enter e!
    """
    print(txt)
    while True:
        num = input("Which day do you want to solve? Day ")
        if num == 'e':
            break
        if not num.isnumeric():
            continue

        num = int(num)
        print("You have selected Day {}".format(num));
        if num < 1 or num > last_solved:
            print("This day is not defined! Please try another one")
            continue

        print("now, please enter your puzzle input. Afterwards, press ENTER twice")
        data_thisline = input()
        data = ""
        while not data_thisline == "":
            data += data_thisline
            data_thisline = input()
            if not data_thisline == "":
                data += '\n'
        if data == 'e':
            break

        print("COMPUTING.......")
        
        if num == 1:
            print("task 1: {}; task 2: {}".format(advent1(data), advent1_2(data)))
        elif num == 2:
            print("task 1: {}; task 2: {}".format(advent2(data), advent2_2(data)))
        elif num == 3:
            advent3(data)
        elif num == 4:
            advent4(data)
        elif num == 5:
            advent5(data)
        elif num == 6:
            advent6(data)

if __name__ == "__main__":
    main()
