value1 = int(input("Enter the first number: "))
value2 = int(input("Enter the second number: "))

operator = input("Choose an operator (+, -, *, /): ")

if operator == "+":
    total = value1 + value2
    print("Your sum is:", total)

elif operator == "-":
    sub = value1 - value2
    print("Your difference is:", sub)

elif operator == "*":
    multi = value1 * value2
    print("Your multiplication is:", multi)

elif operator == "/":
    if value2 != 0:
        div = value1 / value2
        print("Your division is:", div)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")