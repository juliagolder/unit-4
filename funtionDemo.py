#julia golder
#3/9/18
#functionDemo.py - how to write our own functions

def hw():
    print("Hello, world")


def double(thingToDouble):
    print(thingToDouble * 2)

def bigger(a,b):
    if a>b:
        print(a)
    else:
        print(b)

bigger(3,4)
bigger(4,3)
bigger("Smedinghoff","Sam")
bigger(True,False)

print("the max of 3 and 4 is", max(3,4))
print("the max of 3 and 4 is", bigger(3,4))

def slope(x1, y1, x2, y2):
    print((y2-y1)/(x2-x1))

slope(1,1,2,2)

double(12) #test of double funtion
double('w') #test of double iwth string input


hw() #test of funtion
hw() #another test
