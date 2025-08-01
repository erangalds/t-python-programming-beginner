## Python Strings: Secret Codes and Messages 🕵️‍♀️

Welcome, Junior Agent! Your mission today is to learn about **strings** in Python. A string is just a fancy name for text—any sequence of letters, numbers, or symbols. In the world of secret agents, strings are our coded messages!

In Python, you create a string by putting text inside either single quotes (`'...'`) or double quotes (`"..."`).

## 1. What are Strings?

Strings are Python's way of handling text data. Think of a string as a sealed envelope containing a secret message. You need to create a variable to hold this message.

**Example Code:**

```python
# A secret message in a single-quote string
codename = 'Agent Alpha'
print(f"The agent's codename is: {codename}")

# Another message in a double-quote string
mission_details = "Meet at the coffee shop at 8 PM."
print(f"The mission details are: {mission_details}")

# A long message that can span multiple lines using triple quotes
mission_report = """Mission 007
Status: Complete
Target: Acquired"""
print(f"--- Mission Report ---\n{mission_report}")
```

## 2. Combining Strings (Concatenation)

Sometimes, you need to combine two different secret messages into one. This is called **string concatenation**, and you can do it using the `+` operator.

**Example Code:**

```python
# Combining two strings with the '+' operator
first_part = "Mission success: "
second_part = "Target acquired."
full_message = first_part + second_part
print(f"Full message: {full_message}")

# Combining variables and text
agent_rank = "007"
agent_name = "Bond"
greeting = "Hello, Agent " + agent_rank + " " + agent_name + "!"
print(greeting)

# Multiplying a string to repeat it
password_part = "pass"
full_password = password_part * 3
print(f"The password is: {full_password}")
```

## 3. String Indexing: Finding a Character's Position

Every letter in a string has a secret number, called an **index**, which tells you its position. Python starts counting at **zero**! The first character is at index `0`, the second is at index `1`, and so on. You can also use negative numbers to count from the end of the string, with `-1` being the last character.

**Example Code:**

```python
secret_word = "DECODED"
# D-E-C-O-D-E-D
# 0 1 2 3 4 5 6

# Access the first character (D)
first_letter = secret_word[0]
print(f"The first letter is: {first_letter}")

# Access the third character (C)
third_letter = secret_word[2]
print(f"The third letter is: {third_letter}")

# Access the last character using a negative index (D)
last_letter = secret_word[-1]
print(f"The last letter is: {last_letter}")

# Access the second-to-last character (E)
second_to_last = secret_word[-2]
print(f"The second-to-last letter is: {second_to_last}")
```

## 4. String Slicing: Grabbing a Piece of the String

Once you know about indexing, you can grab a whole chunk of a string. This is called **slicing**. You use a colon `:` inside the brackets to tell Python where to start and where to stop.

The syntax is `my_string[start:end]`. The slice includes the character at the `start` index but **does not include** the character at the `end` index. You can also specify a **step** with `my_string[start:end:step]`.

**Example Code:**

```python
# Let's get the word "CODE" out of a longer string
full_message = "ENCRYPT_CODE_MESSAGE"
# The word "CODE" starts at index 8 and ends just before index 12
secret_code = full_message[8:12]
print(f"The secret code is: {secret_code}")

# Slice from the beginning to a specific index (index 7)
first_part = full_message[:7]
print(f"The first part is: {first_part}")

# Slice from a specific index (index 13) to the end
last_part = full_message[13:]
print(f"The last part is: {last_part}")

# Grab every other letter using a step of 2
hidden_message = "S E C R E T"
every_other = hidden_message[::2]
print(f"The hidden message is: {every_other}")

# Get every third character, starting from the second character (index 1)
agent_list = "Agent_Alpha_Beta_Gamma"
third_letters = agent_list[1::3]
print(f"The third letters are: {third_letters}")

# Slice a specific range with a step
coordinates = "34.0522, -118.2437"

# This gets the numbers, skipping the comma and space
numbers_only = coordinates[2:17:3]
print(f"The coordinates numbers are: {numbers_only}")

# Using a negative step to reverse a string
password = "SECRET"
reversed_password = password[::-1]
print(f"The reversed password is: {reversed_password}")

# Grabbing a slice from the end of the string
full_report = "Mission Report 2025-08-01"
year = full_report[-10:-6]
print(f"The year of the report is: {year}")

# Slicing with a negative start and positive end index
coded_message = "DECODING_IN_PROGRESS"
slice_part = coded_message[-10:14]
print(f"The sliced part is: {slice_part}")
```

## 5. Essential String Methods

Strings in Python come with special built-in actions called **methods**. You can think of them as special tools to manipulate your secret messages. To use a method, you type the string variable's name, then a dot `.` followed by the method's name and parentheses `()`.

Here are a few useful methods:

| Method          | What it does                                                                    |
| --------------- | ------------------------------------------------------------------------------- |
| `len()`         | Finds the **length** of the string (how many characters it has).                |
| `.upper()`      | Converts the entire string to **UPPERCASE**.                                    |
| `.lower()`      | Converts the entire string to **lowercase**.                                    |
| `.strip()`      | Removes any extra spaces from the beginning and end of the string.              |
| `.replace()`    | **Replaces** a part of a string with something else.                            |
| `.find()`       | Finds the starting **index** of a character or substring.                       |
| `.isdigit()`    | Checks if the string contains **only numbers**. Returns `True` or `False`.      |
| `.split()`      | **Splits** a string into a list of smaller strings based on a separator.        |
| `.startswith()` | Checks if the string begins with a certain sequence. Returns `True` or `False`. |
| `.endswith()`   | Checks if the string ends with a certain sequence. Returns `True` or `False`.   |

```python
# Using len() to find the length
message = "Top Secret"
length = len(message)
print(f"The length of the message is: {length}") # Output: 10

# Using .upper() and .lower()
command = "execute now"
uppercase_command = command.upper()
print(f"Uppercase command: {uppercase_command}") # Output: EXECUTE NOW

shout = "FIRE IN THE HOLE"
lowercase_shout = shout.lower()
print(f"Lowercase shout: {lowercase_shout}") # Output: fire in the hole

# Using .strip() to clean up spaces
agent_id = " 007-J "
cleaned_id = agent_id.strip()
print(f"Cleaned agent ID: '{cleaned_id}'") # Output: '007-J'

# Using .replace() to substitute text
encoded_message = "agent_omega"
decoded_message = encoded_message.replace("omega", "alpha")
print(f"Decoded message: {decoded_message}") # Output: agent_alpha

# Using .find() to locate a substring
log_entry = "Log: Mission 007 - Success"
index_of_mission = log_entry.find("Mission")
print(f"The word 'Mission' starts at index: {index_of_mission}") # Output: 5

# Using .isdigit() to check for numbers
code1 = "42"
code2 = "A42"
print(f"'42' is all digits: {code1.isdigit()}") # Output: True
print(f"'A42' is all digits: {code2.isdigit()}") # Output: False

# Using .split() to break a string into a list
coordinates = "45.123, -78.456"
lat_long = coordinates.split(", ")
print(f"The coordinates are: {lat_long}") # Output: ['45.123', '-78.456']

# Using .startswith() and .endswith()
file_name = "secret_plan.pdf"
print(f"Does the file name start with 'secret'? {file_name.startswith('secret')}") # Output: True
print(f"Does the file name end with '.zip'? {file_name.endswith('.zip')}") # Output: False
```
## 6. Escape Sequences: Special Characters

Sometimes you need to include special characters in your messages, like a new line or a tab space. To do this, you use an **escape sequence**, which is a backslash `\` followed by a character.

**Example Code:**

```python
# Using \n for a new line
multi_line_message = "Urgent:\nMission successful."
print(multi_line_message)

# Using \t for a tab
tabbed_list = "Agent\tRank\tStatus\nBond\t007\tActive"
print(tabbed_list)

# Escaping a quote to use it inside a string
message_from_hq = "The general said, \"Report for duty!\""
print(message_from_hq)
```

## 7. Multiline Strings: The Extended Message

For long messages that span multiple lines, you can use **triple quotes** (`"""..."""` or `'''...'''`). The string will keep the formatting and line breaks exactly as you type them. This is especially useful for mission briefings, reports, or formatted text.

**Example Code:**

```python
# A report formatted over several lines
mission_report = """
Mission: Operation Nightfall
Date: 2024-05-15
Objective: Retrieve the encrypted data from the target location.
Status: Success. Data secured. All agents safe.
"""
print(mission_report)

# Using a multiline string for a poem or a log entry
secret_log = '''
Agent Log - 2024-06-21
----------------------
Target sighted at 23:00.
Following discreetly.
End of log.
'''
print(secret_log)

# A multiline string containing both single and double quotes
briefing = """
The message said, 'We must be careful.'
The general's order was clear: "Proceed with caution."
"""
print(briefing)
```


## Hands-On Exercises: Secret Agent Puzzles 🤫

It's time for your mission! Use your new string skills to solve these coded puzzles.

### 1. What are Strings? (10 Exercises)

1. **Creating a Secret ID:** Your agent ID is `007`, but you need to store it as a string. Create a variable `agent_id` with this value and print it.
    
2. **Mission Briefing:** Create a string variable `briefing` that says `"Mission: Operation Shadow"`. Print the full briefing.
    
3. **Hiding the Key:** A secret key is `K-88-Z`. Store this in a string variable named `secret_key` and print it.
    
4. **Team Motto:** Create a string variable `motto` with the phrase `"Swift and Silent"`. Print the motto.
    
5. **Triple Quote Report:** Use a multi-line string (triple quotes) to store a message that spans three lines: `Phase 1: Infiltration`, `Phase 2: Extraction`, and `Phase 3: Exfil`. Print the full message.
    
6. **Codename:** Store your codename, `'Pythonic Panther'`, in a variable `codename` and print it.
    
7. **Access Code:** The code for the secure room is `Delta-42`. Store this code as a string in a variable called `access_code`. Print the `access_code`.
    
8. **Location Coordinates:** The coordinates are `'34.0522, -118.2437'`. Store them in a string variable `coordinates` and print them.
    
9. **Date and Time:** Store the string `'2023-01-20 14:30'` in a variable `mission_time` and print it.
    
10. **Agent Status:** Create a string variable `status` with the value `'Active'` and print it.
    

### 2. Combining Strings (10 Exercises)

1. **Full Codename:** You have `first = 'Agent'` and `last = 'Hunter'`. Combine them to create the full codename and print `"Agent Hunter"`.
    
2. **Mission Number:** Combine the strings `'Mission-'` and `'7'` to create the full mission identifier. Store it in a variable and print it.
    
3. **Building a Dossier:** You have `name = 'Bond'` and `rank = '007'`. Combine them to print `"Dossier for Agent Bond, Rank 007"`.
    
4. **Repeated Warning:** The word is `"Warning!"`. Use the multiplication operator to print it three times on the same line: `"Warning!Warning!Warning!"`.
    
5. **Secret Message:** You have `part1 = 'The code is'` and `part2 = ' 1234'`. Combine them to print the full message.
    
6. **Agent Info:** You have `agent = 'Jason'` and `surname = 'Bourne'`. Create a single string `full_name` and print it.
    
7. **Server Address:** Combine `protocol = 'https://'` and `domain = 'secretserver.com'` to create a full URL. Store it in a variable and print it.
    
8. **Status Report:** Combine `subject = 'Status:'` and `report = 'All good'` to print `"Status:All good"`.
    
9. **Creating a Separator:** Use the string `'-'` and the multiplication operator to print a line of 20 dashes.
    
10. **Access Granted:** Combine the strings `"Access"` and `" Granted"` to create the final message and print it.
    

### 3. String Indexing (10 Exercises)

1. **First Letter of a Codename:** Your codename is `'Shadow'`. Print the first letter using indexing.
    
2. **Last Digit of a Code:** The access code is `'A-12-Z'`. Print the last character (`Z`) using both positive and negative indexing.
    
3. **Third Character:** The encrypted message is `'X1Y2Z3A'`. Print the third character (`Y`) using indexing.
    
4. **Second to Last Character:** The password is `'TopSecret'`. Print the second-to-last character (`e`) using negative indexing.
    
5. **Fourth Character:** The code is `'MISSION_COMPLETE'`. Print the fourth character (`S`).
    
6. **Agent ID Check:** An agent's ID is `'agent99'`. Print the first letter (`a`) and the last digit (`9`) using indexing.
    
7. **Accessing a Space:** The phrase is `'Agent Log'`. Find and print the character at index 5 (the space).
    
8. **Fifth Character:** A secret message reads `'CONFIDENTIAL'`. Print the fifth character (`I`).
    
9. **Last Character of a File Name:** The filename is `'top_secret_file.doc'`. Print the last character (`c`) using negative indexing.
    
10. **First Symbol:** The code is `'-KEY-'`. Print the character at index `0`.
    

### 4. String Slicing (10 Exercises)

1. **Decoding a Phrase:** A coded message is `'_SECRET_AGENT_'`. Use slicing to extract and print the word `'AGENT'`.
    
2. **Grabbing a Code:** The message is `'CODE-A-1234'`. Use slicing to get the code part `'1234'`.
    
3. **Getting a Range:** The string is `'ABCDEFGHIJ'`. Use slicing to get the characters `'CDEF'`.
    
4. **From the Beginning:** The full string is `'MISSION_STATUS_OK'`. Use slicing to get everything up to and including the word `'STATUS'`.
    
5. **To the End:** The message is `'MESSAGE: The plan is a go'`. Use slicing to get just the plan itself (`'The plan is a go'`).
    
6. **Extracting the Year:** The date is `'Date: 2024-03-15'`. Use slicing to get only the year, `'2024'`.
    
7. **Every Other Character:** A secret key is `'P-Y-T-H-O-N'`. Use slicing with a step to get the letters `PYTHON`.
    
8. **Reverse a String:** The word is `'reversemission'`. Use slicing to reverse the string and print `'noissim esrever'`.
    
9. **Taking the Middle:** The message is `'[TOP_SECRET]'`. Use slicing to extract the middle part `'TOP_SECRET'`.
    
10. **Grabbing the Hostname:** The URL is `'https://server.com/mission'`. Use slicing to get the hostname `'server.com'`.
    

### 5. Essential String Methods (10 Exercises)

1. **Count the Letters:** The phrase is `'The quick brown fox'`. Use `len()` to find the number of characters and print the length.
    
2. **The Secret is...**: A secret message is `'the secret word is fox'`. Use the `.replace()` method to change `'fox'`to `'eagle'` and print the new message.
    
3. **Cleaning Up a Name:** An agent's name is stored as `' agent007 '`. Use the `.strip()` method to remove the spaces and print the cleaned name.
    
4. **Finding a Key:** The message is `'Location: Coded Base 12'`. Use the `.find()` method to get the starting index of the word `'Base'`. Print the index.
    
5. **Uppercase Command:** A command is `'go go go'`. Use the `.upper()` method to make it all uppercase and print the result.
    
6. **Lowering the Case:** A message is `'URGENT: DESTROY THE DATA'`. Use the `.lower()` method to make it all lowercase and print it.
    
7. **Is It a Number?**: A code is `'4567'`. Use the `.isdigit()` method to check if it contains only numbers. Print the result.
    
8. **Split the Coordinates:** The coordinates are `'45.123, -78.456'`. Use the `.split()` method to separate the two numbers at the comma. Print the result.
    
9. **Title Case Mission:** A mission file is named `'project_falcon_launch'`. Use the `.replace()` and `.title()`methods to make it look like a title: `'Project Falcon Launch'`.
    
10. **Replacing a Symbol:** The password is `'pass@word!'`. Use the `.replace()` method to replace the `'@'` symbol with an `'o'`. Print the new password.
    

### 6. Escape Sequences (10 Exercises)

1. **Multi-line Briefing:** Print a briefing that starts with `"Urgent Briefing"` on one line and `"All agents report to HQ"` on the next, using `\n`.
    
2. **Tabbed Table:** Print a simple table with two columns, "Agent" and "Status", separated by a tab (`\t`). The first row should be "Bond" and "Active".
    
3. **Quote in a Quote:** Print the message `"The message was: 'The key is here'"`. Use an escape sequence to include the single quotes.
    
4. **Another Tabbed Table:** Print a table with three columns: "Item", "Quantity", and "Price", using `\t`.
    
5. **Double Quote in a Double Quote:** Print the message `'The agent said, "The mission is a success!"'`. Use an escape sequence to include the double quotes.
    
6. **Creating a Path:** The path to a file is `C:\Users\Agent\Documents`. Print this path correctly, noting that backslashes are also used for escape sequences.
    
7. **Multi-line Report with Tabs:** Print a report with a title and a sub-point. The title should be on one line, and the sub-point should be tabbed and on a new line.
    
8. **Printing a Backslash:** Print a single backslash character (`\`) by escaping it.
    
9. **New Line in the Middle:** A message is `'Top secret info. Awaiting new orders.'`. Add a new line in the middle to split the message.
    
10. **Formatted Output:** Use `\n` and `\t` to print a list of items with their prices.