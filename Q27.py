total=0
num=int(input("How many charity raisers were there?"))
for i in range(num):
    raised=int(input("enter the total raised by each"))
    total=total+raised
    print("This will be increased to",total)
