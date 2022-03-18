delta = float(input("Maximum relative gradient? (Table 3-15 on page 3-61) "))
w = float(input("Width of traffic lane? "))
# n1 = float(input("Number of lanes rotated? "))
# need to figure out how adjustment for number of lanes affects math
sh = float(input("Width of shoulder? "))
xs = float(input("Distance between cross sections? "))

# bw = (1 + 0.5 * (n1 - 1)) / n1
dl = round( xs * delta / w , 2 )
ds = round( xs * delta / sh , 2 )

print("\nEvery " + str(xs) + " feet, each " + str(w) + " wide lane can change slope by " + str(dl) + " percent, and each " + str(sh) + " wide shoulder can change by " + str(ds) + " percent.\n")

input("\nPress enter to close")
