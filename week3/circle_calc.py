import math

def circle_area(radius):
    return math.pi * radius ** 2

def circle_circumference(radius):
    return 2 * math.pi * radius

r = 5
print(f"Area: {circle_area(r)}")
print(f"Circumference: {circle_circumference(r)}")