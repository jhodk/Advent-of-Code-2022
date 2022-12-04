import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))

def priorityScore(item):
  if ord(item) >= 97:
    return ord(item) - 96
  else:
    return ord(item) - 38

def processLine(line, line2, line3):
  listsByLength = sorted([line,line2,line3], key=len)
  set1 = set(listsByLength[1])
  set2 = set(listsByLength[2])
  searchList = listsByLength[0]
  for i in range(len(searchList)):
    if searchList[i] in set1 and searchList[i] in set2:
      return priorityScore(searchList[i])

totalPriority = 0
while True:
    line = file.readline()
    if line != "":
      line2 = file.readline()
      line3 = file.readline()
      totalPriority += processLine(line, line2, line3)
    else:
      break

print("Total priority score:",totalPriority)