import math

# input stage
a = float(input("Enter length of side A: "))
b = float(input("Enter length of side B: "))

# computing stage (to compute for the hypotenuse)
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

# output stage
print(f"The hypotenuse is {c:.2f}.")

