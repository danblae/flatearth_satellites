satellite14 = open("sateliti14.txt", "r")  # Opens the file
fileLength = len(open("sateliti14.txt", "r").readlines())  # Gets length of the file (Amount of lines in the file)
count = 0  # Just a counter can be removed
previousLine = satellite14.readline()  # Reads in the first line of the document


# Checks if the lines are created by the same satellite.
def checkSameSatellite(previous, current):
    if float(previous.split()[0]) == float(current.split()[0]):
        return True
    return False


# Compares the target values in the 4th position from the two lines. and prints the line which is closer to 180 or 0
def compareValues(previous, current):
    if float(previous.split()[3]) < 180 < float(current.split()[3]):
        if 180 - float(previous.split()[3]) < float(current.split()[3]) - 180:
            print(previousLine)
        else:
            print(currentLine)
        return True
    elif float(previousLine.split()[3]) > 300 > float(currentLine.split()[3]):
        if 360 - float(previous.split()[3]) < float(current.split()[3]):
            print(previousLine)
        else:
            print(currentLine)
        return True
    return False


# Reads in line after line and compares them with another to print out the needed lines with the value, that is needed
for i in range(fileLength - 1):
    currentLine = satellite14.readline()
    if checkSameSatellite(previousLine, currentLine):
        if compareValues(previousLine, currentLine):
            count += 1
    previousLine = currentLine
print(count)
