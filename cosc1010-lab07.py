# Kaleb Moler
# UWYO COSC 1010
# 10/30/24
# Lab 7
# Lab Section: 15
# Sources, people worked with, help given to: 
# Jhett Carr, Jay Trujio



# Prompt the user for an upper bound 
# Write a while loop that gives the factorial of that upper bound
# This will need to be a positive number
# For this you will need to check to ensure that the user entered a number
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # If a user did not enter a number output a statement saying so
# You will continue to prompt the user until a proper integer value is entered

def user_fact():
    interger=""
    while(True):
        interger=input("Enter a Factorial: ")
        if(interger.isdigit()):
            return int(interger)
        else:
            print(f"Please enter a positve number.")
        print("*"*75)

def solve_fact(num):
    upper=num
    fact=1
    if(upper>0):
        while(upper>0):
            fact *= upper
            upper -=1
    print("*"*32)
    return(fact)


factorial=solve_fact(user_fact())

print(f"The result of the factorial based on the given bound is {factorial}")

print("*"*75)
# Create a while loop that prompts a user for input of an integer values
# Sum all inputs. When the user enters 'exit' (regardless of casing) end the loop
# Upon ending the loop print the sum
# Your program should accept both positive and negative input
# Remember all inputs from stdin are strings, so you will need to convert the string to an int first
# Before you convert the number you need to check to ensure that it is a numeric string
    # To do so you can use the methods `.isdigit()` or `.isnumeric()`
    # This will return true if every digit in your string is a numerical character
    # However, that means a string such as `-1` would return false, even though your program should accept negative values
    # This means you will need to have a check to see if `-` is first character of the string before you check if it is numerical
    # If it is in the string you will need to remove the `-` character, and know that it will be a negative number, so a subtraction from the overall sum
    # I recommend checking out: https://www.w3schools.com/python/ref_string_replace.asp to figure out how one may remove a character from a string
# All this together means you will have an intensive while loop that includes multiple if statements, likely with some nesting 
# The sum should start at 0 

def user_adder():
    adder=0
    ans=""
    while(ans!="exit"):
        ans=input("Enter a number to add or exit: ")
        if(ans.isalpha()==False):
            adder += int(ans)
        else:
            ans=ans.lower()
    print("*"*32)
    return(adder)


num_sum = user_adder() 

print(f"Your final sum is {num_sum}")

print("*"*75)
# Now you will be creating a two operand calculator
# It will support the following operators: +,-,/,*,% 
# So accepted input is of the form `operand operator operand` 
# You can assume that the user is competent and will only input strings of that form 
# You will again need to verify that the operands are numerical values
# For this assume only positive integers will be entered, no need look for negative numbers 
# You will need to check the string for which operator it contains
# Once you do, you will need to remove the operands from the string
# This can be done in multiple ways:
    # You can go through the string in a loop and create a substring of the characters until an operator is reached
        # Upon reaching the operator you will switch to another substring and add all characters following to the second new string 
    # Alternatively you can use the `.split()` method to split the string around an operator: https://www.w3schools.com/python/ref_string_split.asp
# Your program will need to work with whatever spacing is given  
    # So, it should function the same for `5 + 6` as `5+6`
# Print the result of the equation
# Again, loop through prompting the user for input until `exit` in any casing is input 

def calc(v1,oper,v2):
    if(oper=="+"):
        return(v1+v2)
    elif(oper=="-"):
        return(v1-v2)
    elif(oper=="/"):
        if(v2!=0):
            return(v1/v2)
        else:
            return("You can not divide by zero.")
    elif(oper=="*"):
        return(v1*v2)
    elif(oper=="%"):
        return(v1%v2)
    else:
        return("That is not a proper equation.")


def user_calc():
    val1=""
    val2=""
    oper=""
    ans=""
    move=False
    print("*"*32)
    while(ans!="exit"):
        ans=input("Enter a equation(1+2, 4 / 12, etc.) using +,-,/,*, or remainder or exit: ")
        if(ans.lower()=="exit"):
            return()
        else:
            ans=ans.replace(" ","")
            ans=str(ans)
            ans=list(ans)
            for char in ans:
                if(char.isdigit()==True and move==False):
                    val1+=char
                elif(char.isdigit()==True and move==True):
                    val2+=char
                else:
                    oper=char
                    move=True
            val1=int(val1)
            val2=int(val2)
        print(calc(val1,oper,val2))
        print("*"*32)
        val1=""
        val2=""
        oper=""

user_calc()

        