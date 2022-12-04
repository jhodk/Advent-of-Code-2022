import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))
shapeScore = {"Rock":1,"Paper":2,"Scissors":3}
myShape = {"X":"Rock","Y":"Paper","Z":"Scissors"}
opponentShape = {"A":"Rock","B":"Paper","C":"Scissors"}
shapeWhichBeats = {"Rock":"Paper","Paper":"Scissors","Scissors":"Rock"}
shapeWhichLoses = {v:k for k, v in shapeWhichBeats.items()}
totalScore = 0

def gameScore(me, opponent):
  if me == opponent:
    return 3
  elif opponent == shapeWhichBeats[me]:
    return 0
  else:
    return 6
  
while True:
    line = file.readline()
    if line != "":
      opponent = opponentShape[line[0]]
      if line[2] == "Y":
        me = opponent
      elif line[2] == "Z":
        me = shapeWhichBeats[opponent]
      else:
        me = shapeWhichLoses[opponent]
      totalScore += shapeScore[me] + gameScore(me,opponent)
    else:
      break
print("Total score:", totalScore)