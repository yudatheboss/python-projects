# Python calculator

operator = input("Enter an operator (+ - * / ) ")
if operator not in ("+", "-", "*", "/"):
    print("Invalid operator.")
    exit()
else:
    pass

num1 = float(input("Enter the 1st number. "))
num2 = float(input("Enter the 2nd number. "))

if operator == "+":
    result = num1 + num2
    print(round(result, 3))
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1/num2
    print(round(result, 3))
else:
    print("Invalid operator.")