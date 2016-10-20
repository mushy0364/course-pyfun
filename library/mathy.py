#!/usr/bin/env python3

def simpleradi():
    radical = discrim

    persq = [4,9,16,25,36,49,64,81,100,121,144,169,196,225,256,289,324,361,400]

    negative = False

    if radical < 0:
        radical = radical * -1
        negative = True

    for num in persq[::-1]:
        if negative == True:
            if radical in persq:
                simplified = radical ** (1/2)+"i"
            elif radical % num <= 0:
                simplified = (num ** (1/2)+"i√"+(radical/num)
        else:
            if radical in persq:
                simplified = (radical ** (1/2))
            elif radical % num <= 0:
                simplified = (num ** (1/2)+"√"+(radical/num)
    return simplified
