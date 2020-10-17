import os
import re


def add_leading_zero(number):
    number_string = str(number)
    digits = len(number_string)
    number = ("0"*(3 - digits)) + number_string
    return number


def rename(user_choice):
    files_counter = 0
    root = os.getcwd()
    for path, dirs, files in os.walk(root):
        file_names = os.listdir(path)
        if user_choice == 3:
            custom_name = input("Type base name: ")
            separator = input("Type separator: ")
            validator = True
            leading_zero = input("Do you want leading zeroes? (Y/N)").lower()
            while leading_zero != "y" and leading_zero != "n":
                leading_zero = input("Please, select a valid option (Y/N):")
            counter = 1
        for file_name in file_names:
            if user_choice == 1:
                dst = file_name.capitalize()
            if user_choice == 2:
                dst = file_name.lower()
            if user_choice == 3:
                extention = re.search("\.([^.]+$)", file_name)
                extention = extention.group(0)
                if leading_zero == "y":
                    dst = custom_name + separator + \
                        add_leading_zero(counter) + extention
                    counter += 1
                elif leading_zero == "n":
                    dst = custom_name + separator + str(counter) + extention
                    counter += 1
            src = path + "\\" + file_name
            dst = path + "\\" + dst

            os.rename(src, dst)
            files_counter += 1

    print(str(files_counter) + " files renamed")

def run():
    CHOICES = ["1", "2", "3"]

    print("What do you want to do?")
    print("1 Capitalize")
    print("2 Lowercase")
    print("3 Custom")

    while True:
        user_choice = input()
        if user_choice in CHOICES:
            user_choice = int(user_choice)
            break
        else:
            print("Please, select a proper option")

    rename(user_choice)

if __name__ == '__main__':
    run()