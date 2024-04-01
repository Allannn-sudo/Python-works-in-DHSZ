cost_on_bus = 550
tickets_park = 30
student_name = []
not_paid=0
num_students = int(input("put the number of students participated, within the range 0=<x=<45 "))
if 0 <= num_students <= 45:
    for i in range(num_students):
        name = input("enter the name for students")
        paid = input("if he or she has paid?")
        if paid == "yes":
           print("OK")
        if paid == "no":
           not_paid=not_paid+1
           student_name.append(name)
           print("inserted")
        else:
           print("cannot identified")
    cost = (cost_on_bus + tickets_park * num_students - num_students/10*30)/num_students
    print("The cost for each students is", cost)
    print("Those students have not paid", student_name)
else:
    print("out of the range")
profit = not_paid*cost-cost*num_students
if profit < 0:
    print("the cost is", profit)
if profit > 0:
    print("the profit is", profit)
else:
    print("non profit or lost")
