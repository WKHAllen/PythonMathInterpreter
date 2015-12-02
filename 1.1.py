from math import *
from os import system

chars = {
    "nums": {
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    },
    "operators": {
        '+', '-', '*', '/', '%', '^', '{'
    },
    "misc": {
        '(', ')'
    }
}

commands = [
    ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "+", "-", "*", "/", "%", "^", "{"],
    ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "parentheses", "parentheses", "add", "subtract", "multiply", "divide", "modulus", "exponent", "root"],
    ["1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.0", "1.1", "1.1", "1.1"]
]

work = False

def pythonize(string):
    string = string.replace(" ", "")
    done = False
    
    while not done:
        done = True
        for i in range(1, len(string) - 1):
            if done and string[i] in chars["operators"] and string[i - 1] in chars["operators"] and string[i - 1] != ' ':
                string = string[:i] + " " + string[i:]
                done = False
                
            elif done and string[i] in chars["operators"] and string[i + 1] in chars["operators"] and string[i - 1] != ' ':
                string = string[:i + 1] + " " + string[i + 1:]
                done = False
                
            elif done and string[i] in chars["operators"] and string[i - 1] not in chars["operators"] and string[i - 1] != ' ':
                string = string[:i] + " " + string[i:]
                done = False
                
            elif done and string[i] in chars["operators"] and string[i + 1] not in chars["operators"] and string[i + 1] != ' ':
                string = string[:i + 1] + " " + string[i + 1:]
                done = False

    return string

def syntaxcheck(exp):
    par = 0
    
    for a in range(len(exp)):
        if exp[a] == '(':
            par += 1
        elif exp[a] == ')':
            par -= 1

        if par < 0:
            print "\nSYNTAX ERROR: Unbalanced parentheses"
            return False

        if a < len(exp) - 1 and exp[a] == '(' and exp[a + 1] == ')':
            print "\nSYNTAX ERROR: Empty parentheses ()"
            return False

        if exp[a] not in chars["nums"] and exp[a] not in chars["operators"] and exp[a] not in chars["misc"] and exp[a] != '.':
            print "\nSYNTAX ERROR: Unexpected character '" + exp[a] + "'"
            return False

        if a < len(exp) - 1 and exp[a] == '-' and exp[a + 1] in chars["operators"]:
            print "\nSYNTAX ERROR: Invalid syntax '" + pythonize(exp[a:a + 2]) + "'"
            return False

        if a < len(exp) - 2 and exp[a] in chars["operators"] and exp[a + 1] in chars["operators"] and exp[a + 2] in chars["operators"]:
            print "\nSYNTAX ERROR: Invalid syntax '" + pythonize(exp[a:a + 3]) + "'"
            return False

        if a > 0 and a < len(exp) - 1 and exp[a] in chars["operators"] and ((exp[a - 1] not in chars["nums"] and exp[a - 1] not in chars["misc"]) or (exp[a + 1] not in chars["nums"] and exp[a + 1] not in chars["misc"])) and exp[a] != '-' and exp[a + 1] != '-':
            print "\nSYNTAX ERROR: Invalid syntax '" + pythonize(exp[a - 1:a + 2]) + "'"
            return False

    if exp == "":
        print "\nSYNTAX ERROR: String cannot be empty"
        return False

    if exp == "-" or exp == ".":
        print "\nSYNTAX ERROR: Invalid syntax '" + exp + "'"
        return False
    
    if par != 0:
        print "\nSYNTAX ERROR: Unbalanced parentheses"
        return False

    if (exp[0] in chars["operators"] and exp[0] != '-') or exp[len(exp) - 1] in chars["operators"]:
        print "\nSYNTAX ERROR: Expression cannot begin or end with an operator"
        return False

    return True

def mathcheck(one, two, m1, m2, operation):
    if operation == '/' and two == 0:
        print "\nMATH ERROR: Cannot divide by zero"
        return False

    if operation == '{' and one == 0:
        print "\nMATH ERROR: Root must not be zero"
        return False

    if operation == '{' and one % 2 == 0 and two * m2 < 0:
        print "\nMATH ERROR: Cannot take the even root of a negative number"
        return False

    if operation == '%' and two == 0:
        print "\nMATH ERROR: Cannot mod by zero"
        return False

    return True

def beginningcheck(exp):
    for b in range(len(exp)):
        if b < len(exp) - 1 and exp[b] == ')' and exp[b + 1] == '(':
            exp = exp[:b + 1] + "*" + exp[b + 1:]
            exp = beginningcheck(exp)
            break

        if (b == 0 and len(exp) > 1 and exp[b] == '0' and exp[b + 1] in chars["nums"] and exp[b + 1] != '.') or (b > 0 and b < len(exp) - 1 and exp[b - 1] not in chars["nums"] and exp[b - 1] != '.' and exp[b] == '0' and exp[b + 1] in chars["nums"] and exp[b + 1] != '.'):
            exp = exp[:b] + exp[b + 1:]
            exp = beginningcheck(exp)
            break

        if exp == "-0":
            exp = "0"
            break

    return exp

def endcheck(exp):
    if exp.find(".") != -1 and exp[len(exp) - 1] == '0':
        exp = exp[:len(exp) - 1]
        exp = endcheck(exp)

    if exp.find(".") == len(exp) - 1:
        exp = exp[:len(exp) - 1]

    return exp

def solve(exp):
    if not syntaxcheck(exp):
        main()
    
    if work:
        print pythonize(exp)
        
    found = False
    
    for c in range(1, len(exp)):
        if exp[c] in chars["operators"]:
            found = True
    
    if exp.find("(") != -1:
        start = -1
        par = 0
        
        for d in range(len(exp)):
            if d >= len(exp):
                break
            
            if exp[d] == '(' and start == -1:
                start = d

            if exp[d] == '(':
                par += 1
                
            elif exp[d] == ')':
                par -= 1

            if par == 0 and start != -1:
                exp = exp[:start] + solve(exp[start + 1:d]) + exp[d + 1:]
                exp = solve(exp)

    elif found:
        first = ""
        second = ""
        loop = 0
        firstmult = secondmult = 1

        if exp[loop] == '-':
            firstmult = -1
            loop += 1

        while exp[loop] not in chars["operators"]:
            first += exp[loop]
            loop += 1

        op = loop
        loop += 1

        if exp[loop] == '-':
            secondmult = -1
            loop += 1

        while loop < len(exp) and exp[loop] not in chars["operators"] and exp[loop] not in chars["misc"]:
            second += exp[loop]
            loop += 1

        if mathcheck(float(first), float(second), int(firstmult), int(secondmult), exp[op]):
            if exp[op] == '+':
                ans = (firstmult * float(first)) + (secondmult * float(second))

            elif exp[op] == '-':
                ans = (firstmult * float(first)) - (secondmult * float(second))

            elif exp[op] == '*':
                ans = (firstmult * float(first)) * (secondmult * float(second))

            elif exp[op] == '/':
                ans = (firstmult * float(first)) / (secondmult * float(second))

            elif exp[op] == '%':
                ans = (firstmult * float(first)) % (secondmult * float(second))

            elif exp[op] == '^':
                try:
                    ans = (firstmult * float(first)) ** (secondmult * float(second))

                except:
                    print "\nMATH ERROR: Overflow"
                    main()

            elif exp[op] == '{':
                if float(first) % 2 == 1 and secondmult == -1:
                    ans = -1 * (float(second) ** (1 / (firstmult * float(first))))

                else:
                    ans = (secondmult * float(second)) ** (1 / (firstmult * float(first)))

            if str(ans).find("e") != -1:
                if str(ans)[str(ans).find("e") + 1] == '+':
                    formatting = "{:" + str(int(12 + abs(log(ans, 10)))) + "f}"
                    ans = formatting.format(ans)

                elif str(ans)[str(ans).find("e") + 1] == '-':
                    formatting = "{:." + str(int(12 + abs(log(ans, 10)))) + "f}"
                    ans = formatting.format(ans)

            ans = str(ans)

            exp = ans + exp[loop:]
            
            exp = solve(exp)

        else:
            main()
    
    return exp

def cmd(command):
    if command == "about":
        print "\nThe Python Math Interpreter is a program created for the purpose of simplifying simple math expressions."
        print "It is currently in version 1.1 and can only do arithmetic math with no order of operations apart from parentheses."
        print "The program will be updated every once in a while and new functions will be added.\n"
        return True

    elif command == "characters":
        print "\nCharacters:\n\n\tsyntax\t\tname\t\tversion added\n\t------\t\t----\t\t-------------"
        
        for e in range(len(commands[0])):
            charline = "\t" + commands[0][e] + "\t"

            if len(commands[0][e]) < 8:
                charline += "\t"

            charline += commands[1][e] + "\t"

            if len(commands[1][e]) < 8:
                charline += "\t"

            charline += commands[2][e]

            print charline

        print
        return True

    if command == "cls":
        system("cls")
        return True
    
    elif command == "commands":
        print "\nCommands:\n\n\tabout\n\tcharacters\n\tcls\n\tcommands\n\texit\n\twork\n"
        return True
    
    elif command == "exit":
        quit()

    elif command == "work":
        global work
        
        if work:
            work = False
            
        else:
            work = True
            
        print "\nOption 'work' set to " + str(work) + "\n"
        return True

    return False

def main():
    print
    
    while True:
        exp = raw_input(">>> ")
        ans = None

        if not cmd(exp.lower()):
            exp = exp.replace(" ", "")
            
            if syntaxcheck(exp):
                exp = beginningcheck(exp)
                
                if work:
                    print
                
                ans = solve(exp)

                ans = endcheck(ans)

            print

            if ans != None:
                print ans + "\n"

system("title Python Math Interpreter")
print "PYTHON MATH INTERPRETER 1.1"

main()
