print("Welcome to the calculator program")

no1 = float(input("What is the first number? "))
operation = input("What operation would you like to perform? Input '+', '-', '*', or '/': ")
while operation != '+' and operation != '-' and operation != '*' and operation != '!':
    operation = input("What operation would you like to perform? Input '+', '-', '*', or '/': ")
no2 = float(input("What is the second number? "))

def add(no1, no2):
    solution = (no1 + no2)
    print(solution)

def subtract(no1, no2):
    solution = (no1 - no2)
    print(solution)

def multiply(no1, no2):
    solution = (no1 * no2)
    print(solution)

def divide(no1, no2):
    solution = (no1 / no2)
    print(solution)

if operation == '+':
    add(no1, no2)
elif operation == '-':
    subtract(no1, no2)
elif operation == '*':
    multiply(no1, no2)
elif operation == '/':
    divide(no1, no2)