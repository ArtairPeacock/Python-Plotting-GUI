# Importing all of tkinter library
from tkinter import *
  
# Import filedialog module
from tkinter import filedialog

# Importing pandas for the excel manipulation
import pandas as pd

# Depenancy for pandas stuff
import openpyxl 

import numpy as np
import matplotlib.pyplot as plt
  
# Function for opening the 
# file explorer window
# This version opens Excel files 
# (see format of line 18 in "filetypes")

data_file_location = ""

def BrowseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Data Files",
                                                        "*.xlsx"),
                                                       ("all files",
                                                        "*.*")))
                                                        
    # Accesses global variable and changes it to the location
    # of the data file to be plotted														
    global data_file_location
    data_file_location = filename 

    # Change label contents
    label_file_explorer.configure(text="File Opened: " + str(filename))                                                                      

# Create the root window
window = Tk()
  
# Set window title
window.title('File Explorer')

# Set window size
window.geometry("700x500")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window, 
                            text = "Please select the data file you wish to use. \n Accepts Excel files only.",
                            width = 100, height = 4, 
                            fg = "black")
  
button_explore = Button(window, 
                        text = "Browse Files",
                        command = BrowseFiles) 
  
button_exit = Button(window, 
                     text = "Exit",
                     command = exit)       

# Initalising lists for holding data                  
x_values = []
y_values = []
                 
def Load2DData():
	# Excel file must have title of columns in the first cell
	df = pd.read_excel(data_file_location, usecols=range(0, 2))
	
	# Global to allow plot function to have updated versions
	global x_values 
	x_values = df[df.columns[0]].values.tolist()
	
	global y_values
	y_values = df[df.columns[1]].values.tolist() 
	         
def Plot2DData():
	plt.scatter(x_values, y_values)
	
	plt.grid(True)
	plt.title("Bruh")
	plt.xlabel("x")
	plt.ylabel("y")
	
	plt.show()
		
button_test = Button(window,
					 text = "Load 2D Data",
					 command = Load2DData)		
					 
button_plot = Button(window,
					 text = "Plot 2D Data",
					 command = Plot2DData)			
							 
# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
  
button_explore.grid(column = 1, row = 2)
  
button_exit.grid(column = 1, row = 3)

button_test.grid(column = 1, row = 4)

button_plot.grid(column = 1, row = 5)

# Let the window wait for any events
window.mainloop()
