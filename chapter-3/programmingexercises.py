import math

# calculating the volume and surface area of a sphere
def main():
    r = int(input("Enter a radius: "))
    V = (4 / 3) * math.pi * pow(r, 3)
    A = 4 * math.pi * pow(r, 2)
    print(f"The volume of the sphere is {V} and the surface area is {A}")
main()

# Calculating the cost per square
def main():
    p = int(input("Enter the price of the pizza: "))
    d = int(input("Enter the diameter of the pizza: "))
    r = d / 2
    A = math.pi * pow(r, 2)
    P = A / p
    print(f"The cost per square is {P}")
main()

#Calculate the molecular weight based on the number of hydrogen, carbon and oxygen
def main():
    h = int(input("Enter the number of hydrogen: "))
    c = int(input("Enter the number of carbon: "))
    o = int(input("Enter the number of oxygen: "))
    M = (h * 1.00794) + (c * 12.0107) + (o * 15.9994)
    print(f"The molecular weight is {M}")
main()

#calculate the distance struck by a lightening
def main():
    t = int(input("Enter the time between the flash and the sound: "))
    d = 1100 * t
    m = d / 5280
    print(f"The distance in ft is {d} ft")
    print(f"The distance in mile/s is {m}mile")
main()

# calculate cost of a coffee shop that sells coffee at $10.50 a pound plus the cost
# of shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for
# overhead.
def main():
    coffee = 10.50
    shipping = 0.86
    fixed_cost = 1.50
    c = int(input("How many will you buy: "))
    p = coffee * c
    s = (shipping * c)
    total = p + s + fixed_cost
    print(f"The cost of coffee: ${p}")
    print(f"The shipping cost: ${s}")
    print(f"The total cost is ${total}")
main()

#calculate two points in a plane are specified using the coordinates (x1,y1) and
#(x2,y2).
def main():
    x1 = int(input("Enter the first coordinate for x1: "))
    x2 = int(input("Enter the second coordinate for x2: "))
    y1 = int(input("Enter the first coordinate for y1: "))
    y2 = int(input("Enter the second coordinate for y2: "))
    m = ((y2**2) - (y1**2)) / ((x2**2) - (x1**2))
    print(f"The slope of the line is {m}")
main()

# a program that accepts two points and determines the distance between them.
def main():
    x1 = int(input("Enter the first point for x1: "))
    x2 = int(input("Enter the second point for x2: "))
    y1 = int(input("Enter the first point for y1: "))
    y2 = int(input("Enter the second point for y2: "))
    distance = math.sqrt((pow(x2, 2) - pow(x1, 2))**2 + (pow(y2, 2) - pow(y1, 2))**2)
    print(f"The distance between the two points are {distance}")
main()

#The Gregorian epact is the number of days between January 1st
#and the previous new moon. This value is used to figure out the date of Easter.
def main():
    year = int(input("Enter a four digit year: "))
    C = year // 100
    epact = (8 + (C // 4) - C + (( 8*C + 13) // 25) + 11 *(year % 19))%30
    print(f"Next Easter falls on {epact}")
main()

#calculate the area of a triangle given the length of its three sides:a, b, and c
def main():
    a = int(input("Enter the first side: "))
    b = int(input("Enter the second side: "))
    c = int(input("Enter the third side: "))
    s = (a + b + c) / 2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"The area of the triangle is {A}")
main()

#to determine the length of a ladder required to reach a given height
#when leaned against a house. The height and angle of the ladder are given as inputs
def main():
    height = int(input("Enter the height: "))
    angle = int(input("Enter the angle in degrees: "))
    radians = math.pi / 180
    length = height / math.sin(angle)
    print(f"The angle in radians is {radians}")
    print(f"The length of the ladder is {length}")
main()

#to find the sum of the first n natural numbers
def main():
    n = int(input("Enter a natural number: "))
    total = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is : {total}")
main()

#to find the sum of the cubes of the first n natural numbers
def main():
    n = int(input("Enter a natural number: "))
    total = (n * (n + 1) // 2) ** 2
    print(f"The sum of the cubes of the first  {n} natural numbers is : {total}")
main()

# a program to sum a series of numbers entered by the user.
def main():
    prompt = int(input("How many numbers are to be summed: "))
    total = 0
    for i in range(1, prompt + 1):
        number = float(input(f"Enter number {i}: "))
        total += number
        print(f"The total sum of the entered numbers is {total}")
main()

#a program that finds the average of a series of numbers
def main():
    prompt = int(input("How many numbers are to be averaged: "))
    total = 0
    for i in range(1, prompt + 1):
        number = float(input(f"Enter number {i}: "))
        total += number
        average = total / prompt
        print(f"The average of the entered numbers is {average}")
main()

#a program that approximates the value of pi by summing the terms
#of this series: 4/1- 4/3 + 4/5- 4/7 + ...
def main():
    n = int(input("Enter the number of terms: "))
    total = 0
    for i in range(n):
        term = 4 / (2 * i + 1)
        if i % 2 == 0:
            total += term
        else:
            total -= term
            difference = math.pi - total
            print(f"Approximated value of pi after {n} terms : {total}")
            print(f"Actual value of pi: {math.pi}")
            print(f"Difference: {difference}")
main()

#A Fibonacci sequence is a sequence of numbers where each successive number is the sum
# of the previous two.e a program that computes the nth Fibonacci number
def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    a, b = 1, 1

    for _ in range(3, n + 1):
        a, b = b, a + b

    return b


n = int(input("Enter the value of n: "))

print(f"The {n}th number in the Fibonacci sequence is {fibonacci(n)}")













