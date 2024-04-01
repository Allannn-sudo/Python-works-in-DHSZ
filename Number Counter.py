count=0
for i in range(80):
   number=int(input("Enter a number between 100 and 1000"))
   while number<= 99 or number>1000:
       print("This is incorrect, please try again")
       number=int(input("Enter a number between 100 and 1000"))
       if number>500:
           count=count+1
       else:
           count=0
           print(count,"numbers were larger than 500")