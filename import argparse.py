import argparse
import sys
from functools import reduce
import operator

#!/usr/bin/env python3
"""
calculator.py

Simple CLI calculator for basic arithmetic.
Usage examples:
    python calculator.py add 1 2 3
    python calculator.py sub 10 4 3
    python calculator.py mul 2 3 4
    python calculator.py div 20 2 2
    python calculator.py pow 2 8
    python calculator.py mod 10 3
If run without arguments, enters an interactive prompt.
"""


def add(nums):
        return sum(nums)

def sub(nums):
        # left-associative subtraction: a - b - c ...
        return nums[0] - sum(nums[1:]) if len(nums) >= 1 else 0.0

def mul(nums):
        return reduce(operator.mul, nums, 1.0)

def div(nums):
        if len(nums) < 2:
                raise ValueError("div requires at least two numbers")
        result = nums[0]
        for n in nums[1:]:
                if n == 0:
                        raise ZeroDivisionError("division by zero")
                result /= n
        return result

def power(nums):
        if len(nums) != 2:
                raise ValueError("pow requires exactly two numbers: base exponent")
        return nums[0] ** nums[1]

def mod(nums):
        if len(nums) != 2:
                raise ValueError("mod requires exactly two integers")
        return nums[0] % nums[1]

OPS = {
        "add": add,
        "sub": sub,
        "mul": mul,
        "div": div,
        "pow": power,
        "mod": mod,
}
def parse_args():
        p = argparse.ArgumentParser(description="Basic arithmetic calculator")
        p.add_argument("op", nargs="?", choices=OPS.keys(),
                                     help="operation: " + ", ".join(OPS.keys()))
        p.add_argument("nums", nargs="*", help="numbers (space separated)")
        return p.parse_args()

def to_number(s):
        try:
                if "." in s:
                        return float(s)
                return int(s)
        except ValueError:
                return float(s)  # last resort, may raise

def run_operation(op_name, str_nums):
        nums = [to_number(s) for s in str_nums]
        func = OPS[op_name]
        return func(nums)

def interactive():
        print("Simple calculator. Enter commands like: add 1 2 3")
        print("Available ops:", ", ".join(OPS.keys()))
        try:
                while True:
                        line = input("> ").strip()
                        if not line:
                                continue
                        if line.lower() in ("exit", "quit"):
                                break
                        parts = line.split()
                        op = parts[0]
                        if op not in OPS:
                                print("Unknown op:", op)
                                continue
                        try:
                                result = run_operation(op, parts[1:])
                                print(result)
                        except Exception as e:
                                print("Error:", e)
        except (EOFError, KeyboardInterrupt):
                print()

def main():
        args = parse_args()
        if not args.op:
                interactive()
                return
        try:
                if not args.nums:
                        print("No numbers provided.")
                        sys.exit(2)
                result = run_operation(args.op, args.nums)
                print(result)
        except Exception as e:
                print("Error:", e)
                sys.exit(1)

if __name__ == "__main__":
        main()