import math

V = float(input("Design speed in mph? (Posted speed by EI C11, 2013) "))
g1 = float(input("Start grade in percent? "))
g2 = float(input("End grade in percent? "))

A = g2 - g1

L = ( A * V**2 )/46.5
L = math.ceil(L)

print("\nFor a posted speed of " + str(V) + " mph, a starting grade of " + str(g1) + "%, and an ending grade of " + str(g2) + "%, the length of curve to meet the passenger comfort criteria is " + str(L) + " ft.\n")

input("\nPress enter to close")
