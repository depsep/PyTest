import math

size = float
#should be 25 sq meters.
#31 is close enough, finished!

def main():
    print("Hello world")
    size = float(input("Choose the size of the circle in units. (FROM CENTER) = "))
    print(f" Area of a {size} unit wide circle:")
    print(f"{round(math.pi * size**2)} square units")
    print(f"pi = {math.pi}")

main()