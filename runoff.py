delta = float(input("Maximum relative gradient? (Table 3-15 on page 3-61) "))
w = float(input("Width of traffic lane? "))
n1 = float(input("Number of lanes rotated? "))
ed = float(input("Design superelevation rate? "))

bw = (1 + 0.5 * (n1 - 1)) / n1
Lr = w * n1 * ed / delta * bw
Lr = round(Lr)

print("\nFor " + str(n1) + " lane(s), each " + str(w) + " wide, a design superelevation rate of " + str(ed) + "%, and a maximum relative gradient of " + str(delta) + "%, the runoff is " + str(Lr) + " ft.\n")

enc = 2
Lt = 2 / ed * Lr
Lt = round(Lt)

print("Assuming a " + str(enc) + "% normal cross slope, the tangent runout is " + str(Lt) + " ft.")

input("\nPress enter to close")
