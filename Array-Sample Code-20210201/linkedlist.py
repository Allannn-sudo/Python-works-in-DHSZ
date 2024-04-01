'''
Program created by DA of Xclass on XDate
to illustrate linked list - 1D Array
'''
class node(object):

    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

#create nodes
a = node(1)#object of node class
b = node(2)
c = node(3)

#link the nodes
a.nextNode = b
b.nextNode = c

print(a.data)#outputs 1
print(a.nextNode.data)#outputs 2

print(b.data)#outputs 2
print(b.nextNode.data)#outputs 3

print(c.data)#outputs 3
#print(c.nextNode.data)#outputs error message because c is end of list

print(a.data,b.data,c.data)
'''
class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):#Head node
    def __init__(self, head=None):
        self.head = head


def insert(self, data):#insert node - time complexity - O(1)
    new_node = Node(data)
    new_node.set_next(self.head)
    self.head = new_node


def size(self):#size - time complexity - O(n)
    current = self.head
    count = 0
    while current:
        count += 1
        current = current.get_next()
    return count


def search(self, data):#search - time complexity - O(n)
    current = self.head
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            current = current.get_next()
    if current is None:
        raise ValueError("Data not in list")
    return current


def delete(self, data):#delete - time complexity - O(n)
    current = self.head
    previous = None
    found = False
    while current and found is False:
        if current.get_data() == data:
            found = True
        else:
            previous = current
            current = current.get_next()
    if current is None:
        raise ValueError("Data not in list")
    if previous is None:
        self.head = current.get_next()
    else:
        previous.set_next(current.get_next())
'''
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
'''

