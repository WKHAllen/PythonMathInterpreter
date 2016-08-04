from os import system

chars = {
    "nums": {
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
    },
    "operators": {
        '+', '-', '*', '/'
    },
    "misc": {
        '(', ')'
    }
}

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

def check(exp):
    par = 0
    
    for a in range(len(exp)):
        if exp[a] == '(':
            par += 1
        elif exp[a] == ')':
            par -= 1

        if par < 0:
            print "\nERROR: Unbalanced parentheses"
            return False

        if a < len(exp) - 1 and exp[a] == '(' and exp[a + 1] == ')':
            print "\nERROR: Empty parentheses ()"
            return False

        if exp[a] not in chars["nums"] and exp[a] not in chars["operators"] and exp[a] not in chars["misc"]:
            print "\nERROR: Unexpected character '" + exp[a] + "'"
            return False

        if a < len(exp) - 1 and exp[a] == '-' and exp[a + 1] in chars["operators"]:
            print "\nERROR: Invalid syntax '" + pythonize(exp[a:a + 2]) + "'"
            return False

        if a < len(exp) - 2 and exp[a] in chars["operators"] and exp[a + 1] in chars["operators"] and exp[a + 2] in chars["operators"]:
            print "\nERROR: Invalid syntax '" + pythonize(exp[a:a + 3]) + "'"
            return False

        if a > 0 and a < len(exp) - 1 and exp[a] in chars["operators"] and ((exp[a - 1] not in chars["nums"] and exp[a - 1] not in chars["misc"]) or (exp[a + 1] not in chars["nums"] and exp[a + 1] not in chars["misc"])) and exp[a] != '-' and exp[a + 1] != '-':
            print "\nERROR: Invalid syntax '" + pythonize(exp[a - 1:a + 2]) + "'"
            return False

    if exp == "":
        print "\nERROR: String must not be empty"
        return False

    if exp == "-":
        print "\nERROR: Invalid syntax '-'"
        return False
    
    if par != 0:
        print "\nERROR: Unbalanced parentheses"
        return False

    if (exp[0] in chars["operators"] or exp[len(exp) - 1] in chars["operators"]) and exp[0] != '-':
        print "\nERROR: Expression cannot begin or end with an operator"
        return False

    return True

def solve(exp):
    if not check(exp):
        main()
    
    if work:
        print pythonize(exp)
        
    found = False
    
    for b in range(1, len(exp)):
        if exp[b] in chars["operators"]:
            found = True
    
    if exp.find("(") != -1:
        start = -1
        par = 0
        
        for c in range(len(exp)):
            if c >= len(exp):
                break
            
            if exp[c] == '(' and start == -1:
                start = c

            if exp[c] == '(':
                par += 1
                
            elif exp[c] == ')':
                par -= 1

            if par == 0 and start != -1:
                exp = exp[:start] + solve(exp[start + 1:c]) + exp[c + 1:]
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

        if exp[op] == '+':
            ans = (firstmult * int(first)) + (secondmult * int(second))

        elif exp[op] == '-':
            ans = (firstmult * int(first)) - (secondmult * int(second))

        elif exp[op] == '*':
            ans = (firstmult * int(first)) * (secondmult * int(second))

        elif exp[op] == '/':
            ans = (firstmult * int(first)) / (secondmult * int(second))

        exp = str(ans) + exp[loop:]
        exp = solve(exp)
    
    return exp

def cmd(command):
    if command == "about":
        print "\nThe Python Math Interpreter is a program created for the purpose of simplifying simple math expressions."
        print "It is currently in version 1.0 and can only do arithmetic math with no order of operations apart from parentheses."
        print "The program will be updated every once in a while and new functions will be added.\n"
        return True

    if command == "cls":
        system("cls")
        return True
    
    elif command == "commands":
        print "\nCommands:\n\n\tabout\n\tcls\n\tcommands\n\texit\n\twork\n"
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

        if not cmd(exp):
            exp = exp.replace(" ", "")
            
            if check(exp):
                if work:
                    print
                
                ans = solve(exp)

            print

            if ans != None:
                print ans + "\n"

system("title Python Math Interpreter")
print "PYTHON MATH INTERPRETER 1.0"

main()
