total=0
count=0
while count<=7:
    tem=int(input("enter the seven temperature"))
    total=total+tem
    count=count+1
    avg=total/7
    print("This week's average was",avg,"degrees centigrade")