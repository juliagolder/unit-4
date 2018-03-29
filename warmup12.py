#julia golder
#3/29/18
#warmup12.py


def GCF(num1,num2):
    i = num1
    while i >= 1:
        if num1%i == 0 and num2%i == 0:
            return i
        i-=1
        
print(GCF(12,15))
print(GCF(5,9))
print(GCF(16,64))
