#!-_-coding;utf-8 !-_-
'''求素数的最佳实现方案'''
'''
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
'''
'''杨辉三角'''
'''
n=int(input())-1
n1=n
k=int(input())-1
k1=k
m1=n-k
if n<k or n < 0 or k < 0:
    print('傻逼，不会数学就别瞎填数字！')
elif k==0 or n==0 or n==k:
    print(1)
else:
    while n > 1:
        n1=n1*(n-1)
        n -= 1
    while k > 1:
        k1=k1*(k-1)
        k -= 1
    m=m1
    while m >1:
        m1=m1*(m-1)
        m -= 1
    print(n1//(m1*k1))
'''
'''矩阵置换'''
