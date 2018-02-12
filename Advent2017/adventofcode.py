import math
from operator import itemgetter
from collections import deque

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

# Used also in day 14
def knot_hash(data):
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
    return hush

        
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
        

    print("task1:{}; task2:{}".format(result1, knot_hash(data)))

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
def print_grid(rows):
    for i in range(128):
        for n in range(128):
            if rows[i][n] == 1:
                print(chr(9632), end = '')
            elif rows[i][n] == 0:
                print(chr(9633), end = '')
            elif rows[i][n] == 2:
                print(chr(9652), end = '')
        print()
    print()

def regionify(rows, coord):
    if coord[0] < 0 or coord[0] > 127 or coord[1] < 0 or coord[1] > 127:
        return
    if rows[coord[0]][coord[1]] == 1:
        rows[coord[0]][coord[1]] = 2  # mark as found
        regionify(rows, [coord[0]-1, coord[1]])
        regionify(rows, [coord[0], coord[1]-1])
        regionify(rows, [coord[0]+1, coord[1]])
        regionify(rows, [coord[0], coord[1]+1])

def advent14(data):
    rows = []
    ones = 0
    regions = 0
    for i in range(128):
        hush = knot_hash(data + "-" + str(i))
        integer = int(hush,16)
        binary = list(map(int, bin(integer)[2:]))
        binary = [0]*(128-len(binary)) + binary
        rows.append(binary)
        ones += (binary.count(1))

    # print_grid(rows)  #debug
        
    for i in range(128):
        for n in range(128):
            if rows[i][n] == 1:
                regions += 1
                regionify(rows, [i, n])

    print("task1:{}; task2:{}".format(ones, regions))

# DAY 15 ---------------------------------------------------------
def advent15(data):
    info_lines = data.split('\n')
    gen_A_start = 0
    gen_B_start = 0
    for info in info_lines:
        info = info.split()
        if info[1] == 'A':
            gen_A_start = int(info[4])
        elif info[1] == 'B':
            gen_B_start = int(info[4])

    count = 0
    count_2 = 0
    gena = gen_A_start
    gena_2 = gen_A_start
    genb = gen_B_start
    genb_2 = gen_B_start
    genam = 16807
    genbm = 48271
    mod = 2147483647
    
    cycles = 40000000  # 40 millions :D
    for i in range(cycles):
        gena = (gena*genam)%mod         
        genb = (genb*genbm)%mod
        gena_bin_16 = gena%65536  # cut last 16 bits: 65536 is lowest number with 17b
        genb_bin_16 = genb%65536
        if gena_bin_16 == genb_bin_16:
            count += 1

    # doesn't make sense to have it in the same cycle... python is already too slow for this
    cycles = 5000000
    for i in range(cycles):
        gena_2 = (gena_2*genam)%mod
        while not gena_2%4 == 0:
            gena_2 = (gena_2*genam)%mod

        genb_2 = (genb_2*genbm)%mod
        while not genb_2%8 == 0:
            genb_2 = (genb_2*genbm)%mod

        gena_2_bin_16 = gena_2%65536
        genb_2_bin_16 = genb_2%65536

        if gena_2_bin_16 == genb_2_bin_16:
            count_2 += 1

            
    print("task1:{}; task2:{}".format(count, count_2))

# DAY 16 -----------------------------------------------------------------

def advent16(data):
    programs = []
    letter = 'a'
    for i in range(16):
        programs.append(letter)
        letter = chr(ord(letter) + 1)

    oldprograms = programs[:]
    data = data.split(',')
    i = 1
    while i <= 1000000000:
        for move in data:
            instr = list(move)[0]
            if instr == 's':
                a = int(move[1:])
                programs = programs[(-a):] + programs[:(15-a+1)]          
            elif instr == 'x':
                positions = move[1:].split('/')
                l1_pos = int(positions[0])
                l2_pos = int(positions[1])
                l1 = programs[l1_pos]
                l2 = programs[l2_pos]
                programs[l1_pos] = l2
                programs[l2_pos] = l1
            elif instr == 'p':
                letters = move[1:].split('/')
                l1_pos = programs.index(letters[0])
                l2_pos = programs.index(letters[1])
                l1 = programs[l1_pos]
                l2 = programs[l2_pos]
                programs[l1_pos] = l2
                programs[l2_pos] = l1
        if i == 1:
            firsttask = programs[:]
        if programs == oldprograms:
            i = i*int(1000000000/i)

        i+= 1

    print("task1:{}; task2:{}".format("".join(firsttask), "".join(programs)))

# DAY 17 ------------------------------------------------------

def advent17(data):
    steps = int(data)
    lst = [0]
    pos = 0
    firsttask = 0
    for i in range(1, 2018):
        pos = (pos+steps)%(len(lst)) + 1
        # print("insert {} at pos {}".format(i,pos))
        lst.insert(pos, i)
        if i == 2017:
            firsttask = lst[pos+1]

    lst = [0]
    length = 1
    
    # we don't have to keep the whole list, because zero is always on index 0
    for i in range(1, 50000001):
        pos = (pos+steps)%(length) + 1
        length += 1
        if pos > steps:
            continue
        # print("insert {} at pos {}".format(i,pos))
        lst.insert(pos, i)
            
    
    print("task1:{}; task2:{}".format(firsttask, lst[1]))

# DAY 18 -------------------------------------------------------------
# i hate this one

def duet(lines, registers, pos, task2 = False, sndq = [], rcvq = [], sndcnt = [0], prog = 0):
    last_frequency_played = -1
    while True:
        if pos[0] >= len(lines) or pos[0] < 0:
            return -1
        instr = lines[pos[0]].split()
        first = instr[1]
        second = None
        if len(instr) == 3:
            second = instr[2]
        
        firstisreg = False
        if first >= 'a' and first <= 'z':
            firstisreg = True
            if first not in registers:
                registers[first] = 0
        else:
            first = int(first)

        secondisreg = False
        if second is not None and second >= 'a' and second <= 'z':
            secondisreg = True
            if second not in registers:
                registers[second] = 0
        elif second is not None:
            second = int(second)
        
        jmp = False


        if instr[0] == "snd":
            if firstisreg:
                last_frequency_played = registers[first]
                sndq.append(registers[first])
            else:
                last_frequency_played = first
                sndq.append(first)
            sndcnt[0] += 1

        elif instr[0] == "set":
            if firstisreg:
                if secondisreg:
                    registers[first] = registers[second]
                else:
                    registers[first] = second

            else:
                print("ERROR in SET")    

        elif instr[0] == "add":
            if firstisreg:
                if secondisreg:
                    registers[first] += registers[second]
                else:
                    registers[first] += second
            else:
                print("ERROR in ADD")

        elif instr[0] == "mul":
            if firstisreg:
                if secondisreg:
                    registers[first] *= registers[second]
                else:
                    registers[first] *= second
            else:
                print("ERROR in MUL")
    
        elif instr[0] == "mod":
            if firstisreg:
                if secondisreg:
                    if not registers[second] == 0:
                        registers[first] = registers[first] % registers[second]
                else:
                    if not second == 0:
                        registers[first] = registers[first] % second
            else:
                print("ERROR in MOD")

        elif instr[0] == "rcv":
            if firstisreg:
                if not task2:
                    if not registers[first] == 0:
                        return last_frequency_played
                else:
                    if len(rcvq) > 0:
                        registers[first] = rcvq.popleft()
                    else:
                        return 0
                
            else:
                print("ERROR in RCV")
                if not task2:
                    if not first == 0:
                        return last_frequency_played

        elif instr[0] == "jgz":
            if (firstisreg and registers[first] > 0) or (not firstisreg and first > 0):
                if secondisreg:
                    pos[0] += registers[second]
                else:
                    pos[0] += second
                jmp = True

        if not jmp:
            pos[0] += 1

def advent18(data):
    lines = data.split('\n')

    registers = {}
    firsttask = duet(lines, registers, [0])

    registers0 = {}
    registers1 = {}
    registers1['p'] = 1
    p0q = deque([])
    p1q = deque([])
    pos0 = [0]
    pos1 = [0]
    send0 = [0]
    secondtask = [0]
    
    while True:
        rv0 = duet(lines, registers0, pos0, True, p0q, p1q, send0, 0)
        rv1 = duet(lines, registers1, pos1, True, p1q, p0q, secondtask, 1)
        afterfirstrun = True
        if not rv0 == 0 or not rv1 == 0:
            break
        if len(p1q) < 1 and len(p0q) < 1:
            break

    
    

    print("task1:{}; task2:{}".format(firsttask, secondtask[0]))
                
                    

# DAY 19 -------------------------------------------------------------
# i know i'm not checking if i'm out of index... too lazy
def new_direction(rows, x, y, character):
    if character == '|':  # left or right
        ch = rows[y][x-1]
        if ch == '-' or (ch >= 'A' and ch <= 'Z'):
            return [-1, 0, '-']
        ch = rows[y][x+1]
        if ch == '-' or (ch >= 'A' and ch <= 'Z'):
            return [1, 0, '-']

        return [0,0,'F']

    if character == '-':
        ch = rows[y-1][x]
        if ch == '|' or (ch >= 'A' and ch <= 'Z'):
            return [0, -1, '|']
        ch = rows[y+1][x]
        if ch == '|' or (ch >= 'A' and ch <= 'Z'):
            return [0, 1, '|']
        
        return [0,0,'F']

def advent19(data):
    rows = data.split('\n')
    letters = []
    steps = 1
    for i in range(len(rows)):  # listize
        rows[i] = list(rows[i])
        
    direction = [0, 1, '|']  # x difference, y difference, line
    x = 0
    y = 0
    # find the starting point
    for i in range(len(rows[0])):
        if rows[0][i] == '|':
            x = i
            break

    while True:  # these could be shorter, but i would check some things two times in that case
        # one step
        let = rows[y+direction[1]][x+direction[0]]
        if let >= 'A' and let <= 'Z':
            letters.append(let)
            x += direction[0]
            y += direction[1]
            steps += 1
            continue
    
        if let == direction[2]:
            x += direction[0]
            y += direction[1]
            steps += 1
            continue
        if let == '+':
            x += direction[0]
            y += direction[1]
            steps += 1
            direction = new_direction(rows, x, y, direction[2])
            if direction[2] == 'F':
                break
            continue
        # two steps
        let = rows[y+2*direction[1]][x+2*direction[0]]
        if let >= 'A' and let <= 'Z':
            letters.append(let)
            x += 2*direction[0]
            y += 2*direction[1]
            steps += 2
            continue

        if let == direction[2]:    
            x += 2*direction[0]
            y += 2*direction[1]
            steps += 2
            continue
        if let == '+':
            x += 2*direction[0]
            y += 2*direction[1]
            steps += 2
            direction = new_direction(rows, x, y, direction[2])
            if direction[2] == 'F':
                break
            continue

        break

    
    print("task1:{}; task2:{}".format("".join(letters), steps))

# DAY 20 -----------------------------------------------------------------------------

def advent20(data):
    particles_str = data.split('\n')
    particles = []
    count = 0

    for particle_str in particles_str:
        pva = particle_str.split(", ")
        particle = []
        for val in pva:
            particle.append(list(map(int, val[3:-1].split(','))))

        particle[0].append(True)  # indication that particle is still alive
        particles.append(particle)
        count += 1



    collparticles = particles[:]

    for i in range(1000):
        for particle in particles:
            for i in range(3):
                particle[1][i] += particle[2][i]
                particle[0][i] += particle[1][i]

    mindist = None
    minpart = None
    for i in range(len(particles)):
        dist = abs(particles[i][0][0]) + abs(particles[i][0][1]) + abs(particles[i][0][2])
        if mindist is None:
            mindist = dist
            minpart = i
        else:
            if mindist > dist:
                mindist = dist
                minpart = i


    positions = {}
    for i in range(1000):
        for particle in collparticles:

            if not particle[0][3]:  # if collided
                continue
            
            for i in range(3):
                particle[1][i] += particle[2][i]
                particle[0][i] += particle[1][i]

            if (particle[0][0], particle[0][1], particle[0][2]) in positions.keys():  # particles on particular positions
                positions[(particle[0][0], particle[0][1], particle[0][2])].append(particle)
            else:
                positions[(particle[0][0], particle[0][1], particle[0][2])] = [particle]

        for key in positions.keys():  # search for collisions
            parlist = positions[key]
            if len(parlist) > 1:
                for particle in parlist:
                    particle[0][3] = False
                    count -= 1
                    parlist.remove(particle)
        
            

    print("task1:{}; task2:{}".format(minpart, count))

def main():
    last_solved = 20
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
        elif num == 14:
            advent14(data)
        elif num == 15:
            advent15(data)
        elif num == 16:
            advent16(data)
        elif num == 17:
            advent17(data)
        elif num == 18:
            advent18(data)
        elif num == 19:
            advent19(data)
        elif num == 20:
            advent20(data)

if __name__ == "__main__":
    main()
