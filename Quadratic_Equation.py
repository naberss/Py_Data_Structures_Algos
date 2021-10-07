import cmath
import math


def quadEquation(a, b, c):
    r = ((b ** 2) - 4 * a * c)

    if r < 0:
        print(" this equation has no real solution")
    elif r == 0:
        x = (-b + math.sqrt(r) / (2 * a))
        print("this equation has one solution: a%" % (x))
    else:
        x = (-b + cmath.sqrt(r)) / (2 * a)
        x2 = (-b - cmath.sqrt(r)) / (2 * a)
        print("this equation has two solutions: %a e %a" % (x, x2))


A = input("input A variable: ")
B = input("input B variable: ")
C = input("input C variable: ")


quadEquation(A, B, C)
