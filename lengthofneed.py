La = float(input("La (ft):  "))
L2 = float(input("L2 (ft):  "))
Lr = float(input("Lr (ft, from Table 5-10(b)):  "))

X = ( La - L2 ) / ( La / Lr )
Y = La - La / Lr * X

print("\nFor a Lateral Extent of the Area of Concern of " + str(La) + ", distance from edge of travelway to barrier of " + str(L2) + " and a recommended runout (Table 5-10(b)) of " + str(Lr) + ", the length of need is " + str(X) + " ft and the lateral offset is " + str(Y) + " ft.\n")

input("\nPress enter to close")
