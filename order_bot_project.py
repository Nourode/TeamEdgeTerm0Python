# -------------------------------------------- 

	# Yeou've just learned about variablconditionals, functions, and user input. 
	# You've also created a basic calculator in a previous project.
	
	# Now imagine you are going out to eat.
	# Are you at a restaurant for a meal? Are you grabbing boba? Or are you just going to an ice cream parlor?
	# At the end of the meal, you get the bill. 

	# How do you think restaurants automate that math?

					# Let's try it!

# -------------------------------------------- 

# Scenario Parameters: 

	# When you eat out, you have the option to order one or multiple items.
	# What kind of items are available to order? There's usually a menu.
	# Allow your user to order a drink, meal, and dessert.

	# At the end of the order, the receipt comes and you have to calculate the total cost:
	# Don't forget the tax and tip!

# After this program finishes running, it should output a receipt with:
        #1. the items you ordered and their cost 
	#2. a total for your order before tax
	#3. a total for your order after tax
	#4. the amount of your tip 
	#5. the total including tax and tip

# -------------------------------------------- 


# -------------------------------------------- 

# Part 1:
# Let's start by creating the variables we'll need to keep track of the user's order
# as well as TAX and tip

# Remember: Your user should be able to order at least 3 items (a drink, meal, and dessert item). 

# --------------------------------------------

from functools import total_ordering


print("MENU")
print("------")
print("Drinks")
print("1.coke		1.00$")
print("2.apple juice	1.00$")

print("Meals")
print("3.pizza	5.00$")
print("4.Taco	3.00$")
print("5.Rice		2.00$")

print("Desserts")
print("6. cupcakes 3.00$")
print("7. cake		1.00$")

print("Hi ! welcome to Restraunt")

user_drink = ""
drink_cost = 0
user_meal = ""
meal_cost = 0
user_dessert = ""
dessert_cost = 0
# -------------------------------------------- 

# Part 2:
# Next, let's display the menu. Include the food item name and it's cost. 

# Write a function that will display the menu:
# - Print each item available and it's cost. You should have at least 3 items available (a drink, meal, and dessert item). 

# --------------------------------------------






# -------------------------------------------- 

# Part 3:
# Let's take the order. What did the user order? What does it cost?
def order():
	global user_drink
	global drink_cost
	global user_meal 
	global meal_cost
	global user_dessert
	global dessert_cost 


	drink = input("what would you like to drink (enter 1 or 2): ")
	if drink == "1": 
		user_drink = "coke" 
		drink_cost = 1
	else:
		user_drink = "apple juice"
		drink_cost = 1
	meal = input("what would you like to eat")
	if meal == "3":
		user_meal = "pizza"
		meal_cost = 5
	elif meal == "4" :
		user_meal = "taco"
		meal_cost = 3
	elif meal == "5":
		user_meal = "rice"
		meal_cost = 3
    
	dessert = input ("what would you like for dessert" )
	if dessert == "6":
		user_dessert = "cupcakes"
		dessert_cost = 3
	else:
		user_dessert = "cake"
		dessert_cost = 1

order ("Hi I would like a coke")	
order ("I would also like a taco")
order ("For dessert I would like a cake")
# Write a function that will take the order:
# - Prompt the user to enter a drink, dessert, and meal (Bonus: give them the option to not order an item)
# - Return the cost 

# Remember! Functions are meant to be reusable, so write a function that will work when called repeatedly!

# --------------------------------------------











# -------------------------------------------- 

# Part 4:
# Now that you have the costs of everything ordered, let's calculate the cost of the order(including tip and tax).

# Write a function that will calculate the cost of the order, including:
# - Cost of all  ordered items
# - Tax (Look up the sales tax of your city)
# - Tip (Give the user the option to enter how much they want to tip)

# Remember! Functions are meant to be reusable, so write a function that will work when called for each person!

# -------------------------------------------- 












# -------------------------------------------- 

# Part 5:
# Let's print out a receipt.

# Write a function that will take the values of the order and total cost and print it out in an appealing way.

# The receipt should include:
# - Cost of each item  
# - Tax for the order
# - Tip for the order
# - Total cost for the order


# -------------------------------------------- 
def receipt ():
	global user_drink
	global drink_cost
	global user_meal
	global meal_cost
	global user_dessert
	global dessert_cost 

	total = drink_cost + meal_cost + dessert_cost
	
	tip = input("would you like to leave a tip for the order")

	
   
      


   




# -------------------------------------------- 

# Part 6: Food Order Bot

# Call all of your functions to get your food order bot up and running!

# --------------------------------------------







# -------------------------------------------- 

# Part 7: Upchallenges!

# How many of these upchallenges can you implement?

# - Make sure the user is only entering valid values. If they enter an invalid value, prompt them to re-enter. 
# - The displayed prices should only have two decimal places.
# - Implement a rewards system (stamp cards, buy one get one, etc)

# --------------------------------------------
