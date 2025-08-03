def is_armstrong(number):
    strnum = str(number)
    length = len(strnum)
    tot = 0
    for num in strnum:
        tot += int(num)**length
    return tot == number