'''
x = White
o = Black

'''

number = int(input('ป้อนขนาด: '))

for row in range(number):
    for column in range(number):
        if (row + column) % 2 == 0:
            print('x', end = "")
        else:    
            print('o', end = "")
    print(" ")