import os
import re


def addLeadingZero(number):
    numberString = str(number)
    digits = len(numberString)
    number = ("0"*(3 - digits)) + numberString
    return number


def rename(userChoice):
    filesCounter = 0
    root = os.getcwd()
    for path, dirs, files in os.walk(root):
        fileNames = os.listdir(path)
        if userChoice == 3:
            customName = input("Type base name: ")
            separator = input("Type separator: ")
            validator = True
            leadingZero = input("Do you want leading zeroes? (Y/N)").lower()
            while leadingZero != "y" and leadingZero != "n":
                leadingZero = input("Please, select a valid option (Y/N):")
            counter = 1
        for fileName in fileNames:
            if userChoice == 1:
                dst = fileName.capitalize()
            if userChoice == 2:
                dst = fileName.lower()
            if userChoice == 3:
                extention = re.search("\.(.*)", fileName)
                extention = extention.group(0)
                if leadingZero == "y":
                    dst = customName + separator + \
                        leadingZero(counter) + extention
                    counter += 1
                elif leadingZero == "n":
                    dst = customName + separator + str(counter) + extention
                    counter += 1
            src = path + "\\" + fileName
            dst = path + "\\" + dst

            os.rename(src, dst)
            filesCounter += 1

    print(str(filesCounter) + " files renamed")


choices = ["1", "2", "3"]

print("What do you want to do?")
print("1 Capitalize")
print("2 Lowercase")
print("3 Custom")

while True:
    userChoice = input()
    if userChoice in choices:
        userChoice = int(userChoice)
        break
    else:
        print("Please, select a proper option")

rename(userChoice)
