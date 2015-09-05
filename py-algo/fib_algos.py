#!/usr/bin/env python3
# Copyright (c) James Beedy, 2015

# Analysis of Fib alogos in python

def fib_recursive(n):

    if n <= 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

