med = input("Enter Y or N for medical reason:")
attend = int(input("Enter # of days the student attended:"))
if med=="Y":
    print("You are allowed to take exam.")
else:
    if attend>75:
        print("You are allowed to take exam.")
    else:
        print("You aren't allowed to take exam.")