import argparse 
import sys
import ast

def calculateJains(values):
    '''
        This function is meant to calculate the JFI value based on the given values
        values: hold the set of values that we want to calculate their JFI value.
    '''
    # Gathering the JFI formula parts
    lengthOfValues = len(values)
    valuesSquared = [val ** 2 for val in values] 
    # JFI Formula
    JFI = float(pow(sum(values), 2) / (lengthOfValues * sum(valuesSquared)))  
    return JFI

def readFile(inputFile):
    '''
        This function is meant to read a text file, extract values from it and
        convert them into one unit (to Kbps this time) and return them as an list
        of float values that can be later sent into the calculateJains function to
        calculate the JFI value for them.
        inputValues: This arguments holds the destinition of the file that we
        are intending to bring our values from.

    '''
    with open(inputFile,'r',encoding='utf-16') as file:
        contentList = [] # The list that will inhold the values

        # Going through line by line in the file
        for line in file:
            value, unit = line.strip().split(" ") # splitting the file into values and units
            value = float(value)

            # Converting the values into the destination unit (Kbps)
            if unit == "Mbps":
                value = value * 1000
            elif unit == "bps":
                value = value/1000

            contentList.append(value)

    return contentList

# Creating a new argument parser, with the arguments 'file' and 'list' to calculate 
# the JFI based on what kind on inputs user is calculiting the index for.
parser = argparse.ArgumentParser(description='Jains fairness calculator')
parser.add_argument('-f', '--file', type=str, help='Path to the input file') # file argument
parser.add_argument('list', nargs='?', default='[]', help='List of floats') # normal list argument
args = parser.parse_args()

values = []
# Testing if the inputs are valid, otherwise thorw an exception
try:
    if args.file:
        values = readFile(args.file) # reading the file
    else:
        # converting the string list into a float list which makes it possible for the
        # compiler to use the function on the values and return the Jain's fairness index
        values = [float(x) for x in ast.literal_eval(args.list)] 
except Exception as e:
    # iIn case the values are not valid, throw the exception and print what type of exceptions is it
    print(f"Your input is not valid: {e}") 
    sys.exit()

# Calculate the JF index and print it 
print(f"Jains Fairness index is: {calculateJains(values):.3f}")