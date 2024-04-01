class Sorting_algorithms:
    List=[]
    I = int(input("enter the numbers of number"))
    for i in range (I):
        N1 = int(input("Number"))
        List.append(N1)
    def onepass(b):
        int = 0
        new_list = []
        for x in b:
            if x > int:
                int = x
                new_list.insert(0,x)
            else:
                new_list.insert(-1,x)
        print(b)
    onepass(List)

    def _sort_(a):
        a.sort()
        print(a)
    _sort_(List)



