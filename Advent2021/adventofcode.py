import math
from operator import itemgetter
from collections import deque

def advent1(data):
    lines = data.split('\n')
    increasecount = 0
    increasegroupcount = 0
    lm = [None, None, None]
    lastmeasurement = 0
    afterfirst = False
    for l in lines:
        if afterfirst and int(l) > lastmeasurement:
            increasecount += 1
        lastmeasurement = int(l)

        if lm[2]:
            if  (int(l) + lm[0] + lm[1]) > (lm[0] + lm[1] + lm[2]):
                increasegroupcount += 1;
            
        lm[2] = lm[1]
        lm[1] = lm[0]
        lm[0] = int(l)
        
        afterfirst = True

    print("First: {}, second {}".format(increasecount, increasegroupcount))

def advent2(data):
    lines = data.split('\n')

    depth = 0
    length = 0

    aim = 0
    length2 = 0
    depth2 = 0

    for l in lines:
        cv = l.split(' ')
        command = cv[0]
        value = cv[1]
        if command == "forward":
            length += int(value)
            length2 += int(value)
            depth2 += int(value) * aim
        elif command == "down":
            depth += int(value)
            aim += int(value)
        elif command == "up":
            depth -= int(value)
            aim -= int(value)

    print("First: {}, second {}".format(depth*length, depth2 * length2)) 

def advent3_get_rests(lines, position, top):
    totalsize = len(lines)
    onecount = 0
    topval = 0
    
    for l in lines:
        if l[position] == "1":
            onecount += 1

    if onecount > totalsize / 2:
        topval = 1

    if onecount == totalsize / 2:
        topval = 1

    filt = []

    
    for l in lines:
        if int(l[position]) == topval and top:
            filt.append(l)
        elif int(l[position]) != topval and not top:
            filt.append(l)


    return filt
        

def advent3(data):
    lines = data.split('\n')
    totalsize = len(lines)
    bitwidth = len(lines[0])
    onecounts = [0] * bitwidth

    for l in lines:
        for i in range(bitwidth):
            if l[i] == "1":
                onecounts[i] += 1

    finals = ["0"] * bitwidth
    finale = ["1"] * bitwidth
    for i in range(bitwidth):
        if onecounts[i] > totalsize/2:
            finals[i] = "1"
            finale[i] = "0"

    sigma = int("".join(finals), base = 2)
    epsilon = int("".join(finale), base = 2)

    filtertop = lines
    filterleast = lines
    for i in range(bitwidth):
        if(len(filtertop) > 1):
            filtertop = advent3_get_rests(filtertop, i, True)
        if(len(filterleast) > 1):
            filterleast = advent3_get_rests(filterleast, i, False)

    oxygen = int(filtertop[0], base = 2)
    co2 = int(filterleast[0], base = 2)

    print("First: {}, second {}".format(sigma*epsilon, oxygen*co2))

def main():
    last_solved = 3
    txt = """
   __,                            _  _  _  ,
  /  |   _|        _      _|_    / )/ \/ )/|
 |   |  / |  |  |_|/ /|/|  |      /|   |/  |
  \_/\_/\/|_/ \/  |_/ | |_/|_/   /__\_//__ |
                                            
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
            advent1(data)
        elif num == 2:
            advent2(data)
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
