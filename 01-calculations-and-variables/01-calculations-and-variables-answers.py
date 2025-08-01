# ==============================================================================
# SOLUTIONS FOR HANDS-ON EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 40 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: Variables 🧑‍💻
# ------------------------------------------------------------------------------

# Question 1: The Magical Backpack
# Thought Process: The question asks us to create a variable named 'wands'
# and store the number 3 in it. After that, we need to print the value
# that is inside the 'wands' variable.
wands = 3
print(f"I have {wands} magic wands.")

# Question 2: Counting Treasure
# Thought Process: We need to create a variable called 'gold_coins'
# and give it a value of 10. Then, we print the value of that variable
# to show how many coins we found.
gold_coins = 10
print(f"I found {gold_coins} gold coins.")

# Question 3: Naming Your Dragon
# Thought Process: The name of the dragon is a word, so we need to use
# a string. We create a variable 'dragon_name' and put the text 'Spitfire'
# inside of it, using single or double quotes. Finally, we print the name.
dragon_name = 'Spitfire'
print(f"My dragon's name is {dragon_name}.")

# Question 4: Tracking Your Score
# Thought Process: The current score is 500. We create a variable 'score'
# to hold this number. Then, we print the variable to display the score.
score = 500
print(f"My current score is {score}.")

# Question 5: Changing Your Health
# Thought Process: First, we set the initial health to 100. Then, the
# problem states we lose 20 health. To update the 'health' variable, we
# subtract 20 from its current value. Finally, we print the new value.
health = 100
health = health - 20
print(f"My final health is {health}.")

# Question 6: Saving Your Name
# Thought Process: The user's name is 'PixelPlank', which is text.
# We create a variable 'player_name' and store the text as a string.
# Then, we print the value of the variable.
player_name = 'PixelPlank'
print(f"The player's name is {player_name}.")

# Question 7: Counting Cats
# Thought Process: We need to keep track of a number, so we use a variable
# 'cat_count' and assign it the number 5. Then, we print the variable.
cat_count = 5
print(f"I am looking after {cat_count} cats.")

# Question 8: The Daily High Temperature
# Thought Process: The temperature is a number, 25. We create a variable
# 'high_temp' and set it to 25. Then, we print the variable's value.
high_temp = 25
print(f"The high temperature for today is {high_temp} degrees Celsius.")

# Question 9: Your Age
# Thought Process: This is a simple variable assignment. We create a variable
# 'age' and store a number in it (for this example, 14). Then, we print the variable.
age = 14
print(f"My age is {age}.")

# Question 10: Tallying Laps
# Thought Process: We start with a variable 'laps_completed' set to 3.
# We then need to add 2 more laps. To do this, we can take the current
# value of 'laps_completed' and add 2 to it, and then store the new
# total back into the same variable. Finally, we print the updated value.
laps_completed = 3
laps_completed = laps_completed + 2
print(f"I have now completed {laps_completed} laps.")


# ------------------------------------------------------------------------------
# Section 2: Basic Operators (Addition, Subtraction, Multiplication, Division) ➕➖✖️➗
# ------------------------------------------------------------------------------

# Question 1: Sharing Pizza
# Thought Process: We have 2 pizzas with 8 slices each. To find the total,
# we need to multiply 2 by 8. We store the result in a variable and print it.
total_slices = 2 * 8
print(f"The total number of pizza slices is {total_slices}.")

# Question 2: Collecting Gems
# Thought Process: We need to add the number of blue gems and red gems.
# First, we store each count in its own variable. Then, we add the two
# variables together and store the result in a new variable.
blue_gems = 5
red_gems = 7
total_gems = blue_gems + red_gems
print(f"The total number of gems is {total_gems}.")

# Question 3: Selling Cookies
# Thought Process: We start with 24 cookies and 8 are eaten. To find out
# how many are left, we subtract 8 from 24. We store the result and print it.
cookies_left = 24 - 8
print(f"There are {cookies_left} cookies left.")

# Question 4: Dividing Toys
# Thought Process: We have 15 robots to be shared equally among 3 friends.
# To find out how many each friend gets, we need to divide 15 by 3.
robots_per_friend = 15 / 3
print(f"Each friend gets {robots_per_friend} robots.")

# Question 5: Shopping Spree
# Thought Process: We start with $100. We need to subtract the cost of the
# book ($20) and the comic ($10) from the initial amount.
money = 100
money_left = money - 20 - 10
print(f"I have ${money_left} left after my shopping spree.")

# Question 6: Trip Planning
# Thought Process: The total distance is 120 km and we've driven 50 km.
# To find the remaining distance, we subtract 50 from 120.
km_left = 120 - 50
print(f"I have {km_left} kilometers left to drive.")

# Question 7: Feeding the Dragons
# Thought Process: We have 4 dragons and each eats 2 fish. To find the total
# number of fish, we multiply the number of dragons by the number of fish
# per dragon.
daily_fish_needed = 4 * 2
print(f"We need {daily_fish_needed} fish per day.")

# Question 8: Sharing a Cake
# Thought Process: A cake has 12 pieces and is being shared by 4 people.
# To find out how many pieces each person gets, we divide 12 by 4.
cake_pieces_per_person = 12 / 4
print(f"Each person gets {cake_pieces_per_person} pieces of cake.")

# Question 9: Collecting Stickers
# Thought Process: We start with 15 stickers, get 5 more, and buy 10.
# To find the total, we add all these numbers together.
total_stickers = 15 + 5 + 10
print(f"I have a total of {total_stickers} stickers.")

# Question 10: Calculating a Discount
# Thought Process: The game costs $60 and there's a $15 discount.
# To find the final price, we subtract the discount from the original price.
final_price = 60 - 15
print(f"The final price of the video game is ${final_price}.")


# ------------------------------------------------------------------------------
# Section 3: Advanced Operators (Modulo, Exponentiation, Floor Division) ➗➕🧑‍🎓
# ------------------------------------------------------------------------------

# Question 1: Sharing Leftovers
# Thought Process: We have 17 candies to share with 4 friends. The modulo
# operator (%) is used to find the remainder of a division. We divide 17 by 4
# and get the remainder.
leftover_candy = 17 % 4
print(f"I have {leftover_candy} leftover candies.")

# Question 2: Building a Tower
# Thought Process: The base is a square with a side of 3 blocks. The number
# of blocks for the first layer is 3 squared (3 * 3). The exponentiation
# operator (**) is perfect for this.
base_blocks = 3 ** 2
print(f"The first layer of the tower needs {base_blocks} blocks.")

# Question 3: Packing Apples
# Thought Process: We have 25 apples and each basket holds 6. We want to
# know how many *full* baskets we can make. Floor division (//) gives
# us the whole number result of a division, ignoring the remainder.
full_baskets = 25 // 6
print(f"You can pack {full_baskets} full baskets of apples.")

# Question 4: Counting Weeks
# Thought Process: A month has 30 days and a week has 7. We want the number
# of *full* weeks, so we use floor division (//).
full_weeks = 30 // 7
print(f"There are {full_weeks} full weeks in the month.")

# Question 5: The Box of Cookies
# Thought Process: We have 25 cookies and can fit 5 in each box. We use the
# modulo operator (%) to find the remainder, which will tell us how many
# cookies are left over.
leftover_cookies = 25 % 5
print(f"There are {leftover_cookies} cookies left over.")

# Question 6: Calculating Cube Volume
# Thought Process: The volume of a cube is the side length cubed. The side
# length is 4 cm. We use the exponentiation operator (**) to calculate 4 to
# the power of 3.
cube_volume = 4 ** 3
print(f"The volume of the cube is {cube_volume} cm³.")

# Question 7: Group Division
# Thought Process: We have 35 students and need to form groups of 8. We
# want to know how many *full* groups are possible. Floor division (//)
# is the operator to use here.
full_groups = 35 // 8
print(f"You can form {full_groups} full groups of students.")

# Question 8: Finding Remainder
# Thought Process: We have 50 marbles to arrange in rows of 9. The modulo
# operator (%) will find the number of marbles left over after forming
# as many full rows as possible.
remainder_marbles = 50 % 9
print(f"There will be {remainder_marbles} marbles left over.")

# Question 9: Powering Up
# Thought Process: The robot's strength is 5 to the power of 4. We use the
# exponentiation operator (**) to calculate this.
robot_strength = 5 ** 4
print(f"The super robot's strength is {robot_strength}.")

# Question 10: The Final Score
# Thought Process: We want the number of *full* rounds completed, which
# means we need to perform floor division (//) of the total score (120)
# by the points per round (25).
rounds_completed = 120 // 25
print(f"You have completed {rounds_completed} full rounds.")


# ------------------------------------------------------------------------------
# Section 4: Order of Operations (PEMDAS/BODMAS) 🔢
# ------------------------------------------------------------------------------

# Question 1: The Treasure Hunt
# Thought Process: The problem is 5 + 2 * 3. According to PEMDAS, multiplication
# comes before addition. So, we first calculate 2 * 3, which is 6. Then we add 5.
# The final result is 5 + 6, which is 11.
final_number = 5 + 2 * 3
print(f"The final number you should look for is {final_number}.")

# Question 2: Scoring a Goal
# Thought Process: The problem is 3 * 2 + 5. Again, multiplication comes before
# addition. First, we calculate 3 * 2, which is 6. Then we add 5.
# The total score is 6 + 5, which is 11.
total_score = 3 * 2 + 5
print(f"Your total score is {total_score}.")

# Question 3: Sharing Cookies (Again)
# Thought Process: The formula is (3 * 12 + 5) / 4. Parentheses come first.
# Inside the parentheses, multiplication (3 * 12) is done before addition (+ 5).
# So, we do 3 * 12 = 36. Then 36 + 5 = 41. Finally, we divide by 4.
cookies_per_friend = (3 * 12 + 5) / 4
print(f"Each friend gets {cookies_per_friend} cookies.")

# Question 4: The Super-Sized Potion
# Thought Process: The formula is 10 + 2 ** 3 - 4. Exponents come first.
# So, we calculate 2 ** 3, which is 8. Then we perform addition and subtraction
# from left to right: 10 + 8 = 18, and then 18 - 4 = 14.
potion_amount = 10 + 2 ** 3 - 4
print(f"The potion amount is {potion_amount}.")

# Question 5: The Grand Adventure
# Thought Process: The calculation is 2 * 5 + 3. Multiplication comes first.
# So, we calculate 2 * 5 = 10. Then we add 3 to get 13.
total_snacks = 2 * 5 + 3
print(f"You have a total of {total_snacks} snacks.")

# Question 6: Calculating a Grade
# Thought Process: The formula is 80 + 100 / 2. Division comes before addition.
# So, we first calculate 100 / 2, which is 50. Then we add 80.
# The final grade is 80 + 50 = 130.
final_grade = 80 + 100 / 2
print(f"Your final grade is {final_grade}.")

# Question 7: The Magic Spell
# Thought Process: The formula is 4 * (5 + 3). Parentheses come first.
# We calculate 5 + 3, which is 8. Then we multiply that result by 4.
# The spell power is 4 * 8 = 32.
spell_power = 4 * (5 + 3)
print(f"The magic spell's total power is {spell_power}.")

# Question 8: Mixing Potions
# Thought Process: The formula is 3 * 10 + 2 * 5. Multiplication is done first,
# from left to right. So, 3 * 10 = 30 and 2 * 5 = 10. Then we add the
# results: 30 + 10 = 40.
total_potion = 3 * 10 + 2 * 5
print(f"The total amount of potion is {total_potion} ml.")

# Question 9: Building a Skyscraper
# Thought Process: The calculation is 50 * 3 + 5. Multiplication comes first.
# So, we calculate 50 * 3, which is 150. Then we add 5 to get 155.
total_height = 50 * 3 + 5
print(f"The total height of the skyscraper is {total_height} meters.")

# Question 10: The Final Race
# Thought Process: The calculation is 5 * 2 + 1. Multiplication comes first.
# So, we calculate 5 * 2, which is 10. Then we add 1 to get 11.
total_distance = 5 * 2 + 1
print(f"The total distance of the race is {total_distance} kilometers.")
