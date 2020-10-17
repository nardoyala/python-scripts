import os

root = os.getcwd()

for path, dirs, files in os.walk(root):
    for file in files:
        if file.endswith(".py"):
            fileName = os.path.splitext(file)[0]
            filePath = root + "\\" + file
            batFile = open(fileName + ".bat", "w+")
            batFile.write("@py.exe " + filePath + " %*")
            batFile.close()
