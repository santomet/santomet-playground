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




def main():
    last_solved = 1
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
##        elif num == 2:
##            advent2(data)
##        elif num == 3:
##            advent3(data)
##        elif num == 4:
##            advent4(data)
##        elif num == 5:
##            advent5(data)
##        elif num == 6:
##            advent6(data)
##        elif num == 7:
##            advent7(data)
##        elif num == 8:
##            advent8(data)
##        elif num == 9:
##            advent9(data)
##        elif num == 10:
##            advent10(data)
##        elif num == 11:
##            advent11(data)
##        elif num == 12:
##            advent12(data)
##        elif num == 13:
##            advent13(data)
##        elif num == 14:
##            advent14(data)
##        elif num == 15:
##            advent15(data)
##        elif num == 16:
##            advent16(data)
##        elif num == 17:
##            advent17(data)
##        elif num == 18:
##            advent18(data)
##        elif num == 19:
##            advent19(data)
##        elif num == 20:
##            advent20(data)

if __name__ == "__main__":
    main()
