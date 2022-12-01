import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))
runningTotal = 0
maximums = [0,0,0]

def updateMaximums():
    global maximums
    global runningTotal
    maximums.append(runningTotal)
    maximums = sorted(maximums)
    maximums = maximums[1:]

while True:
    line = file.readline()
    if line == "":
        if runningTotal > min(maximums):
            updateMaximums()
        break
    if line == "\n":
        if runningTotal > min(maximums):
            updateMaximums()
        runningTotal = 0
    else:
        runningTotal += int(line)

print("Sum of top 3 calories",sum(maximums))

