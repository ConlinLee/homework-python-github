#!-_- coding=utf-8 !-_-

from name_function import GetFormatName

print("Enter 'q' at any time to quit.")
while True:
    first = input('please give me a first name:\n')
    if first == 'q':
        break
    last = input('please give me a last name:\n')
    if last == 'q':
        break
    print(GetFormatName(first, last))
    print('\n')




