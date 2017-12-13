import math
from operator import itemgetter

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

# DAY 7-------------------------------------------------------------
# too much oop, solutions on reddit caused a depression...

class Program:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.parent = None
        self.children = []
        
        self.total_weight = weight
        self.total_children = 0

    def __str__(self):
        return self.name
    def __eq__(self, other):
        return self.name == other.name

    def propagate_info_to_root(self, weight_to_add):
        self.total_children += 1
        self.total_weight += weight_to_add
        if self.parent is not None:
            self.parent.propagate_info_to_root(weight_to_add)

    def add_child(self, program):
        program.parent = self
        self.children.append(program)
        self.propagate_info_to_root(program.total_weight)

def advent7(data):
    line_list = data.split('\n')
    program_list = []

    for line in line_list:
        values_list = line.split()
        name = values_list[0]
        weight_str = values_list[1][1:-1]
        weight = int(weight_str)
        program_list.append(Program(name, weight))

    for line in line_list:
        values_list = line.split(" -> ")
        if not len(values_list) == 2:
            continue
        name_and_weight = values_list[0].split()
        name = name_and_weight[0]

        children_str_list = values_list[1].split(", ")

        children_list = []
        program = None
        for prog in program_list:
            if prog.name == name:
                program = prog
            if prog.name in children_str_list:
                children_list.append(prog)

        for prog in children_list:
            program.add_child(prog)

    #now find the greatest
    max_children = 0
    max_program = None
    for prog in program_list:
        if prog.total_children > max_children:
            max_children = prog.total_children
            max_program = prog

    #now find the fucking traitor            
    correct = 0
    prog = max_program
    while True:
        num_to_count = {}
        for child in prog.children:
            if child.total_weight not in num_to_count:
                num_to_count[child.total_weight] = 1
            else:
                num_to_count[child.total_weight] += 1

        if len(num_to_count) <= 1:
            break
        
        sort = [(k, num_to_count[k]) for k in sorted(num_to_count, key=num_to_count.get)]
        changed = False
        for child in prog.children:
           if child.total_weight == sort[0][0]:
               prog = child
               correct = child.weight + (sort[1][0] - sort[0][0])
               changed = True
            
            
    print("tast1:{}; task2:{}".format(max_program.name, correct))

# DAY 8 ---------------------------------------------------------------
def advent8(data):
    lines = data.split('\n')
    registers = {}
    highest_ever = None
    for line in lines:
        line = line.split()

        reg = line[0]
        instr = line[1]
        val = line[2]
        cond_reg = line[4]
        cond = line[5]
        cond_val = line[6]

        val = int(val)
        cond_val = int(cond_val)

        cond_fulf = False
        
        if reg not in registers:
            registers[reg] = 0

        if cond_reg not in registers:
            registers[cond_reg] = 0

        if cond == ">":
            if registers[cond_reg] > cond_val:
                cond_fulf = True
        if cond == "<":
            if registers[cond_reg] < cond_val:
                cond_fulf = True
        if cond == ">=":
            if registers[cond_reg] >= cond_val:
                cond_fulf = True
        if cond == "<=":
            if registers[cond_reg] <= cond_val:
                cond_fulf = True
        if cond == "==":
            if registers[cond_reg] == cond_val:
                cond_fulf = True
        if cond == "!=":
            if registers[cond_reg] != cond_val:
                cond_fulf = True

        if cond_fulf:
            if instr == "inc":
                registers[reg] += val
            elif instr == "dec":
                registers[reg] -= val

        if highest_ever is None:
            highest_ever = registers[reg]
        elif highest_ever < registers[reg]:
            highest_ever = registers[reg]

    v = list(registers.values())
    k = list(registers.keys())
    max_register_value = max(v)

    print("tast1:{}; task2:{}".format(max_register_value, highest_ever))


# DAY 9 -----------------------------------------------------------------------


def advent9(data):
    char_list = list(data)
    score = 0
    garbage_score = 0
    is_garbage = False
    ignore_next = False
    nesting = 0

    for char in char_list:
        if is_garbage:
            if ignore_next:
                ignore_next = False
            else:
                if char == '>':
                    is_garbage = False
                elif char == '!':
                    ignore_next = True
                else:
                    garbage_score += 1

        elif char == '<':
            is_garbage = True
        elif char == '{':
            nesting += 1
            score += nesting
        elif char == '}':
            nesting -= 1

    print("tast1:{}; task2:{}".format(score, garbage_score))

# DAY 10 -----------------------------------------------------------------

def reverse_sub(lst, pos, cnt):
    lst2 = lst[:]
    pos2 = (pos+cnt-1)%len(lst)
    for i in range(cnt):
        lst[(pos+i)%len(lst)] = lst2[(pos2-i)%len(lst)]

        
def advent10(data):
    seq = list(map(int, data.split(',')))
    
    lst = list(range(256))
    pos = 0
    skip = 0
    for length in seq:
        if length > len(lst):
            continue
        reverse_sub(lst, pos, length)
        pos = (pos+length+skip)%len(lst)
        skip += 1

    result1 = lst[0]*lst[1]

    #TASK 2---------------------------------------
    seq = list(data.encode('ascii'))
    seq.extend([17,31,73,47,23])
    lst = list(range(256))
    pos = 0
    skip = 0
    for i in range(64):
        for length in seq:
            if length > len(lst):
                continue
            reverse_sub(lst, pos, length)
            pos = (pos+length+skip)%len(lst)
            skip += 1

    dense = []
    hush = ""
    for i in range(16):
        dense_part = 0
        for n in range(16):
            dense_part = dense_part ^ lst[i*16+n]
        dense.append(dense_part)
        hush_add = hex(dense_part)[2:]
        if len(hush_add) < 2:
            hush_add = '0'+hush_add
        hush += hush_add
        

    print("task1:{}; task2:{}".format(result1, hush))

# DAY 11 ---------------------------------------------------------
def advent11(data):
    dir_list = data.split(',')
    position = [0,0,0]  # honeycomb, needs 3 dimensions to easily address them
    max_steps = 0
    for direction in dir_list:
        if direction == "n":
            position[1] += 1
            position[2] += 1
        elif direction == "s":
            position[1] -= 1
            position[2] -= 1
        elif direction == "nw":
            position[0] -= 1
            position[1] += 1
        elif direction == "se":
            position[0] += 1
            position[1] -= 1
        elif direction == "ne":
            position[0] += 1
            position[2] += 1
        elif direction == "sw":
            position[0] -= 1
            position[2] -= 1
        total = abs(position[0]) + abs(position[1]) + abs(position[2])
        steps = total//2
        if steps > max_steps:
            max_steps = steps

    total = abs(position[0]) + abs(position[1]) + abs(position[2])
    steps = total//2
    print("task1:{}; task2:{}".format(steps, max_steps))

# DAY 12 ----------------------------------------------------------
def advent12(data):
    line_list = data.split('\n')
    isets = [{0}]
    root = None
    for line in line_list:
        str_list = line.split()
        left_num = int(str_list[0])
        right_nums = str_list[2:]  # strip
        right_nums = "".join(right_nums)  # get together
        right_nums = list(map(int, right_nums.split(',')))  # remove colons and map to ints

        interconnected = set([left_num] + right_nums)
        found = False
        for i in range(len(isets)):
            if len(interconnected & isets[i]) > 0:
                isets[i] = isets[i] | interconnected
                found = True
        if not found:
            isets.append(interconnected)

        # finally, reduce the list
        for s in isets[1:]:
            if len(s & isets[0]) > 0:
                isets[0] = isets[0] | s
                isets = list(filter((s).__ne__, isets))

    # Ugly ugly ugly, but finally works correctly!!
    i = 1
    while True:
        changed = False
        if i >= len(isets):
            break
        j = 1
        while True:
            n = j+1
            if n == i:
                j += 1
                continue
            if n >= len(isets):
                break
            if len(isets[n] & isets[i]) > 0:
                isets[i] = isets[i] | isets[n]
                isets = isets[:n] + isets[(n+1):]
                if n <= i:
                    i -= 1
            else:
                j += 1
        i += 1
    
    print("task1:{}; task2:{}".format(len(isets[0]), len(isets)))

# DAY 13 ---------------------------------------------------------------
def advent13(data):
    lines = data.split('\n')
    layers = {}
    for line in lines:
        depth_range = line.split(": ")
        depth = int(depth_range[0])
        rang = int(depth_range[1])

        rang_mod = (rang-1)*2
        
        layers[depth] = [rang, rang_mod]

    top_layer = max(layers.keys())
    picosecond = 0
    severity = 0
    for i in range(top_layer+1):
        if i not in layers.keys():
            picosecond += 1
            continue
        position = picosecond%layers[i][1]
        if position == 0:
            severity += i*layers[i][0]
        #print("it{}pos{}pic{}sev{}".format(i, position, picosecond, severity))
        picosecond += 1

    # second task, too lazy, just copy the code and bruteforce it :P
    picosecond_start = 0
    while True:
        picosecond = picosecond_start
        caught = False
        for i in range(top_layer+1):
            if i not in layers.keys():
                picosecond += 1
                continue
            position = picosecond%layers[i][1]
            if position == 0:
                caught = True
                break
            #print("it{}pos{}pic{}sev{}".format(i, position, picosecond, severity))
            picosecond += 1
        if not caught:
            break
        picosecond_start += 1

    print("task1:{}; task2:{}".format(severity, picosecond_start))

# DAY 14 --------------------------------------------------------------------------

        

def main():
    last_solved = 13
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
        elif num == 7:
            advent7(data)
        elif num == 8:
            advent8(data)
        elif num == 9:
            advent9(data)
        elif num == 10:
            advent10(data)
        elif num == 11:
            advent11(data)
        elif num == 12:
            advent12(data)
        elif num == 13:
            advent13(data)

if __name__ == "__main__":
    main()
