def check_age(age):
    if age >= 18:
        return "You are an adult."
    else:
        return "You are a youngling."

# Example usage
age = int(input("Enter your age: "))
result = check_age(age)
print(result)