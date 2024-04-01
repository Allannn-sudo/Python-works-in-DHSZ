'''
Program created by DA of Xclass on XDate
to illustrate Stacks- 1D Array
'''

def stack(scores):
    score = 0#integer
    for i in range(3):
        score = int(input("Input score: "))
        scores.append(score)#adding items unto stack
    print("Old scores after push: ", scores)
    scores.pop()#removes item
    print("New scores after pop", scores)
   
#main
scores = [60, 70, 80]
stack(scores)#Call subroutine

#empty - len(array) == true
#top/peek - print(array[-1])
#full - research

'''
Maximum length of a list is platform dependent
and depends upon address space and/or RAM.
The maxsize constant defined in sys module
returns 263-1 on 64 bit system.
>>> import sys
>>> sys.maxsize
9223372036854775807
'''




