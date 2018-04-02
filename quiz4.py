#julia golder
#4/2/18
#quiz4.py


def count(x):
    for i in range(1,x+1):
        print(i)
    print('BOOM!')


def excitedPrint(word):
    print(word.upper() + '!!!')
    
def firstLetter(word2): 
    letter = ''
    for ch in word2:
        if ch not in letter:
            letter = letter + ch
        return(letter)
        
def repeats(x,y,z):
    if x == y or x == z or y == z:
        return(True)
    else:
        return(False)

count(7)
excitedPrint('I <3 computer programming')
print(firstLetter('Smedinghoff'))
print(repeats(5,6,5))
