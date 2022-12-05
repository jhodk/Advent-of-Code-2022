import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))

from collections import deque

startCraning = False
stacks = []

def processLine(line):
  if startCraning:
    processInstruction(line)
  else:
    processConfiguration(line)

def processConfiguration(line):
  global stacks
  if stacks == []:
    stacks = [deque() for i in range(len(line)//4)]
  for i in range(len(stacks)):
    if line[1 + i*4] != " ":
      stacks[i].appendleft(line[1 + i*4])

def processInstruction(line):
  line = list(map(int, line.split()[1::2]))
  grabbedStack = deque()
  for i in range(line[0]):
    grabbedStack.append(stacks[line[1]-1].pop())
  for i in range(line[0]):
    stacks[line[2]-1].append(grabbedStack.pop())

while True:
    line = file.readline()
    if line != "":
      if line[0] == " ":
        startCraning = True
        file.readline()
        line = file.readline()
      processLine(line)
    else:
      break

print("Top of stacks:", "".join(list(map(lambda a: a.pop(), stacks))))