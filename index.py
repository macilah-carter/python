num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
mathematical_operation = input("Enter mathematical operation: ")
if mathematical_operation == "+":
    print(f"{num1} {mathematical_operation} {num2} =",int(num1) + int(num2))
elif mathematical_operation == "-": 
    print(f"{num1} {mathematical_operation} {num2} =", int(num1) - int(num2))
elif mathematical_operation == "*":
    print(f"{num1} {mathematical_operation} {num2} =", int(num1) * int(num2))
elif mathematical_operation == "/":
    print(f"{num1} {mathematical_operation} {num2} =", int(num1) / int(num2))
else:
    print("Invalid operation")
