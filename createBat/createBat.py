import os

def run():
    root = os.getcwd()

    for path, dirs, files in os.walk(root):
        for file in files:
            if file.endswith(".py"):
                file_name = os.path.splitext(file)[0]
                file_path = root + "\\" + file
                bat_file = open(file_name + ".bat", "w+")
                bat_file.write("@py.exe " + file_path + " %*")
                bat_file.close()

if __name__ == '__main__':
    run()