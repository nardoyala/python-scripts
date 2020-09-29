import os

root = os.getcwd()
files = os.listdir(root)

for file in files:
    if file.endswith(".py"):
        fileName = os.path.splitext(file)[0]
        filePath = root + "\\" + file
        batFile = open(fileName + ".bat", "w+")
        batFile.write("@py.exe " + filePath + " %*")
        batFile.close()
