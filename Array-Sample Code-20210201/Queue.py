'''
Program created by DA of Xclass on XDate
to illustrate Linear Queues- 1D Array
'''

def queue(gLevels):
    gLevel = ""
    for i in range(3):
        gLevel = input("Input GLevel students: ")
        gLevels.append(gLevel)
    print("Old GLevels after push: ", gLevels)
    gLevels.popleft()
    print("New GLevels after pop", gLevels)

import collections
gLevels = collections.deque(["Agnes", "Robin", "Stephen"])
queue(gLevels)#Call subroutine

'''
glevels= collections.deque(["Agnes", "Robin", "Stephen"])
stack(scores)#Call subroutine

'''

