# COMMANDS = BASIC
PUSH = "PUSH"
PULL = "PULL"
SET = "SET"
JUMP = "JUMP"
JUMPIF = "JUMPIF"
LOOP = "LOOP"
STOP = "STOP"
PRN = "PRN"
VAR = "VAR"
INPUT = "INPUT"                 
CALL = "CALL"               #for functions


#COMMANDS = MATHS
ADD = "ADD"
SUB = "SUB"
MULTI = "MULTI"
DIV = "DIV"
MOD = "MOD"
INC = "INC"
DEC = "DEC"

#COMMANDS = LOGIC
LT = "LT"
GT = "GT"
LTE = "LTE"
GTE = "GTE"
AND = "AND"
OR = "OR"


# REGISTER
CTR = "CTR"                 #for loops
SI = "SI"                   #for arrays


counter = 0
sourceIndex = 0
stack = []
variables = {}
arrays = {}

#Common function to raise and print errors
def raiseError(errorType, pointer, varKey = ""):
    if(errorType == "ne"): raise NameError(f"Error occurred at line {pointer}\nvariable {varKey} not found")
    elif(errorType == "se"):raise SyntaxError(f"Error occurred at line {pointer}\nInvalid Syntax")
    elif(errorType == "me"): raise MemoryError(f"Error occurred at line {pointer}\nStack out of memory")
    elif(errorType == "te"): raise TypeError(f"Error occurred at line {pointer}\nCan't operate with different types")
    elif(errorType == "zde"): raise ZeroDivisionError(f"Error occurred at line {pointer}\nCan't divide with 0")
    elif(errorType == "ie"): raise IndexError(f"Error occurred at line {pointer}\nIndex is out of range")
    else: raise RuntimeError(f"Unknown error occurred at line {pointer}")


#To change and set new values for variables and registers
def setVar(varKey,value,pointer):
    global counter
    global variables
    global sourceIndex

    if(CTR in varKey): counter = value
    elif(SI in varKey) : sourceIndex = value
    elif(varKey in variables): variables[str(varKey)] = value
    else: raiseError("ne",pointer,varKey)


#To check and store the values with correct data type
def evalCode(code,pointer):
    code = str(code)
    if(PULL in code): return stack[len(stack)-1]
    elif(CTR in code): return counter
    elif(SI in code): return sourceIndex
    elif(code.isnumeric()): return int(code)
    elif(code in variables): return evalCode(str(variables[str(code)]),pointer)

    #Checkc for float
    elif(code.isalnum):
        if("." in code):
            flts = code.split(".")
            if(len(flts)==2 and flts[0].isnumeric and flts[1].isnumeric):
                return float(code)
            else:
                return str(code)
    
    return str(code)


# check functions for arrays
def evalArr(code,pointer):

    codeArr = code[1:len(code)-1].split(",")
    for i in range(len(codeArr)):
        codeArr[i] = evalCode(codeArr[i],pointer)
    return(codeArr)


#Reads the code file
def readFile(filePath):
    f = open(filePath, "r")
    return (f.read())
    



#Main compile funciton
def compile(filePath):

    global counter
    global stack
    global variables
    global arrays
    global sourceIndex

    #spliting each line of file into a queue
    codeLines = readFile(filePath).split("\n") 

    #Index for each line         
    pointer = 0  

    #Initial values to the stack so simplyfy some errors        
    stack.append(0)
    stack.append(0)


    try:
        while True:

            #Seperating each line into seperate tokens
            tokens = str(codeLines[pointer]).strip().split(" ")
            
            #First token of each line is a keyword
            keyword = tokens[0]

            #Check for array keywords
            if("[]" in keyword):
                if(PUSH in keyword):

                    if(len(tokens)!=2):raiseError("se",pointer)

                    arrName = str(tokens[1])

                    if(arrName not in arrays): raiseError("ne",pointer,arrName)

                    stack.append(evalCode(arrays[arrName][sourceIndex],pointer))

                elif(VAR in keyword):

                    if(len(tokens)!=3):raiseError("se",pointer)

                    codeArr = evalArr(tokens[2],pointer)
                    arrays[tokens[1]] = codeArr

                elif(SET in keyword):

                    if(len(tokens)!=3):raiseError("se",pointer)

                    arrName = str(tokens[1])

                    if(arrName not in arrays): raiseError("ne",pointer,arrName)

                    val = evalCode(tokens[2],pointer)
                    arrays[arrName][sourceIndex] = val

                else:
                    raiseError("ne",pointer,keyword)

            else:

                if(keyword == PUSH):
                    if(len(tokens)!=2): raiseError("se",pointer)
                    stack.append(evalCode(tokens[1],pointer))
                
                elif(keyword == PULL):
                    print(stack[len(stack)-1])
                    

                elif(keyword == SET):
                    if(len(tokens)!=3): raiseError("se",pointer)

                    val = evalCode(tokens[2],pointer)
                    varKey = str(tokens[1])
                    setVar(varKey,val,pointer)

                elif(keyword == ADD):

                    if(len(tokens)!=1): raiseError("se",pointer)

                    if(len(stack)<2): raiseError("me",pointer)

                    a = stack.pop()
                    b = stack.pop()

                    stack.append(a+b)

                elif(keyword == SUB):
                    if(len(tokens)!=1): raiseError("se",pointer)

                    if(len(stack)<2): raiseError("me",pointer)

                    a = stack.pop()
                    b = stack.pop()
                        
                    stack.append(a-b)

                elif(keyword == MULTI):
                    if(len(tokens)!=1): raiseError("se",pointer)

                    if(len(stack)<2): raiseError("me",pointer)

                    a = stack.pop()
                    b = stack.pop()

                    stack.append(a*b)

                elif(keyword == DIV):
                    if(len(tokens)!=1): raiseError("se",pointer)

                    if(len(stack)<2): raiseError("me",pointer) 

                    a = stack.pop()
                    b = stack.pop()


                    if(b==0): raiseError("zde", pointer)

                    stack.append(a/b)

                elif(keyword == MOD):
                    if(len(tokens)!=1): raiseError("se", pointer)

                    if(len(stack)<2): raiseError("me", pointer)

                    a = stack.pop()
                    b = stack.pop()

                    if(b==0): raiseError("zde", pointer)

                    stack.append(a%b)

                elif(keyword == INC):
                    if(len(tokens)!=2): raiseError("se", pointer)

                    setVar(str(tokens[1]),evalCode(str(tokens[1]),pointer)+1,pointer)

                elif(keyword == DEC):
                    if(len(tokens)!=2): raiseError("se", pointer)

                    setVar(str(tokens[1]), evalCode(str(tokens[1]),pointer)-1,pointer)

                elif(keyword == LT):
                    if(len(tokens)!=1): raiseError("se", pointer)

                    if(len(stack)<2): raiseError("me", pointer)

                    a = stack.pop()
                    b = stack.pop()

                    stack.append(1 if a < b else 0)

                elif(keyword == GT):
                    if(len(tokens)!=1): raiseError("se", pointer)

                    if(len(stack)<2): raiseError("me", pointer)

                    a = stack.pop()
                    b = stack.pop()

                    stack.append(1 if a > b else 0)

                elif(keyword == LTE):
                    if(len(tokens)!=1): raiseError("se", pointer)

                    if(len(stack)<2): raiseError("me", pointer)

                    a = stack.pop()
                    b = stack.pop()

                    stack.append(1 if a <= b else 0)

                elif(keyword == GTE):
                    if(len(tokens)!=1): raiseError("se", pointer)

                    if(len(stack)<2): raiseError("me", pointer)

                    a = stack.pop()
                    b = stack.pop()

                    stack.append(1 if a >= b else 0)

                elif(keyword == AND):
                    if(len(tokens)!=1): raiseError("se", pointer)

                    if(len(stack)<2): raiseError("me", pointer)

                    a = stack.pop()
                    b = stack.pop()

                    stack.append(a and b)

                elif(keyword == OR):

                    if(len(tokens)!=1): raiseError("se", pointer)

                    if(len(stack)<2): raiseError("me", pointer)

                    a = stack.pop()
                    b = stack.pop()

                    stack.append(a or b)

                elif(keyword == JUMP):

                    if(len(tokens)!=2): raiseError("se", pointer)
                    
                    pointer = evalCode(tokens[1],pointer)

                    if(pointer >= len(codeLines) or pointer < 0):
                        raiseError("ie", pointer)

                    pointer -= 1

                elif(keyword == JUMPIF):
                    
                    if(len(stack)<1): raiseError("me", pointer)

                    if(stack.pop() == 1):
                        if(len(tokens)!=2): raiseError("se", pointer)

                        pointer = evalCode(tokens[1],pointer)

                        if(pointer>= len(codeLines) or pointer<0): raiseError("ie", pointer)

                        pointer -= 1

                elif(keyword == LOOP):

                    if(len(tokens)!=2): raiseError("se", pointer)

                    counter -= 1
                    if(counter >= 0):
                        pointer = evalCode(tokens[1],pointer)

                        if(pointer>= len(codeLines) or pointer<0): raiseError("ie", pointer)

                        pointer -= 1

                elif(keyword == PRN):

                    if(len(tokens)!=1): raiseError("se", pointer)

                    if(len(stack)<1): raiseError("me", pointer)

                    print(stack[len(stack)-1])
                
                elif(keyword == CALL):

                    if(len(tokens)!=2): raiseError("se", pointer)
                    
                    destination = evalCode(tokens[2],pointer)
                    setVar(tokens[1],pointer+1,pointer)
                    pointer = destination

                    if(pointer >= len(codeLines) or pointer < 0):
                        raiseError("ie", pointer)

                    pointer -= 1

                elif(keyword == VAR):

                    if(len(tokens)!=3): raiseError("se", pointer)

                    variables[tokens[1]] = evalCode(tokens[2],pointer)

                elif(keyword == INPUT):

                    if(len(tokens)!=2): raiseError("se", pointer)

                    inVal = evalCode(input(),pointer)
                    varKey = str(tokens[1])
                    setVar(varKey,inVal,pointer)

                elif(keyword == STOP):

                    if(len(tokens)!=1): raiseError("se", pointer)


                    # Uncomment below code lines for debugging

                    '''
                    print(stack)
                    print(variables)
                    print(arrays)
                    print(sourceIndex)
                    print("Code executed Successfully")
                    '''

                    #For succesfull code execution
                    raise EOFError("Code executed successfully")

                else: raiseError("ne",pointer,keyword)
                
            pointer += 1

    except Exception as e:
        print(e)
    

compile('code.txt')