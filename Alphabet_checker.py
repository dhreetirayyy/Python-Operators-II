char = input("Enter a character:")

if char.isalpha() and len(char) == 1:
    print(f"'{char}' is an alphabet.")
else:
    print(f"'{char}' is not an alphabet.")