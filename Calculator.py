#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      HP 15
#
# Created:     07-07-2022
# Copyright:   (c) HP 15 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Function for the addition of two numbers
def add(num1, num2):
    print(num1 + num2)


# Function for the subtraction of two numbers
def sub(num1, num2):
    print(num1 - num2)


# Function for the division of two numbers
def div(num1, num2):
    print(num1 / num2)


# Function for the multiplication of two numbers
def mul(num1, num2):
    print(num1 * num2)


# Function for power of a number
def pow(num1, num2):
    print(num1**num2)


while True:

    # Printing a formatted menu for the calculator
    print("\t\t     WELCOME TO NEHA'S BASIC CALCULATOR")
    print('\t MENU:')
    print('\t 1:ADDITION OF TWO NUMBERS')
    print('\t 2:SUBTRACTION OF TWO NUMBERS')
    print('\t 3:DIVISION OF TWO NUMBERS')
    print('\t 4:MULTIPLICATION OF TWO NUMBERS')
    print('\t 5:POWER OF A NUMBER (FIRST^SECOND)')

    # Take input from the user
    choice = input("Enter choices between 1 to 5 ")

    print("Enter Two Numbers:")
    num1= int(input('Enter First Number:'))
    num2= int(input('Enter Second Number:'))

    # If choice is one then the add function will be called

    if choice == '1':
        add(num1,num2)

    # If choice is two then the sub function will be called

    elif choice == '2':
        sub(num1,num2)

    # If choice is three then the div function will be called

    elif choice =='3':
        div(num1,num2)

    # If choice is four then the mul function will be called

    elif choice =='4':
        mul(num1,num2)

    # If choice is five then the power function will be called

    elif choice =='5':
        pow(num1,num2)

    # If choice does not lies between 1 and 5 then there is an error message

    else:
        print(" Wrong Input ")

    print("Want to calculate more? ")

    d = input('yes or no')

    if d.lower()=='yes' or d.upper()=='yes' :
        continue;
    else:
        break;


