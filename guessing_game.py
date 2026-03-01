x=34
y=int(input("Guess the number: "))
i=3

while i!=0:
    if y==x:
        print("Correct!!! YOU WON!")
        break
    elif y<x:
        y=int(input(f"Low Guess! You have {i} chance left. Guess Again: "))
        i-=1
        if i==0:
            print("LOST!!!")
    elif y>x:
        y=int(input(f"High Guess! You have {i} chance left. Guess Again: "))
        i-=1
        if i==0:
            print("LOST!!!")

