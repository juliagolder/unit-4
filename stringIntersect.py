#julia golder
#4/1/18
#stringUnion.py

def stringIntersect(word1,word2):
    answer = ''
    for ch in word1:
        if ch in word2 and ch not in answer:
            answer = answer + ch
    return(answer)


print(stringIntersect('mississippi', 'pennsylvania'))
