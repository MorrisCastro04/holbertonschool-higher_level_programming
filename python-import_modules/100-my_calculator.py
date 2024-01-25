#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys

if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])

if sys.argv[2] == "+":
    result = a + b
    print(f"{a} {operator} {b} = {result}")
elif sys.argv[2] == '-':
    result = a - b
    print(f"{a} {operator} {b} = {result}")
elif sys.argv[2] == '*':
    result = a * b
    print(f"{a} {operator} {b} = {result}")
elif sys.argv[2] == '/':
    result = a / b
    print(f"{a} {operator} {b} = {result}")
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
