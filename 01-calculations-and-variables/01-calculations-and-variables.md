
## 1. Variables

**Variables** are like little storage containers or boxes for information. You give them a name, and you can put different types of information inside, like numbers, words, or a list of things. You can also change what's in the box later.

**Example Code:**


```python 
# A variable to store a number
player_score = 100
print(f"The player's score is: {player_score}")

# A variable to store a word (text)
favorite_fruit = "apple"
print(f"The favorite fruit is: {favorite_fruit}")

# A variable to store a decimal number
price = 9.99
print(f"The price is: {price}")

# You can change the value of a variable
player_score = 150
print(f"The new score is: {player_score}")

# You can also use one variable to update another
high_score = player_score
print(f"The high score is now: {high_score}")
```

### The `print()` Function: Talking to Your Computer 💬

The `print()` function is one of the most useful tools in Python. It's how you tell the computer to display a message or show you the value of something. Think of it as Python's way of "speaking" back to you.

You use `print()` by typing the word `print`, followed by parentheses `()`. Whatever you want the computer to say goes inside those parentheses.

#### Scenario 1: Printing Simple Text and Numbers

To print a simple message, you put the text inside single (`' '`) or double (`" "`) quotes. For numbers, you just write the number.

**Example Code:**

```python
# Printing a simple message
print("Hello, Python!")

# Printing a number
print(100)

# Printing a more complex message
print("The sun is shining today.")
```

#### Scenario 2: Printing Variables

The real power of `print()` comes when you use it with **variables**. It allows you to see what information is currently stored in your variables.

**Example Code:**

```python
# First, we create a variable
player_name = "PixelPlank"
high_score = 5000

# Now, we print the value of the variables
print(player_name)
print(high_score)

# We can also print them with explanatory text
print("The current player is:")
print(player_name)
```

#### Scenario 3: Printing Multiple Items

You don't have to use a separate `print()` statement for every single thing. You can print multiple pieces of information on the same line by separating them with a **comma** `,`. Python will automatically add a space between them.

**Example Code:**

```python
# Printing a mix of text and a variable's value
player_name = "ShadowRunner"
print("The player's name is", player_name)

# Printing multiple variables
level = 5
experience = 250
print("Level:", level, "XP:", experience)
```

#### Scenario 4: Using f-strings (Formatted String Literals)

**f-strings** are a modern and super-easy way to combine text and variables. They let you put your variable's name directly inside a string.

To create an f-string, you just put the letter `f` right before the opening quote. Then, you can place your variable names inside curly braces `{}` within the string.

This is the method which most useful for us when we write programs, and it's a very popular way to format text in Python.

**Example Code:**

```python
# Let's use f-strings to print a variable with text
hero_name = "Captain Comet"
print(f"Our hero is named {hero_name}!")

# This makes printing multiple variables very clean
level = 10
gold = 75
print(f"You have reached level {level} and found {gold} gold coins!")
```


---

## 2. Basic Operators (Addition, Subtraction, Multiplication, Division)

Operators are symbols that tell Python to perform a calculation. We'll use them to do basic math.

- `+` is for **addition**. It adds two numbers together.
    
- `-` is for **subtraction**. It finds the difference between two numbers.
    
- `*` is for **multiplication**. It multiplies two numbers.
    
- `/` is for **division**. It divides one number by another.
    

**Example Code:**


```python
# Addition
cookies = 5
new_cookies = 3
total_cookies = cookies + new_cookies
print(f"You started with 5 cookies and got 3 more. You now have {total_cookies} cookies.")

# Subtraction
money = 20
cost = 7
money_left = money - cost
print(f"You had $20 and spent $7. You have ${money_left} left.")

# Multiplication
pizzas = 4
slices_per_pizza = 2
total_slices = pizzas * slices_per_pizza
print(f"There are 4 pizzas with 2 slices each. That's {total_slices} slices in total.")

# Division
friends = 12
people = 3
slices_per_person = friends / people
print(f"If you have 12 slices and share with 3 people, each person gets {slices_per_person} slices.")

# You can also combine them
total_cost = 5 + 2 * 3
print(f"The total cost is: {total_cost}")
```

---

## 3. Advanced Operators (Modulo, Exponentiation, Floor Division)

Python has some other useful operators:

- `**` is for **exponentiation**, which means "to the power of." For example, `2 ** 3` is 2 * 2 * 2.
    
- `//` is for **floor division**. It divides two numbers but throws away any remainder, giving you only the whole number part.
    
- `%` is the **modulo operator**. It gives you the _remainder_ after a division.
    

**Example Code:**


```python
# Exponentiation (3 to the power of 2)
result_power = 3 ** 2
print(f"3 squared is: {result_power}")

# Floor Division (dividing 17 by 5, but ignoring the remainder)
floors = 17 // 5
print(f"17 divided by 5 is: {floors}")

# Modulo (what is the remainder when 17 is divided by 5?)
remainder = 17 % 5
print(f"The remainder is: {remainder}")

# Another floor division example
blocks_per_row = 20 // 6
print(f"You can make {blocks_per_row} full rows.")

# Another modulo example
leftover_items = 15 % 4
print(f"There are {leftover_items} items left over.")

# Combining advanced operators
complicated_calc = 2 ** 4 // 3
print(f"A complicated calculation: {complicated_calc}")
```

---

## 4. Order of Operations (PEMDAS/BODMAS)

Just like in math class, Python follows a specific order when it sees multiple operators in one line. You can remember it with PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction) or BODMAS (Brackets, Orders, Division and Multiplication, Addition and Subtraction). Operations inside parentheses `()` are always done first.

**Example Code:**


```python
# Without parentheses, multiplication happens first
result1 = 5 + 2 * 3
print(f"Result without parentheses: {result1}")

# With parentheses, the addition happens first
result2 = (5 + 2) * 3
print(f"Result with parentheses: {result2}")

# A more complex example
result3 = 10 - 2 ** 3 + 4 * 2
print(f"A complex result: {result3}")

# Another example with parentheses
result4 = (10 - 2) ** 3 / 4
print(f"Another complex result: {result4}")

# An example with multiple types of operators
final_score = (5 * 2 + 10) / 2
print(f"Your final score is: {final_score}")
```

---

## Hands-On Exercises  

Now, with those explanations and examples in mind, here are the 40 story-based questions for you to practice. 

### 1. Variables 🧑‍💻

1. **The Magical Backpack:** "You're a wizard heading to a new school. Your magical backpack can hold a few things. Let's store the number of magic wands you have. Create a variable called `wands` and set it to `3`. Then, print the value of `wands`." 🪄
    
2. **Counting Treasure:** "You've just found a pirate's treasure chest! Inside, there are 10 gold coins. Create a variable named `gold_coins` and set it to `10`. Now, print out the number of coins." 💰
    
3. **Naming Your Dragon:** "You've hatched a baby dragon! You want to remember its name. Create a variable called `dragon_name` and set it to the text `'Spitfire'`. Print the value of `dragon_name`." 🐉
    
4. **Tracking Your Score:** "You're playing a video game and your current score is 500. Create a variable `score` and assign it the value `500`. Then, print your `score`." 🎮
    
5. **Changing Your Health:** "You're a knight with 100 health points. Create a variable `health` and set it to `100`. Now, you get hit and lose 20 health. Update the `health` variable to be the new value. Print your final `health`." ❤️
    
6. **Saving Your Name:** "You are designing a user login for a game. The user's name is 'PixelPlank'. Store this name in a variable called `player_name` and print it to the screen." 👾
    
7. **Counting Cats:** "You are a cat-sitter. You have to keep track of how many cats you're looking after. Create a variable `cat_count` and set it to `5`. Print the `cat_count`." 🐈
    
8. **The Daily High Temperature:** "You are a weather reporter. The high temperature for today is 25 degrees Celsius. Store this value in a variable named `high_temp`. Print the value of `high_temp`." ☀️
    
9. **Your Age:** "You want to store your age in a variable. Create a variable called `age` and set it to your age (e.g., `14`). Then, print the value of `age`." 🎂
    
10. **Tallying Laps:** "You are running laps around a track. You have completed 3 laps so far. Create a variable `laps_completed` and set it to `3`. Later, you run 2 more laps. Update the `laps_completed` variable and print its new value." 🏃
    

---

### 2. Basic Operators (Addition, Subtraction, Multiplication, Division) ➕➖✖️➗

1. **Sharing Pizza:** "You and your friends ordered 2 large pizzas. Each pizza has 8 slices. Create a variable `total_slices` and use multiplication to find the total number of slices. Print the result." 🍕
    
2. **Collecting Gems:** "You found 5 blue gems and 7 red gems. Create a variable `blue_gems` and set it to `5`. Create another variable `red_gems` and set it to `7`. Then, create a third variable `total_gems` and use addition to find the total. Print the `total_gems`." 💎
    
3. **Selling Cookies:** "You baked 24 cookies. Your friends ate 8 of them. Use subtraction to figure out how many cookies you have left. Store the remaining cookies in a variable called `cookies_left` and print it." 🍪
    
4. **Dividing Toys:** "You have 15 toy robots to share equally among your 3 friends. Use division to find out how many robots each friend gets. Store the result in a variable called `robots_per_friend` and print it." 🤖
    
5. **Shopping Spree:** "You have $100. You buy a book for $20 and a comic for $10. Create a variable `money` with the starting amount. Use subtraction to calculate how much money you have left after buying both items. Print the final amount." 🛍️
    
6. **Trip Planning:** "You need to drive 120 kilometers to get to the beach. You've already driven 50 kilometers. Use subtraction to find out how many kilometers you have left to drive. Store the result in a variable `km_left` and print it." 🚗
    
7. **Feeding the Dragons:** "You have 4 baby dragons. Each dragon eats 2 fish a day. Use multiplication to calculate the total number of fish you need per day. Store the result in a variable called `daily_fish_needed` and print it." 🐉🐟
    
8. **Sharing a Cake:** "A birthday cake has 12 pieces. You want to share it among 4 people. Use division to find out how many pieces each person gets. Store the result in a variable `cake_pieces_per_person` and print it." 🎂
    
9. **Collecting Stickers:** "You have 15 stickers. You get 5 more stickers from a friend and buy 10 stickers. Use addition to find out how many stickers you have in total. Store the result in `total_stickers` and print it." ✨
    
10. **Calculating a Discount:** "A new video game costs $60. There's a $15 discount. Use subtraction to find the final price. Store the result in `final_price` and print it." 🎮
    

---

### 3. Advanced Operators (Modulo, Exponentiation, Floor Division) ➗➕🧑‍🎓

1. **Sharing Leftovers:** "You have 17 pieces of candy to share with 4 friends. You want to give each friend an equal number of candies. Use the **modulo operator (`%`)** to find out how many candies are left over after you've given everyone their share. Store the result in `leftover_candy` and print it." 🍬
    
2. **Building a Tower:** "You're building a LEGO tower. The base is 3 blocks wide. If you want to make a square base, how many blocks do you need in total for the first layer? Use the **exponentiation operator (`**`)** to calculate 3 squared (3 to the power of 2). Store the result in a variable called `base_blocks` and print it." 🧱
    
3. **Packing Apples:** "You have 25 apples and you can fit 6 apples in each basket. Use **floor division (`//`)**to find out how many full baskets of apples you can pack. Store the result in a variable `full_baskets` and print it." 🍎
    
4. **Counting Weeks:** "There are 30 days in a month. Use **floor division (`//`)** to find out how many full weeks are in that month. Store the result in `full_weeks` and print it." 🗓️
    
5. **The Box of Cookies:** "You have 25 cookies. You can fit 5 cookies in a box. Use the **modulo operator (`%`)** to check if there will be any cookies left over after you fill all the boxes. Store the result in `leftover_cookies` and print it." 🍪
    
6. **Calculating Cube Volume:** "A cube has a side length of 4 cm. Use the **exponentiation operator (`**`)** to calculate the volume of the cube (side length cubed, or 4 to the power of 3). Store the result in `cube_volume` and print it." 📦
    
7. **Group Division:** "You have 35 students in a class. You need to divide them into groups of 8. Use **floor division (`//`)** to find out how many full groups you can form. Store the result in `full_groups` and print it." 🏫
    
8. **Finding Remainder:** "You have 50 marbles. You want to arrange them in rows of 9. Use the **modulo operator (`%`)** to find out how many marbles will be left over after you've made as many full rows as possible. Store the result in `remainder_marbles` and print it." 🔴
    
9. **Powering Up:** "A super robot's strength is calculated as 5 to the power of 4. Use the **exponentiation operator (`**`)** to find its strength. Store the result in a variable called `robot_strength` and print it." 🤖
    
10. **The Final Score:** "In a game, your score is based on the number of full rounds you've completed. You have a score of 120 points, and each round is worth 25 points. Use **floor division (`//`)** to find out how many full rounds you've completed. Store the result in `rounds_completed` and print it." 🎮
    

---

### 4. Order of Operations (PEMDAS/BODMAS) 🔢

1. **The Treasure Hunt:** "You're on a treasure hunt. The final clue is `5 + 2 * 3`. What number should you look for? Calculate the result using the correct order of operations. Store the answer in a variable called `final_number` and print it." 🗺️
    
2. **Scoring a Goal:** "In a soccer game, you scored 3 goals worth 2 points each, and 1 goal worth 5 points. To find your total score, you need to calculate `3 * 2 + 5`. What's your total score? Store the total in `total_score` and print it." ⚽
    
3. **Sharing Cookies (Again):** "You baked 3 dozen cookies (a dozen is 12) and then your mom gave you 5 more. You want to share them equally among your 4 friends. To find out how many each friend gets, you need to calculate `(3 * 12 + 5) / 4`. What's the result? Store the answer in `cookies_per_friend` and print it." 🍪
    
4. **The Super-Sized Potion:** "You're making a big potion. The formula is `10 + 2 ** 3 - 4`. What is the result? Make sure you follow the order of operations. Store the result in `potion_amount` and print it." ✨
    
5. **The Grand Adventure:** "You're planning a grand adventure. You have 2 bags, and each bag can hold 5 snacks. You also have 3 extra snacks. How many snacks do you have in total? The calculation is `2 * 5 + 3`. What's the total? Store it in `total_snacks` and print it." 🎒
    
6. **Calculating a Grade:** "Your final grade is calculated by taking your test score (80) and adding half of your project score (100). The formula is `80 + 100 / 2`. What is your final grade? Store the result in `final_grade` and print it." 💯
    
7. **The Magic Spell:** "A magic spell's power is calculated using the formula `4 * (5 + 3)`. What is the total power? Remember to do the calculation inside the parentheses first. Store the result in `spell_power` and print it." 🧙
    
8. **Mixing Potions:** "You are mixing potions. You have 3 vials with 10 ml each, and you add 2 vials with 5 ml each. The formula is `3 * 10 + 2 * 5`. What is the total amount of potion? Store the total in `total_potion`and print it." ⚗️
    
9. **Building a Skyscraper:** "A skyscraper is 50 floors tall. Each floor is 3 meters high. There is a 5-meter antenna on top. To find the total height, you need to calculate `50 * 3 + 5`. What is the total height? Store the result in `total_height` and print it." 🏙️
    
10. **The Final Race:** "You are in a race. You run 5 laps, and each lap is 2 kilometers. You then walk an extra 1 kilometer. To find the total distance, you need to calculate `5 * 2 + 1`. What's the total distance? Store it in `total_distance` and print it." 🏃



