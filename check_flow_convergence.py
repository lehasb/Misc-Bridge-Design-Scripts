import textwrap

# Bring in file using browse dialog
import tkinter
from tkinter import filedialog
root = tkinter.Tk()     # define base window so it can be hidden
root.withdraw()         # hide base window
file_path = filedialog.askopenfilename()
print("Opening " + file_path)
root.destroy()          # get rid of window so it doesn't mess up graphing window later

# Process data
import numpy
clean_data = numpy.loadtxt(file_path, skiprows=1)
num_rows = clean_data.shape[0]
last_time = clean_data[num_rows - 1, 0]
print("\nThere are " + str(num_rows) + " rows, with the last time being " + str(last_time) + " hours\n")

# Check when diff Q < 0.5%
row = 1
while (abs(clean_data[row,1] - clean_data[row-1,1]) > (0.001 * clean_data[num_rows-1,1])):
    row = row + 1
else:
    output_string = "The model has a flow difference from the previous flow of less than 0.1% the final flow at the time of " + str(clean_data[row,0]) + " hours, when the flow was " + str(clean_data[row,1]) + " cubic feet per second, and the water surface elevation was " + str(clean_data[row,2]) + " feet."
    print(textwrap.fill(output_string))

# Make graph
from matplotlib import pyplot
pyplot.plot(clean_data[...,0], clean_data[...,1])
pyplot.title('Flow through monitor line over model run time')
pyplot.xlabel('Time ($hrs$)')
pyplot.ylabel('Flow ($ft^3/s$)')
pyplot.show()

# Keep window open to read data until hit enter
input("\nPress enter to close")
