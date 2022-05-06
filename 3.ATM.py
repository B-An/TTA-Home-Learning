#Task 3: ATM

#Write a program that simulates the behaviour of a basic ATM. 

#Follow the instructions below:

#1.	Print a main menu:
#Welcome to Northern Frock
#2.	1 - Display balance
#3.	2 - Withdraw funds
#4.	3 - Deposit funds
#5.	9 - Return card
#Enter an option:
#6.	If ‘1’ is entered, display the current balance and the maximum amount available for withdrawal (must be a multiple of £10), and return to main menu.
#7.	If ‘2’ is entered, print a sub-menu with withdrawal amounts of:
#Please select withdrawal amount
#8.	1 - £10
#9.	2 - £20
#10.	3 - £40
#11.	4 - £60
#12.	5 - £80
#13.	6 - £100
#14.	7 - Other amount
#15.	8 - Return to main menu
#Enter an option:
#a.	If ‘1 to 6’’ is selected check that the requested withdrawal is allowed, print a message to show that the money has been withdrawn, calculate the new balance and return to main menu.
#b.	If ‘7’ is selected, then prompt the user for an integer value. Check this number is a multiple of 10 and that the withdrawal is permitted, print a message to show that the money has been withdrawn, calculate the new balance and return to main menu.
#c.	If ‘8’ is selected return to main menu.
#16.	If ‘3’ is entered, provide another menu that will allow the user to enter an amount to deposit (does not need to be a multiple of £10), return to main menu or return card. If funds are deposited, provide appropriate feedback and update the balance and return to main menu.
#17.	If ‘9’ is entered, print a goodbye message and exit (break).
#18.	If another value is entered, print an error message and print the menu again.

#1.	Establish initial balance and maximum withdrawal amount:
balance = 2500
max_with = 1780

#menu lists (tuples)
main_options = ["1 - Display balance", "2 - Withdraw funds", "3 - Deposit funds", "9 - Return card"]
sub_menu_options = ["1 - £10", "2 - £20", "3 - £40", "4 - £60", "5 - £80", "6 - £100", "7 - Other amount", "8 - Return to main menu"]

#menu user-interface
main_menu = int(input("Welcome to Northern Frock \n1 - Display balance\n2 - Withdraw funds\n3 - Deposit funds\n9 - Return card\nEnter an option: "))
sub_menu = int(input("Please select withdrawal amount\n8.	1 - £10\n9.	2 - £20\n10.	3 - £40\n11.	4 - £60\n12.	5 - £80\n13.	6 - £100\n14.	7 - Other amount\n15.	8 - Return to main menu\nEnter an option: "))
deposit_menu = int(input("Please enter a deposit amount (integer values only): "))

#define declared integer for withdrawal
x = int(input("Please input the amount you wish to withdraw: "))

if main_menu == 1:
    print('balance')
elif main_menu == 2:
    sub_menu == 1 and ['max_with'] >= 10:
        print("£10 has been withdrawn. You new balance is now" 'balance'-10 "You will now be returned to the main menu")
    elif sub_menu == 2 and ['max_with'] >= 20:
        print("£20 has been withdrawn. You new balance is now" 'balance'-20 "You will now be returned to the main menu")
    elif sub_menu == 3 and ['max_with'] >= 40:
        print("£40 has been withdrawn. You new balance is now" 'balance'-40 "You will now be returned to the main menu")
    elif sub_menu == 4 and ['max_with'] >= 60:
        print("£40 has been withdrawn. You new balance is now" 'balance'-60 "You will now be returned to the main menu")
    elif sub_menu == 5 and ['max_with'] >= 80:
        print("£40 has been withdrawn. You new balance is now" 'balance'-80 "You will now be returned to the main menu")
    elif sub_menu == 6 and ['max_with'] >= 100:
        print("£40 has been withdrawn. You new balance is now" 'balance'-100 "You will now be returned to the main menu")
    elif sub_menu == 7:
        if (int(x) >= 0) and (x % 10 = 0) AND (['max_with'] >= 0):
            print(x "has been withdrawn. You new balance is now" 'balance'-int(x) "You will now be returned to the main menu")
        else:
            print("Please enter an integer value to withdraw: ")
    elif sub_menu == 8:
        print("Welcome back to Northern Frock \n1 - Display balance\n2 - Withdraw funds\n3 - Deposit funds\n9 - Return card\nEnter an option: ")
    else:
        print(main_menu)
elif main_menu == 3:
    deposit_menu > 0 and ['max_with'] >= 0:
    print(deposit_menu "has been withdrawn. You new balance is now" 'balance'-deposit_menu "You will now be returned to the main menu"):
    'balance' = 'balance' + deposit_menu
    print("This is your new 'balance'"),
    print(main_menu)
elif main_menu == 9:
    print("Thank you for your custom and goodbye for now. We look forward to having you with us again")
    break
else:
    print("Error! You will be returned to the main menu"),
    print(main_menu)