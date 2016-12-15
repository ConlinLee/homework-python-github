#!-_-coding;utf-8 !-_-

from time import clock
def SuShu(num):
    ss=[2]
    for x in range(3,num,2):
        for y in ss:
            if x % y == 0:
                break
            elif y > int(num**0.5):
                ss.append(x)
        else:
            ss.append(x)
    return ss
c = clock()
print(SuShu(1000000))
print(len(SuShu(1000000)))
print(clock() -c)