import os, sys
from math import *

def cmd(command):
    if command == "about":
        print "\nThe Python Math Interpreter is a program created for the purpose of simplifying simple math expressions."
        print "It is currently in version 1.2 and can do arithmetic, logarithmic, and trigonometric math with order of operations."
        print "The program will be updated every once in a while and new functions will be added.\n"
        return True

    if command == "cls":
        os.system("cls")
        return True
    
    elif command == "commands":
        print "\nCommands:\n\n\tabout\n\tcls\n\tcommands\n\tquit\n"
        return True
    
    elif command == "quit":
        sys.exit()

    return False

def main():
    print
    
    while True:
        exp = raw_input(">>> ")

        if not cmd(exp.lower()):
            print
            
            try:
                print eval(exp)
            
            except Exception as e:
                print "ERRROR: " + str(e)

            print

os.system("title Python Math Interpreter")
print "PYTHON MATH INTERPRETER 1.2"

if __name__ == "__main__":
    main()
