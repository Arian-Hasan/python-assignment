name, age = input("Enter your name: "), input("Enter your age: ")
n1, n2 = int(input("Enter first number: ")), int(input("Enter second number: "))

print(f"""
Hello, {name}!
Your age is {age}.
Addition: {n1 + n2}
Subtraction: {n1 - n2}
Multiplication: {n1 * n2}
Division: {n1 / n2 if n2 != 0 else 'Undefined (Cannot divide by zero)'}""")