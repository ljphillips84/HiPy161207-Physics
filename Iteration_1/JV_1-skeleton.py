import matplotlib.pyplot as plt
import numpy as np


# ---- Start Functions ---- #
def getVoc(data):
    #
    #code goes here
    #
    return Voc

def getJsc(data):
    #
    # code goes here
    #
    return Jsc

def getFF(data):
    #
    # code goes here
    #
    return FF

def getEff(data):
    #
    # code goes here
    #
    return Eff

def i_to_j(data):
    #
    # code goes here
    #
    return data
# ---- End Functions ---- #


# ---- Main Program ----#

# Import data into an array
#
data =
#

# Convert I to J
#
#

# Plot the data
#
#

# When all the functions are completed, running the script should output all the parameters:

print("Voc = " + str.format('{0:.2f}', getVoc(data)) + " V")
print("Jsc = " + str.format('{0:.1f}', getJsc(data)) + " mA cm^-2")
print("FF = " + str.format('{0:.1f}', 100*getFF(data)) + "%")
print("Eff = " + str.format('{0:.1f}', getEff(data)) + "%")
