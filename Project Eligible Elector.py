
while True:
    voter_age = int(input("How old are you: "))
    if voter_age > 0:
        break 


if voter_age > 18: 
    print("Congratulations! You are eligible to vote. Go make a difference!")
elif voter_age < 18: 
    print("Oops! You’re not eligible yet. But hey, only", 18-voter_age, "more years to go!")