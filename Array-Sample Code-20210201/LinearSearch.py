'''
Program created by DA of Xclass on XDate
to illustrate linear searching a 1D Array
'''

def linearSearch(name,names):
    for i in range (len(names)):
        if names[i] == name:
            #print ("%s found at positon %i" % (name,i))
            print(name, "is found at position ", i)
            break
    else:
        print (name, "not found")

#main
names = ["Michael", "Keanu", "Ryan", "Swan", "Maggie"]
name = input("Who do you want to find?: ")

linearSearch(name,names)#Call subroutine


