import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))
shapeScore = {"X":1,"Y":2,"Z":3}

myShape = {"X":"Rock","Y":"Paper","Z":"Scissors"}
opponentShape = {"A":"Rock","B":"Paper","C":"Scissors"}
shapeWhichBeats = {"Rock":"Paper","Paper":"Scissors","Scissors":"Rock"}
totalScore = 0

def gameScore(me, opponent):
  me = myShape[me]
  opponent = opponentShape[opponent]
  if me == opponent:
    return 3
  elif opponent == shapeWhichBeats[me]:
    return 0
  else:
    return 6
  
while True:
    line = file.readline()
    if line != "":
      totalScore += shapeScore[line[2]] + gameScore(line[2],line[0])
    else:
      break
print("Total score:", totalScore)