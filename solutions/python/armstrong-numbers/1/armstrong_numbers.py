import math

def is_armstrong(number):
    strnum = str(number)
    length = len(strnum)
    tot = 0
    for num in strnum:
        tot += math.pow(int(num), length)
    return tot == number