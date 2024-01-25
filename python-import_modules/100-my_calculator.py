#!/usr/bin/python3
import sys
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])
if sys.argv[2] == "+":
    print(f"{a} {operator} {b} = {add(a, b)}")
elif sys.argv[2] == '-':
    print(f"{a} {operator} {b} = {sub(a, b)}")
elif sys.argv[2] == '*':
    print(f"{a} {operator} {b} = {mul(a, b)}")
elif sys.argv[2] == '/':
    print(f"{a} {operator} {b} = {div(a, b)}")
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

