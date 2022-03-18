import math

xf_type = input("Cross frame type? ")
beam_depth = float(input("Beam depth? (use decimal inches) "))
beam_spacing = float(input("Beam spacing? (use decimal feet) "))

# Dimensions in inches unless stated otherwise

'''
The initial idea was to write something that would take the beam depth and 
spacing and select a cross frame, but the selection is too complex to code 
easily.

# This hard-codes values into the loop; for best practice, should put values in 
# a matrix and call them.
if beam_depth <= 3.67:
    if beam_spacing < 13.5:
        diaphragm_type = "G"
    elif beam_spacing < 15.0:
        diaphragm_type = "H"
    else:
        print("Beam spacing not in allowable range")
        input("\nPress any key to close")
        quit()
elif beam_depth <= 5.0:
    if beam_spacing < 15.0:
        diaphragm_type = "J"
    elif beam_spacing < 15.0:
        diaphragm_type = "K"
    else:
        print("Beam spacing not in allowable range")
        input("\nPress any key to close")
        quit())
elif beam_depth <= 9.0:
    if beam_spacing < 15.0:
        diaphragm_type = "L"
    elif beam_spacing < 15.0:
        diaphragm_type = "M"
    else:
        print("Beam spacing not in allowable range")
        input("\nPress any key to close")
        quit()()
else:
    print("Beam depth not in allowable range")
    input("\nPress any key to close")
    quit()
'''

# Member properties (weight in plf, width in inches)
member_weight = {'L3x3x516': 6.10, 'WT4x9': 9.0, 'WT5x11': 11.0, 'no_member': 0}
member_width = {'L3x3x516': 3.0, 'WT4x9': 5.25, 'WT5x11': 5.75, 'no_member': 0}

# Minimum connection plates
plate_thick = 0.375
plate_width = 7.0
density_steel = 490 / 12**3  #convert to pci from pcf

# Cross frame elements
frames = {
    'element_defs': ['vert off top', 'vert off bot', 'horiz off', 'diag type', 'horiz type', 'n horiz'],
    'G': [5.0, 5.0, 2.0, 'L3x3x516', 'no_member', 0],
    'H': [5.0, 6.5, 2.0, 'L3x3x516', 'WT4x9', 1],
    'J': [7.5, 6.5, 2.0, 'WT4x9', 'no_member', 0],
    'K': [7.5, 7.0, 2.0, 'WT4x9', 'WT5x11', 1],
    'L': [7.5, 16.0, 2.0, 'WT4x9', 'WT5x11', 1],
    'M': [13.5, 16.0, 2.0, 'WT5x11', 'WT5x11', 2]
    }

# Calculate member lengths
elements = frames[xf_type]
horz_length = beam_spacing - 2 * elements[2]
vert_length = (beam_depth - elements[0] - elements[1] )/12
diag_length = math.sqrt( horz_length**2 + vert_length**2 )

# Sum weights
diag_weight = diag_length * member_weight[ elements[3] ]
horz_weight = horz_length * member_weight[ elements[4] ]
fill_weight = member_width[ elements[3] ]**2 * plate_thick * density_steel
plate_weight = beam_depth * plate_thick * plate_width * density_steel
total_weight = round( diag_weight * 2 + horz_weight * elements[5] + 2 * plate_weight + fill_weight , 2 )

# Output in pounds
summary = ( "Cross frame type: {}\n"
            "Beam depth: {} inches\n"
            "Beam spacing: {} feet\n"
            "Diagonal length: {} feet\n"
            "Diagonal weight: {} pounds\n"
            "Horizontal weight: {} pounds\n"
            "Connection plate weight: {} pounds\n"
            "Filler plate weight: {} pounds\n\n"
            "Total cross frame weight: {} pounds\n\n"
            "Weights do not include any allowance for hardware or reduction for trimming webs"
            ).format(xf_type, beam_depth, beam_spacing, round(diag_length, 2), round(diag_weight, 2), round(horz_weight, 2), round(plate_weight, 2), round(fill_weight, 2), total_weight)

outfile=open("crossframes.txt","w+")
outfile.writelines([summary])
outfile.close()

# Does not include increase for hardware
print("\n" + str(total_weight) + " lbs" )
input("\nPress any key to close")
