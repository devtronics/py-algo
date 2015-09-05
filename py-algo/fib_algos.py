#!/usr/bin/env python3
# Copyright (c) James Beedy, 2015
# Copyright (c) Chris Heckler, 2015

# Analysis of Fib alogos in python

def fib_recursive(n):

    if n <= 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

if __name__ == "__main__":
    # Get fib_num input from user
    fib_num = int(raw_input("Enter a number between 1 and 30"))
    print(fib_recursive(fib_num))

