import time

# WARNING: Wheel load positions defined manually later in this file

win = '018915.00'
project = 'Brewer-Eddington, Eaton Brook Bridge'
engineer = 'J. Hasbrouck'
date = time.strftime('%Y-%m-%d')

fprimec = '4'
tdeck = '8'

overhang = [3, 4]                   # [feet inches]
beam_spacing = [9, 2]
n_beams = 5

overhang = round(overhang[0] + overhang[1]/12, 3)
beam_spacing = round(beam_spacing[0] + beam_spacing[1]/12, 3)
spacing = [overhang]
for i in range(1,n_beams):
        spacing.append(beam_spacing)
spacing.append(overhang)

w_curb = 0.255
d_curb_first = 0.833
d_curb_last = round(overhang - d_curb_first, 3)
w_ws = 0.038
d_ws_first = 1.667
d_ws_last = round(overhang - d_ws_first, 3)

header = ("STAAD PLANE\n"
        "START JOB INFORMATION\n"
        "JOB NAME {}\n"
        "JOB CLIENT MaineDOT\n"
        "JOB NO {}\n"
        "ENGINEER NAME {}\n"
        "ENGINEER DATE {}\n"        
        "END JOB INFORMATION\n").format(project, win, engineer, date)

units = ("INPUT WIDTH 79\n"
        "UNIT INCHES KIP\n")

layout = ["JOINT COORDINATES"]
nodes = []
extra_nodes = 0
for i in range(0,len(spacing)+1):
    nodes.append( "{num} {dist} 0 0;".format(num=i+1, dist=round(sum(spacing[0:i]*12), 3)) )
    if (i+1) % 5 == 0:
        nodes.append("\n")
        extra_nodes += 1
layout.append(' '.join(nodes))
layout.append("MEMBER INCIDENCES")
members = []
for i in range(1,len(nodes)-extra_nodes):
    members.append("{num} {start} {end};".format(num=i, start=i, end=i+1))
layout.append(' '.join(members))

materials = ("DEFINE MATERIAL START\n"
        "ISOTROPIC CONCRETE\n"
        "E 3150\n"
        "POISSON 0.17\n"
        "DENSITY 8.7e-005\n"
        "ALPHA 5e-006\n"
        "DAMP 0.05\n"
        "TYPE CONCRETE\n"
        "STRENGTH FCU {}\n"
        "END DEFINE MATERIAL\n").format(fprimec)

properties = ("MEMBER PROPERTY AMERICAN\n"
        "1 TO {} PRIS YD {} ZD 12\n"
        "CONSTANTS\n"
        "MATERIAL CONCRETE ALL\n").format(len(members), tdeck)

supports = ("SUPPORTS\n"
        "2 TO {} PINNED\n").format(len(nodes)-2)

loads = ["UNIT FEET KIP"]
# Slab weight
loads.append("LOAD 1 LOADTYPE Dead  TITLE SLAB\n"
        "SELFWEIGHT Y -1")
# Railing unit load
loads.append("LOAD 2 LOADTYPE Dead  TITLE RAIL\n"
        "MEMBER LOAD\n"
        "1 CON GY -1 0.943")
# Curb
loads.append("LOAD 3 LOADTYPE Dead  TITLE CURB\n"
        "MEMBER LOAD\n"
        "1 CON GY -{} {}".format(w_curb, d_curb_first) )
loads.append("{} CON GY -{} {}".format(len(members), w_curb, d_curb_last) )
# Wearing surface
loads.append("LOAD 4 LOADTYPE Dead  TITLE WEARING SURFACE\n"
        "MEMBER LOAD\n"
        "2 TO {} UNI GY -{}".format(len(members)-1, w_ws) )
loads.append("1 UNI GY -{} {}".format(w_ws, d_ws_first) )
loads.append("{} UNI GY -{} 0 {}".format(len(members), w_ws, d_ws_last) )
# Wheel in overhang
loads.append("LOAD 5 LOADTYPE Live  TITLE WHEEL-OVERHANG\n"
        "MEMBER LOAD\n"
        "1 CON GY -16 2.667")        # valid only for overhangs longer than 2'-8"
loads.append("2 CON GY -16 {}".format(round(6-(overhang-2.667), 3)) )
# Lane in overhang
loads.append("LOAD 6 LOADTYPE Live  TITLE LANE-POSITIVE\n"
        "MEMBER LOAD\n"
        "1 UNI GY -0.064 2.667\n"
        "2 UNI GY -0.064")
loads.append("3 UNI GY -0.064 0 {}".format(round(10-(overhang-2.667)-beam_spacing, 3)) )    # valid only for overhang + beam spacing of 12'-8" or less

analysis = ("PERFORM ANALYSIS PRINT STATICS CHECK\n"
        "PRINT MEMBER FORCES LIST 1 2\n"
        "PRINT SUPPORT REACTION LIST 2 3\n"
        "FINISH")

staad_deck=open("deck.std","w+")
staad_deck.writelines([header, units, '\n'.join(layout), '\n', materials, properties, supports, '\n'.join(loads), '\n', analysis])
staad_deck.close()

input("New deck.std file written.\n\nPress enter to close.")
