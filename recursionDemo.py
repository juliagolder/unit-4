#julia golder
#3/29/18
#recursionDemo.py - recursive version of countdown

def countdownr(n):
    if n == 0: #base case
        print('BOOM!')
    else: #recursive step
        print(n)
        countdownr(n-1)

countdownr(5)
countdownr(15)