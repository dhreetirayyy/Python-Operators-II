num = int(input("Enter a percentage:"))
if num>=90:
    print("You got an A")
elif num<90 and num>=80:
    print('You got a B')
elif num<80 and num>=70:
    print("You got a C")
elif num<70 and num>=60:
    print("You got a D")
else:
    print("You got a F")