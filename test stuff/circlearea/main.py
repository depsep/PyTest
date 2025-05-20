import math

size = float
#should be 25 squared units for 5 width.
#31 is close enough, epic!

def main():
    print("Hello world")
    size = float(input("Choose the size of the circle in units. (FROM CENTER) = "))
    print(f" Area of a {size} unit wide circle:")
    print(f"{round(math.pi * (size*size))} square units")
    print(f"{math.pi * size**2} sq. units UNROUNDED")
    print(f"pi = {math.pi}")

main()