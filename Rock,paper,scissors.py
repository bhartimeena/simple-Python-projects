import random
chars = "RPS"
def rps(User,computer):
    if  User== "R" and computer== "P":
        return "computer won!!"
    elif User == "P" and computer == "R":
        return "You won!!"
    elif User == "P" and computer == "S":
        return "computer won!!"
    elif User == "S" and computer == "P":
        return "You won!!"
    elif User == "R" and computer == "S":
        return "You won!!"
    elif User == "S" and computer == "P":
        return "computer won!!"
    elif User not in chars:
        return "wrong input"
    elif User == computer:
        return "tie"
run = True
while run:
    User = input("R for rock ,P for Paper,S for scissors : \n")
    computer = random.choice(chars)
    print(rps(User,computer))
