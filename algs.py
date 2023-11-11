
# Copyright 2023 Dmitriy Stepanov stepanovd@iscrasec.ru
# My implementation of mathematical algorithms

# Extended Euclidean algorithm: a > b, ax + by = 1
# out: gcd, x, y
def ext_gcd(a, b):
    transposition = False
    if a < b:
        a, b = b, a
        transposition = True
    x_prev, x = 1, 0
    y_prev, y = 0, 1
    while (b != 0):
        q = a // b
        b, a = a % b, b
        x, x_prev = x_prev - q * x, x
        y, y_prev = y_prev - q * y, y
    if transposition:
        x_prev, y_prev = y_prev, x_prev
    return a, x_prev, y_prev

