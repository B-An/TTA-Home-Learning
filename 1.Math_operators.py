#Task 1:	Calculator

#Write a program that allows user to enter two numbers, and operator and then completes the calculation.


#Follow the instructions below:

#1.	1. Ask the user to pick a number
#2.	2. Ask the user to pick a second number
#3.	3. Ask the user to pick an operator
#4.	4. Create an IF statement to carry out the math operation using the users choice of numbers and choice of operator

#1. Pick first number
number_1 = int(input("Please choose a number: "))

#2. Pick second number
number_2 = int(input("Please choose another number: "))

#3. Please choose an operator to operate on these two numbers
op_sel = input("Please choose one operator from the +, -, *, /, ** etc. :  ")
print("More the full range Python operators, click here: https://www.w3schools.in/python/operators/")

#4. Create IF statement for selected numbers and op_sel
if (number_1 OR number_2 = 0):
    print("Please go back and choose non-zero integers. Thank you.")
else:
    print(number_1 op_sel num number_2) #not sure about this

if menu_option == 1:
    print(number1,"+",number2,"=",number1 + number2)
    elif menu_option == 2:
        print(number1,"-",number2,"=",number1 - number2) 
        elif menu_option == 3:
            print(number1,"*",number2,"=",number1 * number2)
            elif menu_option == 4:
                print(number1,"/",number2,"=",number1 / number2)
            elif menu_option == 5:
                print(number1,"squared =",number1 * number1)
                print(number2,"squared =",number2 * number2)
                elif menu_option == 6:
                    print(number1,"to power of",number2,"=",number1 ** number2)
                    else:
                        print("Invalid option selected")