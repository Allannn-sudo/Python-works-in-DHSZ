x=int(input("please input the number"))
if x==78:
    print("you guess right")
while x!=78:
    if x>78:
        print("you guess too high")
        x=int(input("number"))
    if x<78:
        print("you guess too low")
        x=int(input("number"))
    else:
        print("not avilable")
        x=int(input("number"))