# ==============================================================================
# SOLUTIONS FOR HANDS-ON STRINGS EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 60 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: What are Strings?
# ------------------------------------------------------------------------------

# Question 1: Creating a Secret ID
# Thought Process: The ID '007' needs to be a string. We put it in quotes
# and store it in a variable.
agent_id = "007"
print(agent_id)

# Question 2: Mission Briefing
# Thought Process: We create a variable 'briefing' and store the text
# inside double quotes.
briefing = "Mission: Operation Shadow"
print(briefing)

# Question 3: Hiding the Key
# Thought Process: We store the string 'K-88-Z' in a variable named 'secret_key'.
secret_key = 'K-88-Z'
print(secret_key)

# Question 4: Team Motto
# Thought Process: We store the phrase in a variable called 'motto'.
motto = "Swift and Silent"
print(motto)

# Question 5: Triple Quote Report
# Thought Process: The message spans multiple lines, so triple quotes
# are the best way to store it as a single string.
mission_report = """Phase 1: Infiltration
Phase 2: Extraction
Phase 3: Exfil"""
print(mission_report)

# Question 6: Codename
# Thought Process: We store the text 'Pythonic Panther' in a variable 'codename'.
codename = 'Pythonic Panther'
print(codename)

# Question 7: Access Code
# Thought Process: We create a variable 'access_code' and store the text 'Delta-42'.
access_code = "Delta-42"
print(access_code)

# Question 8: Location Coordinates
# Thought Process: We store the coordinates in a string variable 'coordinates'.
coordinates = '34.0522, -118.2437'
print(coordinates)

# Question 9: Date and Time
# Thought Process: We store the date and time as a string.
mission_time = '2023-01-20 14:30'
print(mission_time)

# Question 10: Agent Status
# Thought Process: We create a string variable 'status' and set its value to 'Active'.
status = 'Active'
print(status)


# ------------------------------------------------------------------------------
# Section 2: Combining Strings
# ------------------------------------------------------------------------------

# Question 1: Full Codename
# Thought Process: We use the '+' operator to join the two strings and a space.
first = 'Agent'
last = 'Hunter'
full_codename = first + ' ' + last
print(full_codename)

# Question 2: Mission Number
# Thought Process: We combine the two strings using the '+' operator.
mission_prefix = 'Mission-'
mission_number = '7'
mission_id = mission_prefix + mission_number
print(mission_id)

# Question 3: Building a Dossier
# Thought Process: We combine the text and the variables to form a complete sentence.
name = 'Bond'
rank = '007'
dossier = "Dossier for Agent " + name + ", Rank " + rank
print(dossier)

# Question 4: Repeated Warning
# Thought Process: The '*' operator is used to repeat a string.
warning = "Warning!"
repeated_warning = warning * 3
print(repeated_warning)

# Question 5: Secret Message
# Thought Process: We combine the two parts of the message using the '+' operator.
part1 = 'The code is'
part2 = ' 1234'
secret_message = part1 + part2
print(secret_message)

# Question 6: Agent Info
# Thought Process: We combine the agent's first and last name with a space in between.
agent = 'Jason'
surname = 'Bourne'
full_name = agent + ' ' + surname
print(full_name)

# Question 7: Server Address
# Thought Process: We combine the protocol and the domain to create a full URL.
protocol = 'https://'
domain = 'secretserver.com'
url = protocol + domain
print(url)

# Question 8: Status Report
# Thought Process: We concatenate the subject and report strings.
subject = 'Status:'
report = 'All good'
status_report = subject + report
print(status_report)

# Question 9: Creating a Separator
# Thought Process: We use the '*' operator to repeat the '-' string 20 times.
separator = '-' * 20
print(separator)

# Question 10: Access Granted
# Thought Process: We combine the two words to form the final message.
access_granted_message = "Access" + " Granted"
print(access_granted_message)


# ------------------------------------------------------------------------------
# Section 3: String Indexing
# ------------------------------------------------------------------------------

# Question 1: First Letter of a Codename
# Thought Process: The first character is always at index 0.
codename = 'Shadow'
first_letter = codename[0]
print(first_letter)

# Question 2: Last Digit of a Code
# Thought Process: The last character can be accessed with positive indexing
# (index 4) or negative indexing (index -1).
access_code = 'A-12-Z'
last_letter_positive = access_code[5]
last_letter_negative = access_code[-1]
print(last_letter_positive)
print(last_letter_negative)

# Question 3: Third Character
# Thought Process: The third character is at index 2 (remember, we start at 0).
encrypted_message = 'X1Y2Z3A'
third_character = encrypted_message[2]
print(third_character)

# Question 4: Second to Last Character
# Thought Process: The second to last character is at index -2.
password = 'TopSecret'
second_to_last = password[-2]
print(second_to_last)

# Question 5: Fourth Character
# Thought Process: The fourth character is at index 3.
message = 'MISSION_COMPLETE'
fourth_character = message[3]
print(fourth_character)

# Question 6: Agent ID Check
# Thought Process: The first letter is at index 0 and the last digit is at index 6 or -1.
agent_id = 'agent99'
first_letter = agent_id[0]
last_digit = agent_id[-1]
print(f"First letter: {first_letter}, Last digit: {last_digit}")

# Question 7: Accessing a Space
# Thought Process: We count the index of the space character.
phrase = 'Agent Log'
space_char = phrase[5]
print(f"The character at index 5 is: '{space_char}'")

# Question 8: Fifth Character
# Thought Process: The fifth character is at index 4.
secret_message = 'CONFIDENTIAL'
fifth_character = secret_message[4]
print(fifth_character)

# Question 9: Last Character of a File Name
# Thought Process: We use negative indexing to access the last character.
filename = 'top_secret_file.doc'
last_character = filename[-1]
print(last_character)

# Question 10: First Symbol
# Thought Process: The first character is at index 0.
code = '-KEY-'
first_symbol = code[0]
print(first_symbol)


# ------------------------------------------------------------------------------
# Section 4: String Slicing
# ------------------------------------------------------------------------------

# Question 1: Decoding a Phrase
# Thought Process: We want the word 'AGENT', which starts at index 8 and
# ends before index 13.
message = '_SECRET_AGENT_'
secret_word = message[8:13]
print(secret_word)

# Question 2: Grabbing a Code
# Thought Process: The code '1234' starts at index 7 and goes to the end.
# We can omit the end index.
message = 'CODE-A-1234'
code = message[7:]
print(code)

# Question 3: Getting a Range
# Thought Process: We want characters from index 2 up to (but not including)
# index 6.
alphabet = 'ABCDEFGHIJ'
slice_of_letters = alphabet[2:6]
print(slice_of_letters)

# Question 4: From the Beginning
# Thought Process: The word 'STATUS' ends at index 12. We start from the
# beginning, so we can omit the start index.
full_string = 'MISSION_STATUS_OK'
status_part = full_string[:13]
print(status_part)

# Question 5: To the End
# Thought Process: The plan starts at index 9 and goes to the end.
message = 'MESSAGE: The plan is a go'
plan = message[9:]
print(plan)

# Question 6: Extracting the Year
# Thought Process: The year '2024' starts at index 6 and ends before index 10.
date_string = 'Date: 2024-03-15'
year = date_string[6:10]
print(year)

# Question 7: Every Other Character
# Thought Process: We use a step of 2 to skip every other character.
secret_key = 'P-Y-T-H-O-N'
decoded_key = secret_key[::2]
print(decoded_key)

# Question 8: Reverse a String
# Thought Process: A step of -1 reverses the string.
word_to_reverse = 'reversemission'
reversed_word = word_to_reverse[::-1]
print(reversed_word)

# Question 9: Taking the Middle
# Thought Process: We find the start index (1) and end index (11) of the word.
message = '[TOP_SECRET]'
middle_part = message[1:11]
print(middle_part)

# Question 10: Grabbing the Hostname
# Thought Process: We want the string from index 8 up to index 17.
url = 'https://server.com/mission'
hostname = url[8:18]
print(hostname)


# ------------------------------------------------------------------------------
# Section 5: Essential String Methods
# ------------------------------------------------------------------------------

# Question 1: Count the Letters
# Thought Process: We use the len() function to find the length of the string.
phrase = 'The quick brown fox'
phrase_length = len(phrase)
print(phrase_length)

# Question 2: The Secret is...
# Thought Process: We use the .replace() method to swap 'fox' with 'eagle'.
secret_message = 'the secret word is fox'
new_message = secret_message.replace('fox', 'eagle')
print(new_message)

# Question 3: Cleaning Up a Name
# Thought Process: The .strip() method removes leading and trailing spaces.
name = '   agent007   '
cleaned_name = name.strip()
print(cleaned_name)

# Question 4: Finding a Key
# Thought Process: The .find() method returns the starting index of the substring.
message = 'Location: Coded Base 12'
index_of_base = message.find('Base')
print(index_of_base)

# Question 5: Uppercase Command
# Thought Process: We use the .upper() method to convert the string.
command = 'go go go'
uppercase_command = command.upper()
print(uppercase_command)

# Question 6: Lowering the Case
# Thought Process: We use the .lower() method to convert the string.
message = 'URGENT: DESTROY THE DATA'
lowercase_message = message.lower()
print(lowercase_message)

# Question 7: Is It a Number?
# Thought Process: We use the .isdigit() method, which returns a boolean.
code = '4567'
is_number = code.isdigit()
print(is_number)

# Question 8: Split the Coordinates
# Thought Process: We use the .split() method with ',' as the separator.
coordinates = '45.123, -78.456'
coordinates_list = coordinates.split(',')
print(coordinates_list)

# Question 9: Title Case Mission
# Thought Process: We replace the underscores and then use .title() to capitalize each word.
filename = 'project_falcon_launch'
title_case_name = filename.replace('_', ' ').title()
print(title_case_name)

# Question 10: Replacing a Symbol
# Thought Process: We use the .replace() method to swap the symbol.
password = 'pass@word!'
new_password = password.replace('@', 'o')
print(new_password)


# ------------------------------------------------------------------------------
# Section 6: Escape Sequences
# ------------------------------------------------------------------------------

# Question 1: Multi-line Briefing
# Thought Process: We use the '\n' escape sequence to create a new line.
briefing = "Urgent Briefing\nAll agents report to HQ"
print(briefing)

# Question 2: Tabbed Table
# Thought Process: We use '\t' to create a tab space between the columns.
table = "Agent\tStatus\nBond\tActive"
print(table)

# Question 3: Quote in a Quote
# Thought Process: We use \' to escape the single quotes inside the double-quoted string.
message = "The message was: 'The key is here'"
print(message)

# Question 4: Another Tabbed Table
# Thought Process: We use a combination of '\t' and '\n' to format the table.
table = "Item\tQuantity\tPrice\nLaptop\t1\t$1200\nPhone\t2\t$800"
print(table)

# Question 5: Double Quote in a Double Quote
# Thought Process: We use \" to escape the double quotes inside the single-quoted string.
message = 'The agent said, "The mission is a success!"'
print(message)

# Question 6: Creating a Path
# Thought Process: The backslash is an escape character. To print a literal backslash,
# we need to use a double backslash '\\'.
path = "C:\\Users\\Agent\\Documents"
print(path)

# Question 7: Multi-line Report with Tabs
# Thought Process: We combine '\n' for the new line and '\t' for the tab.
report = "Project Hydra Report\n\tStatus: Complete"
print(report)

# Question 8: Printing a Backslash
# Thought Process: To print a single backslash, we must escape it with another backslash.
print("\\")

# Question 9: New Line in the Middle
# Thought Process: We find the point in the string where we want to insert the new line.
message = 'Top secret info.\nAwaiting new orders.'
print(message)

# Question 10: Formatted Output
# Thought Process: We use a combination of new lines and tabs to format the output.
output = "Shopping List:\n\t- Flashlight: $15\n\t- Batteries: $5"
print(output)
