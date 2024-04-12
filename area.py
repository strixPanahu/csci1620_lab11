"""
    CSCI 1620 001/851
    Professor Owora
    Week 12 - Lab 11
    11/4/2024

    https://github.com/strixPanahu/csci1620_lab11
"""


from math import pi


def circle(radius):
    radius = float(radius)
    if radius <= 0:
        raise TypeError
    else:
        return (radius ** 2) * pi


def square(length):
    length = float(length)
    if length <= 0:
        raise TypeError
    else:
        return length * length


def rectangle(length, width):
    length = float(length)
    width = float(width)
    if length <= 0 or width <= 0:
        raise TypeError
    else:
        return length * width


def triangle(a, b):
    a = float(a)
    b = float(b)
    if a <= 0 or b <= 0:
        raise TypeError
    else:
        return (a * b) / 2
