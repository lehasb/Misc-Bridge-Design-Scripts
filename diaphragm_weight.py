import math

dia_type = input("Diaphragm type? ")
beam_depth = float(input("Beam depth? (use decimal inches) "))
beam_spacing = float(input("Beam spacing? (use decimal feet) "))

# Dimensions in inches unless stated otherwise

# Member properties (weight in plf, width in inches)
member_weight = {'W21x44': 44.0, 'W24x55': 55.0, 'W16x26': 26.0, 'L3x3x516': 6.10, 'WT5x11': 11.0, 'no_member': 0}
member_width = {'W21x44': 21.0, 'W24x55': 24.0, 'W16x26': 16.0, 'L3x3x516': 3.0, 'WT5x11': 5.75, 'no_member': 0}

# Minimum connection plates
plate_thick = 0.375
plate_width = 7.0
density_steel = 490 / 12**3  #convert to pci from pcf

# Cross frame elements
frames = {
    'element_defs': ['vert off top', 'vert off bot', 'horiz off', 'diag type', 'main type', 'strut type'],
    'B': [4.0, 0.0, 2.0, 'no_member', 'W24x55', 'no_member'],
    'C1': [4.0, 6.5, 2.0, 'no_member', 'W21x44', 'WT5x11'],
    'C2': [4.0, 6.5, 2.0, 'no_member', 'W24x55', 'WT5x11'],
    'D': [4.0, 10.0, 2.0, 'L3x3x516', 'W16x26', 'WT5x11'],
    }

# Calculate member lengths
elements = frames[dia_type]
horz_length = beam_spacing - 2 * elements[2]
vert_length = ( beam_depth - elements[0] - elements[1] - (member_width[ elements[4] ]/2) )/12
diag_length = math.sqrt( (horz_length/2)**2 + vert_length**2 )

# Sum weights
diag_weight = diag_length * member_weight[ elements[3] ]
horz_weight = horz_length * ( member_weight[ elements[4] ] + member_weight[ elements[5] ] )
guss_weight = member_width[ elements[3] ]*3 * 10.0 * plate_thick * density_steel
plate_weight = beam_depth * plate_thick * plate_width * density_steel
total_weight = round( diag_weight * 2 + horz_weight + 2 * plate_weight + guss_weight , 2 )

# Output in pounds
summary = ( "Cross frame type: {}\n"
            "Beam depth: {} inches\n"
            "Beam spacing: {} feet\n"
            "Diagonal length: {} feet\n"
            "Diagonal weight: {} pounds\n"
            "Horizontal weight: {} pounds\n"
            "Connection plate weight: {} pounds\n"
            "Gusset plate weight: {} pounds\n\n"
            "Total cross frame weight: {} pounds\n\n"
            "Weights do not include any allowance for hardware or reduction for trimming webs"
            ).format(dia_type, beam_depth, beam_spacing, round(diag_length, 2), round(diag_weight, 2), round(horz_weight, 2), round(plate_weight, 2), round(guss_weight, 2), total_weight)

outfile=open("diaphragms.txt","w+")
outfile.writelines([summary])
outfile.close()

# Does not include increase for hardware
print("\n" + str(total_weight) + " lbs" )
input("\nPress any key to close")
