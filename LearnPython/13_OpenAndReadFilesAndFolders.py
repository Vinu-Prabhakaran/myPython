import os
import shutil
import send2trash

def clean_up():
    # os.remove("/Users/vinu/Documents/Work/myPython/LearnPython/temp/test_file.txt")
    send2trash.send2trash("/Users/vinu/Documents/Work/myPython/LearnPython/temp/test_file.txt")

if __name__ == "__main__":
    clean_up()
    print(os.getcwd())
    print(os.listdir())
    print(os.listdir("/Users/vinu/Documents/Work/myPython/LearnPython"))
    with open("test_file.txt","w+") as f:
        f.write("This is a test file")
        f.close()

    # Move files
    shutil.move("test_file.txt","temp")
    print(os.listdir("temp/"))

    # Walk through a directory
    walk_dir = '/Users/vinu/Documents/Work/myPython/LearnPython'
    print(f"Walking through {walk_dir}")
    for folder,sub_folders,files in os.walk(walk_dir):
        if folder.__contains__("/Users/vinu/Documents/Work/myPython/LearnPython/.venv"):
            break
        print(f"Current Folder : {folder}")
        if len(sub_folders) == 0:
            print("No sub folders")
        else:
            print(f"Sub Folders under {folder}")
        for sub_folder in sub_folders:
            print(sub_folder)

        print(f"Files are :")
        for file in files:
            print(file)

