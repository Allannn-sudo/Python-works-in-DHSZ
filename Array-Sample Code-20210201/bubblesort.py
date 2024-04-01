'''
Program created by DA of Xclass on XDate
to illustrate bubble-sorting-descending/descendig
'''
import timeit


#ascending order
def sortList():#Procedure using one parameter in, one out
    for p in range(4,0,-1):#Outter loops has n-1(0 to 4) comparisons (4)
        for i in range(p):#begins first pass
            if scores[i] > scores[i+1]:
                scores[i], scores[i+1] = scores[i+1], scores[i]
    print("Sort list is: ",scores) #sorted List

   
#main
scores = [50,20,90,10,60]
sortList(scores)#Call subroutine


'''
def total(b,c):
    a=0
    a = b + c
    print(a)

total(10,20)
'''
'''
scores = [50,20,90,10,60]

scores.sort()
print("Sort list is: ",scores)

scores = [50,20,90,10,60]

print(sorted(scores))

print(sorted([50, 20, 90, 10, 60]))
'''



'''
#ascending order
def sortList(scores):#Procedure using one parameter in, one out
    #print("Original list is: ", scores)#original List
    for p in range(len(scores)-1,0,-1):#Outter loops has n-1(0 to 4) comparisons (4)
        for i in range(p):#begins first pass
            #print(p,i)#Just for viewing loop operating
            
            if scores[i] > scores[i+1]:
                scores[i], scores[i+1] = scores[i+1], scores[i]
            #print(scores)#output after each comparison
    print("Sort list is: ",scores) #sorted List

#main
scores = [50,20,90,10,60]
sortList(scores)#Call subroutine
'''

'''
scores = [50,20,90,10,30,40,20,60]
#print(scores)#original list

scores.sort()#sorted list
print(scores)#sorted list
'''
'''
#two lines of code
scores = [50,20,90,10,30,40,20,60]
print(sorted(scores))

#1 line of code
#print(sorted([50,20,90,10,30,40,20,60]))
'''

'''
#descending order
def sortList(scores):#Procedure using one parameter in, one out
    print("Original list is: ", scores)#original List
    for p in range(len(scores)-1,0,-1):#Outter loops has n-1(0 to 4) comparisons (4)
        for i in range(p):#begins first pass
            #print(p,i)#Just for viewing loop operating
            
            if scores[i] < scores[i+1]:
                scores[i], scores[i+1] = scores[i+1], scores[i]
            #print(scores)#output after each comparison
    print("Sort list is: ",scores) #sorted List

#main
scores = [50,20,90,10,60]
sortList(scores)#Call subroutine
'''
'''
#Descending order
scores = [50,20,90,10,30,40,20,60]
print(scores)#original list
'''
'''
#Descending order
scores = [50,20,90,10,60]

scores.sort(reverse=True)
print (scores)

scores = [50,20,90,10,60]

print(sorted(scores,reverse = True))



print(sorted([50,20,90,10,60],reverse = True))
'''

