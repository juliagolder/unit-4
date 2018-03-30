#julia golder
#3/29/18
#printSquares.py


def square(c,r):
    for i in range(0,c):
        print('+ - - ' *r, '+')
        print('|     ' *r, '|')
    print('+ - - ' *r, '+')


square(5,8)