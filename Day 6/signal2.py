import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))
currentLetterPositions = {}
right = 0
searchLength = 14

def processLine(line):
  left = 0
  global right
  right = 0
  currentLetterPositions[line[left]] = 0
  while right < len(line):
    right += 1
    if not line[right] in currentLetterPositions:
      currentLetterPositions[line[right]] = len(currentLetterPositions)
      if right - left == searchLength - 1:
        return
    else:
      duplicateLetterPosition = currentLetterPositions[line[right]]
      positionToRemove = duplicateLetterPosition + 1
      for key in list(currentLetterPositions):
        if currentLetterPositions[key] > duplicateLetterPosition:
          currentLetterPositions[key] -= positionToRemove
        else:
          currentLetterPositions.pop(key)
      currentLetterPositions[line[right]] = len(currentLetterPositions)
      left += duplicateLetterPosition + 1
      right = max(right,left)
  right = -1

while True:
    line = file.readline()
    if line != "":
      processLine(line)
    else:
      break

print("Start-of-packet marker found after:", right + 1, "characters.")

#  0123  duplicate position     move left forward by
#  abcd         -                       -
#  abca         0                       1
#  abcb         1                       2
#  abcc         2                       3