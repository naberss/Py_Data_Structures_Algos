import math
from getpass import _raw_input


class pow():

    def __init__(self):
        self.x = 0
        self.y = 0

    def power(self, x, y):
        return math.pow(x, y)


x = float(_raw_input("input x value: "))
y = float(input("input y value: "))

myPow = pow()
print(myPow.power(x, y))
