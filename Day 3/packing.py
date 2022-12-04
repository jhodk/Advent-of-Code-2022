import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))

def priorityScore(item):
  if ord(item) >= 97:
    return ord(item) - 96
  else:
    return ord(item) - 38

def processLine(line):
  compartment1 = {}
  compartment2 = {}
  for i in range((len(line))//2):
    compartment1[line[i]] = 0
    compartment2[line[i+len(line)//2]] = 0
    if(line[i] in compartment2):
      return priorityScore(line[i])
    if(line[i+len(line)//2] in compartment1):
      return priorityScore(line[i+len(line)//2])

totalPriority = 0
while True:
    line = file.readline()
    if line != "":
      totalPriority += processLine(line)
    else:
      break

print("Total priority score:",totalPriority)