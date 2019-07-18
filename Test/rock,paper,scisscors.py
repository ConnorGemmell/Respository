import random
x = random.randint(1,3)

if x == 1:
    choice = "Rock"
    
if x == 2:
    choice = "Scisscors"

if x == 3:
    choice = "Paper"
    

    
y = input("Pick 1,2, or 3")

if (y == '2') and (choice == "Rock"):
    print("You Lost!")
elif (y == '2') and (choice == "Paper"):
    print("You Win!")
elif (y == '2') and (choice == "Scisscors"):
    print("Tie")
    
if (y == '1') and (choice == "Scisscors"):
    print("You win!")
elif (y == '1') and (choice == "Rock"):
    print("Tie")
elif (y == '1') and (choice == "Paper"):
    print("You Lost")
    
if (y == '3') and (choice == "Rock"):
    print("You Win!")
elif (y == '3') and (choice == "Paper"):
    print("Tie")
elif (y == '3') and (choice == "Scisscors"):
    print("You Lost")
    
    
   