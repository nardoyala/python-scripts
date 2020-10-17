import os
import shutil


def run():
    root = os.getcwd()
    files_counter = 0
    is_user_sure = ""
    sure = False

    print("Be careful! all folders inside " +
          os.getcwd() + " will be extracted.")
    while is_user_sure not in ["y", "n"]:
        is_user_sure = input(
            "Are you sure to extract all folders? (Y/N): ").lower()

    if is_user_sure == "y":
        sure = True

    if sure:
        for path, dirs, files in os.walk(os.getcwd()):

            for file in files:
                if path != root:
                    source = path + "\\" + file
                    destination = root
                    file_exists = os.path.exists(file)
                    if not file_exists:
                        shutil.move(source, destination)
                        files_counter += 1
                    else:
                        print(file + " already exists")

    print(str(files_counter) + " files moved.")

if __name__ == '__main__':
    run()
