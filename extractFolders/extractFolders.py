import os
import shutil


def extractFolders():
    root = os.getcwd()
    filesCounter = 0
    isUserSure = ""
    sure = False

    print("Be careful! all folders inside " +
          os.getcwd() + " will be extracted.")
    while isUserSure not in ["y", "n"]:
        isUserSure = input(
            "Are you sure to extract all folders? (Y/N): ").lower()

    if isUserSure == "y":
        sure = True

    if sure:
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
