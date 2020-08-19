import os
import shutil

currentLogin = os.getlogin()
currentDirectory = os.chdir(rf"C:\Users\{currentLogin}\Desktop")


def docxFile():
    for file in os.listdir(currentDirectory):
        if file.endswith(".docx"):
            if not os.path.exists(rf"C:\Users\{currentLogin}\Desktop\Word"):
                os.makedirs(rf"C:\Users\{currentLogin}\Desktop\Word")
                shutil.move(file, rf"C:\Users\{currentLogin}\Desktop\Word")
            else:
                shutil.move(file, rf"C:\Users\{currentLogin}\Desktop\Word")
                
def pyFile():
    for file in os.listdir(currentDirectory):
        if file.endswith((".py", ".pyw")):
            if not os.path.exists(rf"C:\Users\{currentLogin}\Desktop\Python"):
                os.makedirs(rf"C:\Users\{currentLogin}\Desktop\Python")
                shutil.move(file, rf"C:\Users\{currentLogin}\Desktop\Python")
            else:
                shutil.move(file, rf"C:\Users\{currentLogin}\Desktop\Python")

def txtFile():
    for file in os.listdir(currentDirectory):
        if file.endswith(".txt"):
            if not os.path.exists(rf"C:\Users\{currentLogin}\Desktop\Notes"):
                os.makedirs(rf"C:\Users\{currentLogin}\Desktop\Notes")
                shutil.move(file, rf"C:\Users\{currentLogin}\Desktop\Notes")
            else:
                shutil.move(file, rf"C:\Users\{currentLogin}\Desktop\Notes")

