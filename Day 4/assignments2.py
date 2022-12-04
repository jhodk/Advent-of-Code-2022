import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))

def processLine(line):
  ranges = list(map(lambda a: a.split("-"), line.split(",")))
  ranges = list(map(lambda a: {*range(int(a[0]),int(a[1])+1)}, ranges))
  if len(ranges[0].intersection(ranges[1])) > 0:
    return 1
  else:
    return 0

totalContained = 0
while True:
    line = file.readline()
    if line != "":
      totalContained += processLine(line)
    else:
      break

print("Total contained:",totalContained)