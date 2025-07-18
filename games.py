import random 

def check(comp, user):
    if comp == user:
     return "none"
    elif (comp == "snake" and user == "water") or (comp == "water" and user == "gun") or (comp == "gun" and user == "snake"):
     return "you lose"
    else:
     return "you win"

items = ["snake", "water", "gun"]
comp = random.choice(items)
user = input("Choice: snake, water, gun\nChoose only between these options: ")


score = check(comp, user)
print("You:", user)
print("Computer:", comp)

if score == "none":
 print("It's a draw")
elif score == "you lose":
    print("You lose")
else:
    print("You win")
         