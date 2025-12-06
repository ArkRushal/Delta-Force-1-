#!/usr/bin/env python3
def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

Y = "Y"

if __name__ == "__main__":
    while Y == "Y":

        print ("Enter two numbers separated by space: ")
        input_numbers = ("Enter two numbers separated by space: ")
        input_numbers = input().split()
        a = float(input_numbers[0])
        b = float(input_numbers[1])

        print(f"a + b = {add(a, b)}")
        print(f"a - b = {subtract(a, b)}")
        print(f"a * b = {multiply(a, b)}")
        print(f"a / b = {divide(a, b)}")


        Y = input("Do you want to continue? (Y/N): ").upper()