import os
import shutil

def extractFolders():
  root = os.getcwd()
  filesCounter = 0

  for path, dirs, files in os.walk(os.getcwd()):

    for file in files:
      if path != root:
        source = path + "\\" + file
        destination = root
        shutil.move(source, destination)
        filesCounter += 1

  print(str(filesCounter) + " files moved.")

extractFolders()