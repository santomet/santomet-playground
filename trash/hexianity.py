# My university stores EM card number in opposite endianity as all
# of my readers. Couldn't find good easy-to-use online tool...
# conversion between big and little endian hex numbers
#  18 <==> 81 (0001 1000 <==> 1000 0001)
import sys

def hexianity(num):
    res = []
    num = list(num)
    for ch in num:
        b = bin(int(ch,16))[2:]
        while len(b) < 4:
            b = "0"+b
        b = b[::-1]
        newch = hex(int(b,2))[2:]
        res.append(newch)
    print("".join(res).upper())


hexianity(sys.argv[1])
