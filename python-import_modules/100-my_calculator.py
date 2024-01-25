#!/usr/bin/python3
import sys
if __name__ == '__main__':
    import calculator_1 as calc
if len(sys.argv) != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
a = int(sys.argv[1])
operator = sys.argv[2]
b = int(sys.argv[3])
if sys.argv[2] == "+":
    print(f"{a} {operator} {b} = {calc.add(a, b)}")
elif sys.argv[2] == '-':
    print(f"{a} {operator} {b} = {calc.sub(a, b)}")
elif sys.argv[2] == '*':
    print(f"{a} {operator} {b} = {calc.mul(a, b)}")
elif sys.argv[2] == '/':
    print(f"{a} {operator} {b} = {calc.div(a, b)}")
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

