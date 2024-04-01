rejected = 0
parcel = int(input("input total number of parcels in a consignment"))
for i in range(parcel):
    dimension = int(input("enter the dimension of the parcel"))
    if dimension > 80:
        print("your size is too large")
    dimension2 = int(input("enter the dimension 2"))
    if dimension2 > 80:
        print("too large")
    dimension3 = int(input("enter the dimension 3"))
    if dimension3 > 80:
        print("too large")
    weight = float(input("enter the weight"))
    if weight < 1:
        print("too light")
    elif weight > 10:
        print("too heavy")
    Sum = dimension + dimension2 + dimension3
    if Sum > 200:
        print("over the size")
    if Sum <= 200 and dimension <= 80 and dimension2 <= 80 and dimension3 <= 80 and weight >= 1 and weight <= 10:
        print("input successfully")
    else:
        rejected = rejected + 1
print("rejected")

accepted = parcel - rejected
print("number of accepted", accepted, "number of rejected", rejected)