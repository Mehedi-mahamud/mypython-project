import random 
a = "you win!"
b = "you lose!"
computer = random.choice([1, -1, 0])
youstr = input("Inter your chose:")
youdict = {"s":1, "w":-1, "g":0}
you = youdict[youstr]
reversdict = {1:"snake", -1:"water", 0:"gun"}
print(f"you chose {reversdict[you]}\ncomputer chose {reversdict[computer]}")

if (computer == you ):
    print("Its a draw")
else:
    if (you == 1 and computer == 0):
     print(b)
    
    elif (you == -1 and computer == 1):
     print(b)
    
    elif (you == 1 and computer == -1):
     print(a)
    
    elif (you == -1 and computer == 0):
     print(a)

    elif (you == 0 and computer == -1):
     print(b)

    elif (you == 0 and computer == 1):
     print(a)
    
    else:
      print("Invalid input")