import math

V = float(input("Design speed in mph? (Posted speed by EI C11, 2013) "))
g = float(input("Grade in percent? "))

G = g/100
a = 11.2
t = 2.5

db = V**2 / (30 * ( a / 32.2 + G ))
SSD = 1.47 * V * t + db
SSD = math.ceil(SSD)

print("\nFor a posted speed of " + str(V) + " mph, and a grade of " + str(g) + "%, the Stopping Sight Distance (adjusting braking distance for grade according to Eq. 3-3) is " + str(SSD) + " ft.\n")

input("\nPress enter to close")
