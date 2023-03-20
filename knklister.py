#Imports
import os
import sys

#Functions
def newfile(filename):
    try:
        f = open(filename, "x")
    except FileExistsError:
        print("Error: File Already Exists")
    else:
        f.close()

def deletefile(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        raise FileNotFoundError("Error: File Doesn't Exists")

def readfile(filename):
    linenum = 0
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("Error: File Doesn't Exists")
    else:
        for line in f:
            print(f"{linenum + 1}. {line}")
            linenum += 1
        f.close()

def addfileline(filename, content):
    try:
        f = open(filename, "a")
    except FileNotFoundError:
        print("Error: File Doesn't Exists")
    else:
        f.write(content + "\n")
        f.close()

def editfileline(filename, fileline, content):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("Error: File Doesn't Exists")
    else:
        f = f.readlines()
        try:
            f[fileline] = content + "\n"
        except:
            print("Error: Invalid Line Number")
        else:
            writef = open(filename, "w")
            writef.writelines(f)
            writef.close()

#KNKLister
print("Welcome to KNKLister!!!")
print("1. Create List")
print("2. Delete List")
print("3. Print List")
print("4. Add New Line to an Existing List")
print("5. Edit a Line in an Existing List")
print("Enter E to Exit")

while True:
    opnum = input("Enter Operation (1-5):- ")
    if opnum == "1":
        listname = input("Enter Name of The List:- ")
        if listname.lower() == "e":
            sys.exit()
        else:
            newfile(listname + ".txt")
    elif opnum == "2":
        listname = input("Enter The Name of The List You Wish to Delete:- ")
        if listname.lower() == "e":
            sys.exit()
        else:
            deletefile(listname + ".txt")
    elif opnum == "3":
        listname = input("Enter The Name of The List You Wish to Read:- ")
        if listname.lower() == "e":
            sys.exit()
        else:
            readfile(listname + ".txt")
    elif opnum == "4":
        listname = input("Enter The Name of List You Wish to Add a Line to:- ")
        linecontent = input("Enter the Contents of line:- ")
        if listname.lower() == "e" or linecontent.lower() == "e":
            sys.exit()
        else:
            addfileline(listname + ".txt", linecontent)
    elif opnum == "5":
        listname = input("Enter The Name of The List You Wish to Edit a Line of:- ")
        listnumber = int(input("Enter The Line Number:- "))
        newlinecontent = input("Enter The Edits:- ")
        if listname.lower() == "e" or str(listnumber).lower() == "e" or newlinecontent.lower() == "e":
            sys.exit
        else:
            editfileline(listname + ".txt", listnumber - 1, newlinecontent)
    elif opnum.lower() == "e":
        sys.exit()
    else:
        raise Exception("Error: Invalid Operation")
