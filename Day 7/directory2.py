import os
file = open(os.path.join(os.path.dirname(__file__), "input.txt"))

working_directory_path = []
sizes_map = {"/":0}

def processLine(line):
  args = line.split()
  if args[0] == "$":
    if args[1] == "cd":
      if args[2] == "..":
        working_directory_path.pop()
      else:
        working_directory_path.append(args[2])
  else:
    if args[0] != "dir":
      working_directory_path_copy = list(working_directory_path)
      while(len(working_directory_path_copy) > 0):
        sizes_map["/".join(working_directory_path_copy)] = sizes_map.get("/".join(working_directory_path_copy), 0) + int(args[0])
        working_directory_path_copy.pop()

while True:
    line = file.readline()
    if line != "":
      processLine(line)
    else:
      break

usedSpace = sizes_map["/"]
totalSpace = 70e6
freeSpace = totalSpace - usedSpace
requiredSpace = 30e6

minimum = totalSpace
for dirSize in sizes_map.values():
  if(freeSpace+dirSize >= requiredSpace and dirSize < minimum):
    minimum = dirSize

print("Smallest folder size which can be deleted to meet the required space is", minimum)