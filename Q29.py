t1=0
t2=0
for i in range(3):
    s1=int(input("please enter the score for player1"))
    t1=t1+s1
for i in range(3):
    s2=int(input("please enter the score for player2"))
    t2=t2+s2
if t2>t1:
    print("Player1 scored",t1,"player2 scored",t2,",player2 wins")
else:
    print("player1 scored",t1,"player2 scored",t2,",player1 wins")
