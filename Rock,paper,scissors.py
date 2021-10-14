import random
chars = "RPS"
def rps(User,computer):
    if User not in chars:
        return "wrong input"
    elif User == computer:
        return "tie"
    return "You won" if (User== "S" and computer== "P") or (User == "P" and computer == "R") or (User == "R" and computer == "S") else "Computer Won"
run = 3
while run:
    run -= 1
    User = input("R for rock ,P for Paper,S for scissors : \nYour Choice: ").upper()
    computer = random.choice(chars)
    print("Computer's choice",computer)
    print(rps(User,computer))
