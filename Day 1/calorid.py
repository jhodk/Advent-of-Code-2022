import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))
runningTotal = 0
currentMaximum = 0

while True:
    line = file.readline()
    if line == "":
        break
    if line == "\n":
        runningTotal = 0
    else:
        runningTotal += int(line)
        if runningTotal > currentMaximum:
            currentMaximum = runningTotal

print("Maximum calories held:",currentMaximum)

