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
        fileExists = os.path.exists(file)
        if not fileExists:
          shutil.move(source, destination)
          filesCounter += 1
        else:
          print(file + " already exists")

  print(str(filesCounter) + " files moved.")

extractFolders()