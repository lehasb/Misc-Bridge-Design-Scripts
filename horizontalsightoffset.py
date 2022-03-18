import math

S = float(input("Sight distance (feet)? "))
R = float(input("Radius of curve (feet)? "))

HSO = R * ( 1 - math.cos( math.radians(28.65 * S / R) ) )
HSO = math.ceil(HSO)

print("\nFor a sight distance of " + str(S) + " feet, and a horizontal curve radius of " + str(R) + " feet, the horizontal sight line offset is " + str(HSO) + " feet.\n")

input("\nPress enter to close")
