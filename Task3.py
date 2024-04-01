Weight=float(input("enter the weight of the parcel"))
if Weight>=1 and Weight<= 5:
    price=10
    print("The cost is 10$")
elif Weight>5:
    price=10+(Weight-5)/0.1*0.1
    print("The cost is ",price,"$")
