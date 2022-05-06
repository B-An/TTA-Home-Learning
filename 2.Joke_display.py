#Task 2: Joke Display

#Write a program that asks a user for their favourite number between 1 and 100 and then tells them a joke based on the number. You should use a minimum of 3 jokes

#https://www.w3schools.com/python/ref_func_input.asp 

#Follow the instructions below:

#1.	Ask the user to pick a number and store against variable
#2.	Create an IF statement which uses logical operators which prints out a joke based on the number the user picked 

num_sel = int(input("Please choose a number between 1 and 10): "))

if num_sel <= 5:
    print("What’s the best thing about Switzerland? \nI don’t know, but the flag is a big plus.")
elif num_sel <= 10 or > 5:
    print("Did you hear about the mathematician who’s afraid of negative numbers?\nHe’ll stop at nothing to avoid them.")
else:
    print("Please a number within the range. Thank you.")