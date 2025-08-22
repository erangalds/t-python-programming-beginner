# Python Tuples: The Classified File 📁

Welcome, Junior Agent! Your next mission is to learn about **tuples** in Python. Think of a tuple as a sealed, classified file—once the information is inside, it can't be changed, added to, or removed. Tuples are perfect for storing data that should remain constant and secure.

In Python, you create a tuple by putting a sequence of items inside parentheses `(...)`, with each item separated by a comma.

## 1. What are Tuples?

A tuple is a Python object that stores an ordered collection of different data types. The most important thing to remember about tuples is that they are **immutable**. This means you cannot modify, add, or remove items once the tuple has been created.

### Example Code:


```python
# A tuple of fixed mission coordinates
mission_coordinates = (45.123, -78.456)
print(f"The mission coordinates are: {mission_coordinates}")

# A tuple containing different types of classified information
agent_profile = ('Agent Bond', 7, 'Active')
print(f"The agent's profile is: {agent_profile}")

# A tuple of tuples, representing a fixed team roster
team_roster = (('Alpha', 1), ('Bravo', 2))
print(f"The team roster is: {team_roster}")

# A tuple with a single item needs a trailing comma
single_item_tuple = ('Top Secret',)
print(f"Single item tuple: {single_item_tuple}")
```


## 2. Accessing Items: Tuple Indexing 🔎

Just like with strings and lists, every item in a tuple has a secret number called an **index**. The first item is at index `0`, the second at index `1`, and so on. You can also use negative numbers to count from the end of the tuple, with `-1` being the last item.

### Example Code:


```python
classified_data = ('codename_phoenix', 'status_green', 2024, True)
# Items:   codename_phoenix, status_green, 2024, True
# Index:   0                 1             2     3

# Access the first item (codename_phoenix)
first_item = classified_data[0]
print(f"The first item is: {first_item}")

# Access the third item (2024)
third_item = classified_data[2]
print(f"The third item is: {third_item}")

# Access the last item using a negative index (True)
last_item = classified_data[-1]
print(f"The last item is: {last_item}")
```


## 3. Slicing Tuples: Reading a Part of the File

You can also grab a chunk of a tuple, which is called **slicing**. This works exactly like slicing strings and lists. You use a colon `:` inside the brackets to tell Python where to start and where to stop.

The syntax is `my_tuple[start:end]`. The slice includes the item at the `start` index but **does not include** the item at the `end` index.

### Example Code:


```python
mission_briefing = ('recon', 'infiltrate', 'secure', 'exfil', 'debrief')
# Grab the core mission actions
core_mission = mission_briefing[1:4]
print(f"The core mission actions are: {core_mission}")

# Slice from the beginning to a specific index
initial_phase = mission_briefing[:2]
print(f"The initial phase includes: {initial_phase}")

# Slice from a specific index to the end
final_phase = mission_briefing[3:]
print(f"The final phase includes: {final_phase}")
```


## 4. Why Can't We Modify Tuples? 🛑

The most important rule about tuples is that they are **immutable**. This is a powerful feature that guarantees the data you store will not be accidentally changed. Because of this, you cannot use methods like `.append()`, `.remove()`, or `.insert()` on tuples, and you cannot reassign items using their index.

### Example Code: A Mission that Fails


```python
# A tuple of agent access codes
access_codes = ('A-1', 'B-2', 'C-3')
print(f"Initial codes: {access_codes}")

# --- THE FOLLOWING CODE WILL CAUSE AN ERROR! ---

# Try to change an item (this will fail)
# access_codes[1] = 'B-5'

# Try to add a new item (this will also fail)
# access_codes.append('D-4')

# When you run the code, you will get a "TypeError"
# Tuples are immutable, so they cannot be modified!
```


## 5. Useful Tuple Functions & Methods 🧠

Tuples have a limited number of methods because they are immutable. The functions and methods you can use don't change the tuple itself but instead provide information about it.

|Function/Method|What it does|
|---|---|
|`len()`|Finds the **length** of the tuple (how many items it has).|
|`.count()`|Counts how many times a specific item appears in the tuple.|
|`.index()`|Finds the **index** of the first occurrence of a specific item.|

A common use of tuples is **unpacking**, where you assign the items of a tuple to individual variables.

### Example Code:


```python
secret_file = ('Location Alpha', 2024, 'Complete')

# Get the length
file_length = len(secret_file)
print(f"The file contains {file_length} pieces of data.")

# Count occurrences of an item
data_tuple = (1, 5, 2, 5, 3)
count_fives = data_tuple.count(5)
print(f"The number 5 appears {count_fives} times.")

# Find the index of an item
status_index = secret_file.index('Complete')
print(f"The 'Complete' status is at index: {status_index}")

# Unpack the tuple into variables
location, year, status = secret_file
print(f"Location: {location}, Year: {year}, Status: {status}")
```


## Hands-On Exercises: Classified Puzzles 🕵️‍♀️

It's time to test your knowledge! Use your new tuple skills to work with these classified files.

### 1. What are Tuples? (10 Exercises)

1. **Creating a Classified File:** Your mission file contains `('Operation Nightfall', 'Active', 101)`. Create a tuple named `mission_file` with these items and print it.
    
2. **Secret Coordinates:** The coordinates for the rendezvous point are `(34.05, -118.24)`. Store these as a tuple called `rendezvous_coords` and print it.
    
3. **Agent Ranks:** Create a tuple named `ranks` containing the numbers `1`, `2`, `3`, `4`, `5`. Print the tuple.
    
4. **A Single Code:** Create a tuple named `secret_code` that contains only the string `'CODE_ALPHA'`. Remember to include the trailing comma. Print the tuple.
    
5. **Mixed Data:** Create a tuple `secure_data` containing a string (`'User: Admin'`), a number (`12345`), and a boolean value (`False`). Print the tuple.
    
6. **Immutable List:** Create a tuple `unbreakable_list` that contains a list of items `['a', 'b', 'c']`. Print the tuple.
    
7. **Mission Numbers:** Create a tuple `mission_numbers` with the values `77`, `88`, `99`. Print the tuple.
    
8. **Status Log:** Create a tuple `status_log` with the strings `'Received'`, `'Processed'`, `'Archived'`. Print the tuple.
    
9. **A Tuple of Tuples:** Create a tuple `database_entry` where each item is a tuple of a name and an ID: `('Bond', '007')` and `('Bourne', '010')`. Print the tuple.
    
10. **Empty Tuple:** Create an empty tuple named `empty_file` and print it.
    

### 2. Accessing and Slicing (10 Exercises)

1. **First Agent:** Your tuple of agents is `agents = ('Alpha', 'Bravo', 'Charlie')`. Print the first agent using indexing.
    
2. **Last Status:** The tuple is `status = ('pending', 'in progress', 'complete')`. Print the last status using both positive and negative indexing.
    
3. **Third Number:** The tuple of codes is `codes = (10, 20, 30, 40)`. Print the third number using its index.
    
4. **Second to Last Record:** Your tuple is `records = ('fileA', 'fileB', 'fileC')`. Print the second-to-last record using negative indexing.
    
5. **Decoding the Middle:** A tuple contains `('start', 'end', 'key', 'code', 'final')`. Use slicing to get the sub-tuple `('key', 'code')`.
    
6. **First Two Items:** A tuple is `data = ('101', '102', '103', '104')`. Use slicing to get the first two items.
    
7. **Slicing to the End:** The tuple is `log = ('read', 'write', 'delete', 'commit')`. Use slicing to get the last three items.
    
8. **Every Other Entry:** A tuple is `entries = ('A', 'skip', 'B', 'skip', 'C')`. Use slicing with a step to get only `'A'`, `'B'`, `'C'`.
    
9. **Reverse the Tuple:** A tuple is `numbers = (1, 2, 3, 4, 5)`. Use slicing to print the tuple in reverse order.
    
10. **Extracting the Year:** The tuple is `report = ('Report', '2024', 'Confidential')`. Use indexing to print the year.
    

### 3. Using Tuple Methods (10 Exercises)

1. **Count the Items:** The tuple is `tasks = ('recon', 'intel', 'report')`. Use `len()` to find out how many tasks there are.
    
2. **How Many Intel Reports?** A tuple of reports is `reports = ('intel', 'recon', 'intel', 'summary')`. Use `.count()`to find how many times `'intel'` appears.
    
3. **Find the Index:** The tuple is `plan = ('step1', 'step2', 'step3')`. Use `.index()` to find the index of `'step3'`.
    
4. **Unpack a Profile:** The tuple is `profile = ('Agent 007', 'Active', 'Alpha')`. Unpack this tuple into three separate variables: `agent_name`, `agent_status`, and `agent_codename`. Print each variable.
    
5. **Count a Number:** The tuple is `data = (1, 5, 2, 8, 5)`. Use `.count()` to find how many times the number `5`appears.
    
6. **Find the First Occurrence:** The tuple is `locations = ('HQ', 'HQ', 'Safehouse', 'HQ')`. Use `.index()` to find the index of the first `'HQ'`.
    
7. **Check the Length:** The tuple is `credentials = ('user', 'password')`. Use `len()` to verify that the tuple has exactly two items. Print the result.
    
8. **Multiple Unpacking:** The tuple is `address = ('123', 'Secret St.', 'Spyville')`. Unpack this into `number`, `street`, and `city`. Print the city.
    
9. **Count a String:** The tuple is `log = ('alert', 'warning', 'alert')`. Use `.count()` to find the number of `'alert'`entries.
    
10. **Find the Index of a Number:** The tuple is `numbers = (10, 20, 30, 40)`. Use `.index()` to find the index of the number `30`.
    

### 4. The Immutable Challenge (5 Exercises)

1. **The Failed Reassignment:** Create a tuple `mission_status = ('pending', 'in progress')`. Write a line of code that attempts to change the first item to `'complete'`. Run the code and observe the `TypeError`. Add a comment explaining why it failed.
    
2. **The Failed Append:** Create a tuple `agent_list = ('Alpha', 'Bravo')`. Write a line of code that attempts to add a new agent, `'Charlie'`, to the tuple. Run the code and observe the `AttributeError`. Add a comment explaining why it failed.
    
3. **The Failed Removal:** Create a tuple `task_list = ('recon', 'intel')`. Write a line of code that attempts to remove the `'recon'` item. Run the code and observe the `AttributeError`. Add a comment explaining why it failed.
    
4. **A Tuple with a Mutable Item:** Create a tuple `confidential = ('Key-1', ['log_a', 'log_b'])`. Access the list inside the tuple and append `'log_c'` to it. Print the tuple to see what happened. (Hint: The tuple itself is immutable, but the _list inside it_ is not!)
    
5. **Converting to a List:** To solve the immutability problem, you can convert a tuple to a list. Create a tuple `roster_tuple = ('Bond', 'M')`. Convert it to a list, add `'Q'`, and then convert it back to a tuple. Print the final tuple.