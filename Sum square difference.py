#!-_- coding ; utf-8
'''
前十个自然数的平方和是：
12 + 22 + ... + 102 = 385
前十个自然数的和的平方是：
(1 + 2 + ... + 10)2 = 552 = 3025
所以平方和与和的平方的差是3025 − 385 = 2640.
找出前一百个自然数的平方和与和平方的差。
'''
n = (100*(100+1)*(2*100+1))//6
m = 5050**2
print(m-n)

