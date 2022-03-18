S = float(input("Sight distance in feet? "))
G1 = float(input("First grade in percent? "))
G2 = float(input("Second grade in percent? "))

A = G1 - G2
L1 = A * S**2 / 2158
L2 = 2 * S - 2158 / A
if S < L1:
    L = L1
elif S > L2:
    L = L2
else:
    print("\nError in calculation, check sight distance vs. curve length \n")
    sys.exit()
L = round(L)

print("\nFor a sight distance of " + str(S) + " feet, and entrance and exit grades of " + str(G1) + "% and " + str(G2) + "%, the required vertical crest curve length is " + str(L) + " feet.\n")

input("\nPress enter to close")
