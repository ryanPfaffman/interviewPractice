'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
'''


def isHappy(n):
    def getNext(num):
        rtn = 0
        for x in str(num):
            rtn += int(x)**2
            print(rtn)
        return rtn
    hashm = {}

    nxt = getNext(n)
    print(f'nxt: {nxt}')
    if nxt == 1:
        return True
    elif nxt == n:
        return False

    i = 0
    hashm[i] = nxt

    while True:
        nxt = getNext(nxt)
        print(f'nxt: {nxt}')
        i += 1
        if nxt in hashm.values():
            return False
        elif nxt == 1:
            return True
        else:
            hashm[i] = nxt
print(isHappy(102304928304923))
