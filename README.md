# Assembly2.0
I tried recreating the assembly language; here is the documentation. The language works on a output stack. Watch this video for a complete explanation

# Syntax

Keyword &emsp; &emsp; [variable name] &emsp; &emsp; [value]

The language is Space-Sensitive and Case-Sensitive, so use only one space for each token and also capital letters for Keywords

# Keywords

Keywords are mnemonics used to perform certain operations

Following are the keywords with the definitions

## PUSH


PUSH &emsp; [variable/value]

Appends the given data value to the stack


## SET


SET &emsp; [variable] &emsp; [value]

Updates the value of the given variable with the given new value

## JUMP


JUMP &emsp; [line index]

Jumps the code execution to the given line index

The line index starts with 0

## JUMPIF


JUMPIF &emsp; [line index]

Jumps the code execution to the given line index if the last inputted value of the stack is 1

The line index starts with 0

## PRN


PRN

Prints the last inputted value of the stack


## VAR


VAR &emsp; [var name] &emsp; [initialization value]

Creates a new variable with the given name

## INPUT


INPUT &emsp; [var name]

Takes user input and stores it in the given variable

## ADD

ADD

Adds the last two inputted values of the stack and pushes the result back into the stack

## SUB

SUB

Substracts the last two inputted values of the stack and pushes the result back into the stack

## MULTI

MULTI

Multiply the last two inputted values of the stack and pushes the result back into the stack

## DIV

DIV

Divides the last two inputted values of the stack and pushes the result back into the stack

## MOD

MOD

Gets the modulus of the last two inputted values of the stack and pushes the result back into the stack

## INC

INC &emsp; [var name]

Increases the value of var by 1

## DEC

DEC &emsp; [var name]

Decreases the value of var by 1

## LT

LT 

Gets the last two inputted values of the stack and if last < second last value, pushes 1 to the stack else pushes 0

## LTE

LTE 

Gets the last two inputted values of the stack and if last <= second last value, pushes 1 to the stack else pushes 0

## GT

GT 

Gets the last two inputted values of the stack and if last > second last value, pushes 1 to the stack else pushes 0

## GTE

GTE 

Gets the last two inputted values of the stack and if last >= second last value, pushes 1 to the stack else pushes 0

## STOP

STOP 

Ends the code execution

## PULL

PUSH PULL

Not a keyword but used to return the last inputted value of the stack and used as a variable


# Loops

Loops can be coded using LOOP keyword and the premade CTR variable

## Syntax


SET CTR [Number of iterations -1]

[codelines]
  
...

LOOP [line index to loop to each time]

LOOP is executed until CTR is 0


# Arrays

Uses the same keywords PUSH[] VAR[] SET[]

These keywords work the same just uses and extra []

Uses the premade SI variable to point to the index of the current array

## Syntax

SET SI [value]

PUSH[] [array name]

-- Pushes the value of array name at the SI index


# Functions

Uses the CALL keyword with a variable to store the index of the line where CALL is used 

## Syntax

VAR [line var] [line index]

CALL [line var] [line index of the 1st line of function]

[codelines]

...

STOP

[First line of function]

[function codelines]

...

JUMP [line var]


# PS

Thanks for checking it out

If you find any Issue create a issue in the repo, I will fix it

HAPPY CODING :)


























