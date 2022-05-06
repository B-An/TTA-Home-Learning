#Task 4:	Lists

#Create 3 different programs to practice using lists.

#1.	Creates a list of three fruits:
#o	Outputs all the fruits in the list
#o	Outputs the second fruit in the list
#2.	Creates a set of three fruits:
#o	Outputs all the fruits in the set
#o	Adds a new fruit to the set
#o	Outputs all the fruits in the set
#o	Tries to add a repeat of a fruit to the set
#o	Outputs all the fruits in the set
#3.	Creates a dictionary of three fruits with a corresponding price:
#o	Outputs all the fruits in the dictionary
#o	Outputs the price of the second fruit in the dictionary
#o	For a given fruit output its price if it is the dictionary or a message if it is not

#1. fruit list (create list of three fruits)
fruits = ("apple", "pears", "durian")

#1a. Outputs all the fruits in the list
print(fruits)

#1b. Outputs the second fruit in the list
print(fruits [1])

#2. Creates a set of three fruits
fruit_set = {"oranges", "cherries", "blueberries"}

#2a. Outputs all the fruits in the set
print(fruit_set)

#2b. Adds a new fruit to the set
fruit_set.add("bananas")

#2c. Outputs all the fruits in the set
print(fruit_set)

#2d. Tries to add a repeat of a fruit to the set
fruit_set.add("cherries")

#2e. Outputs all the fruits in the set
print(fruit_set)

#3. 3.	Creates a dictionary of three fruits with a corresponding price:
fruit_price_index = {"apples": "£1.80", "blueberries": "£3.50", "grapefruits": "£2.80"}

#3a. Outputs all the fruits in the dictionary
print(fruit_price_index)

#3b. Outputs the price of the second fruit in the dictionary
print(fruit_price_index["blueberries"])

#3c. For a given fruit output its price if it is in the dictionary or a message if it is not
fruit_selector = input("Input a fruit of choice and its price will be given to you: ")
if fruit_selector == "apples" or "apple": #variable entry names offered
    print(fruit_price_index["apples"])
elif fruit_price_index == "blueberries" or "blueberry":
    print(fruit_price_index["blueberries"])
elif fruit_price_index == "grapefruits" or "grapefruits":
    print(fruit_price_index["grapefruits"])
else:
    print("This is not in the fruit dictionary. Please choose again")
