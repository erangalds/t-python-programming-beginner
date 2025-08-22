# Python Lists: The Agent's Inventory 🎒

Welcome, Junior Agent! Today's mission is to learn about **lists** in Python. Think of a list as a container, like an agent's backpack or utility belt, that can hold many different items. These items can be anything: secret codes (strings), numerical passwords (integers), or even other lists!

In Python, you create a list by putting a sequence of items inside square brackets `[...]`, with each item separated by a comma.

## 1. What are Lists?

A list is a Python object that can store a collection of different data types in a specific order. Unlike strings, lists are **mutable**, meaning you can change, add, or remove items after the list has been created.

### Example Code:


```python
# A list of agent codenames (strings)
agents = ['Agent Alpha', 'Agent Bravo', 'Agent Charlie']
print(f"The agents in the field are: {agents}")

# A list of mission objectives (different data types)
mission_plan = ['Infiltrate', 2024, True, 'Get the intel']
print(f"The mission plan is: {mission_plan}")

# A list of lists, representing a team and their status
team_status = [['Alpha', 'Active'], ['Bravo', 'Standby']]
print(f"Team status report: {team_status}")
```

---

## 2. Accessing Items: List Indexing 🔎

Just like with strings, every item in a list has a secret number called an **index**, which tells you its position. Python starts counting at **zero**! The first item is at index `0`, the second at index `1`, and so on. You can also use negative numbers to count from the end of the list, with `-1` being the last item.

### Example Code:


```python
agent_inventory = ['grappling hook', 'night vision goggles', 'smoke bomb', 'silenced pistol']
# Items:    grappling hook, night vision goggles, smoke bomb, silenced pistol
# Index:    0               1                     2           3

# Access the first item (grappling hook)
first_item = agent_inventory[0]
print(f"The first item is: {first_item}")

# Access the third item (smoke bomb)
third_item = agent_inventory[2]
print(f"The third item is: {third_item}")

# Access the last item using a negative index (silenced pistol)
last_item = agent_inventory[-1]
print(f"The last item is: {last_item}")
```

---

## 3. Slicing Lists: Grabbing a Piece of the Inventory

You can also grab a chunk of a list, which is called **slicing**. This works just like slicing strings. You use a colon `:` inside the brackets to tell Python where to start and where to stop.

The syntax is `my_list[start:end]`. The slice includes the item at the `start` index but **does not include** the item at the `end` index.

### Example Code:


```python
mission_log = ['arrival', 'reconnaissance', 'infiltration', 'extraction', 'debrief']
# Grab the middle actions
core_mission = mission_log[1:4]
print(f"The core mission actions are: {core_mission}")

# Slice from the beginning to a specific index
initial_phase = mission_log[:2]
print(f"The initial phase includes: {initial_phase}")

# Slice from a specific index to the end
final_phase = mission_log[3:]
print(f"The final phase includes: {final_phase}")
```

---

## 4. Modifying Lists: Adding and Changing Items 🔄

Unlike strings, lists are **mutable**, which means you can change them. You can add new items, change existing ones, or remove them entirely.

### Example Code:


```python
agent_team = ['Agent Alpha', 'Agent Bravo']
print(f"Initial team: {agent_team}")

# Add a new agent to the end using .append()
agent_team.append('Agent Charlie')
print(f"Team after adding new agent: {agent_team}")

# Change an existing item using its index
agent_team[1] = 'Agent Beta'
print(f"Team after changing an agent: {agent_team}")

# Insert a new agent at a specific position using .insert()
agent_team.insert(0, 'Agent 007')
print(f"Team after inserting Agent 007: {agent_team}")

# Remove an item by its value using .remove()
agent_team.remove('Agent Alpha')
print(f"Team after removing an agent: {agent_team}")

# Remove the last item and return it using .pop()
popped_agent = agent_team.pop()
print(f"Popped agent: {popped_agent}")
print(f"Team after popping the last agent: {agent_team}")
```

---

## 5. Other Useful List Methods 🛠️

Lists have special actions called **methods** that help you manage your data. Here are a few essential ones.

|Method|What it does|
|---|---|
|`len()`|Finds the **length** of the list (how many items it has).|
|`.sort()`|**Sorts** the items in the list in ascending order.|
|`.reverse()`|**Reverses** the order of the items in the list.|
|`.count()`|Counts how many times a specific item appears in the list.|
|`.copy()`|Creates a **copy** of the list.|
|`.index()`|Finds the **index** of the first occurrence of a specific item.|
|`.clear()`|Removes all items from the list.|
|`.extend()`|Adds all items from another list to the end of the current list.|

### Example Code:


```python
secret_codes = ['alpha', 'gamma', 'beta', 'alpha']

# Get the length
num_codes = len(secret_codes)
print(f"Number of codes: {num_codes}")

# Sort the list alphabetically
secret_codes.sort()
print(f"Sorted codes: {secret_codes}")

# Reverse the list
secret_codes.reverse()
print(f"Reversed codes: {secret_codes}")

# Count occurrences of an item
count_alpha = secret_codes.count('alpha')
print(f"Count of 'alpha': {count_alpha}")

# Find the index of an item
index_gamma = secret_codes.index('gamma')
print(f"Index of 'gamma': {index_gamma}")

# Create a copy of the list
original_codes = ['1', '2', '3']
codes_copy = original_codes.copy()
codes_copy.append('4')
print(f"Original list: {original_codes}") # Output: ['1', '2', '3']
print(f"Copied list: {codes_copy}") # Output: ['1', '2', '3', '4']

# Add items from another list
new_codes = ['epsilon', 'zeta']
secret_codes.extend(new_codes)
print(f"List after extending: {secret_codes}")

# Clear all items from the list
secret_codes.clear()
print(f"List after clearing: {secret_codes}")
```

---
### Importance of using `.copy()` 

You should use the **`.copy()`** method to create a **true copy** of a list. This is important because assigning one list to another variable directly, like `list2 = list1`, doesn't create a new, independent list. Instead, it creates a **reference**, meaning both variables point to the same list in memory.

**The Problem with References** 🔗

When you create a reference, any changes you make to the list using one variable will affect the list accessed by the other variable. This can lead to unexpected and hard-to-find bugs in your code.


**Example Code: A Simple Mistake**

```python
# A list of our secret agents
agent_list_a = ['Agent Alpha', 'Agent Bravo']

# This creates a reference, not a copy!
agent_list_b = agent_list_a

# Now, let's remove an agent using the second variable
agent_list_b.remove('Agent Alpha')

# Look what happened to the original list...
print(f"Original list (agent_list_a): {agent_list_a}")
# Output: ['Agent Bravo'] - Uh oh! Agent Alpha is gone from the original list too.
```

In this scenario, `agent_list_a` and `agent_list_b` are not two separate lists; they are two different names for the same list.

**The Solution: The `.copy()` Method ✅**

The `.copy()` method creates a **new, shallow copy** of the list. This new list is independent of the original. Changes made to the copy will not affect the original list, and vice versa.

**Example Code: Using `.copy()` Correctly**

```python
# Our original list of agents
agent_list_a = ['Agent Alpha', 'Agent Bravo']

# Use .copy() to create an independent copy
agent_list_c = agent_list_a.copy()

# Now, let's remove an agent from the new list
agent_list_c.remove('Agent Alpha')

# The original list remains unchanged!
print(f"Original list (agent_list_a): {agent_list_a}")
# Output: ['Agent Alpha', 'Agent Bravo'] - Safe and sound!
print(f"Copied list (agent_list_c): {agent_list_c}")
# Output: ['Agent Bravo']
```

In summary, use **`.copy()`** whenever you need to modify a list without changing the original version. This ensures your data remains predictable and your code behaves as intended.

## Hands-On Exercises: Agent Inventory Puzzles 🧩

It's time for your mission! Use your new list skills to manage your agent's inventory and complete these tasks.

### 1. What are Lists? (10 Exercises)

1. **Creating a Gear List:** Your agent gear includes: 'flashlight', 'map', 'compass'. Create a list called `gear_list` with these three items and print it.
    
2. **Mission Log:** Create a list named `mission_log` with the strings `'Start'`, `'Proceed'`, and `'Complete'`. Print the list.
    
3. **Agent Ratings:** An agent's performance ratings are 9.5, 8.0, and 9.2. Create a list called `ratings` to store these numbers and print it.
    
4. **Mixed Data:** Create a list `info` containing a name (`'Agent 007'`), a mission ID (`5`), and a status (`True`). Print the list.
    
5. **Empty Inventory:** You have no gear yet. Create an empty list called `my_inventory` and print it.
    
6. **Task List:** Create a list named `tasks` containing the strings `'Plan'`, `'Execute'`, `'Report'`. Print the list.
    
7. **Secret Numbers:** Create a list named `secret_numbers` with the numbers `10`, `20`, `30`, `40`. Print the list.
    
8. **Team Codewords:** Create a list `codewords` with the strings `'Falcon'`, `'Eagle'`, `'Raven'`. Print the list.
    
9. **Security Levels:** Create a list `security_levels` with the numbers `1`, `2`, `3`, `4`, `5`. Print the list.
    
10. **A List of Lists:** Create a list `team_roster` where each item is a list with an agent's codename and rank, like `['Agent Alpha', 'Rookie']` and `['Agent Bravo', 'Veteran']`. Print the list.
    

### 2. Accessing Items (10 Exercises)

1. **First Tool:** Your list is `tools = ['lockpick', 'decoder', 'tracker']`. Print the first tool using indexing.
    
2. **Last Objective:** The list is `objectives = ['A', 'B', 'C', 'D']`. Print the last objective (`'D'`) using both positive and negative indexing.
    
3. **Third Mission:** The list is `missions = ['Spy', 'Rescue', 'Sabotage']`. Print the third mission (`'Sabotage'`) using its index.
    
4. **Second to Last Gadget:** Your list is `gadgets = ['camera', 'mic', 'laser']`. Print the second-to-last gadget (`'mic'`) using negative indexing.
    
5. **Fourth Item:** A list of items is `data_points = [100, 200, 300, 400, 500]`. Print the fourth item.
    
6. **Accessing the First and Last:** A list of codes is `codes = ['alpha', 'beta', 'gamma']`. Print the first code and the last code on separate lines.
    
7. **Second Element:** The list is `logs = ['entry1', 'entry2', 'entry3']`. Print the second entry.
    
8. **Last Security Level:** A list of levels is `levels = [1, 2, 3]`. Print the last level using negative indexing.
    
9. **Third Agent:** The list is `agents = ['A-1', 'B-2', 'C-3', 'D-4']`. Print the third agent (`'C-3'`).
    
10. **Last Coordinate:** The list is `coordinates = [45, -78, 10]`. Print the last coordinate.
    

### 3. Slicing Lists (10 Exercises)

1. **Decoding a Sublist:** The list of actions is `actions = ['start', 'wait', 'infiltrate', 'secure', 'extract']`. Get and print the sublist `['infiltrate', 'secure']`.
    
2. **First Three Files:** The list is `files = ['file1', 'file2', 'file3', 'file4', 'file5']`. Use slicing to get the first three files.
    
3. **The Last Two Tasks:** A list of tasks is `tasks = ['scan', 'download', 'upload', 'clean up']`. Use slicing to get the last two tasks.
    
4. **Get the Middle:** The list is `secret_data = ['A', 'B', 'C', 'D', 'E']`. Use slicing to get the middle three items (`'B'`, `'C'`, `'D'`).
    
5. **From Start to a Point:** A list is `log_entries = ['log1', 'log2', 'log3', 'log4']`. Get everything up to the third item (`'log1'`, `'log2'`).
    
6. **From a Point to the End:** A list is `mission_stages = ['phase1', 'phase2', 'phase3', 'phase4']`. Get all stages from 'phase3' to the end.
    
7. **Every Other Item:** A list of alternating items is `items = ['A', 'skip', 'B', 'skip', 'C']`. Use slicing with a step to get only `'A'`, `'B'`, `'C'`.
    
8. **Reverse the List:** A list is `numbers = [1, 2, 3, 4, 5]`. Use slicing to print the list in reverse order.
    
9. **Extracting a Range with a Step:** The list is `codes = [1, 2, 3, 4, 5, 6, 7, 8, 9]`. Use slicing with a step to get every third number, starting from the second number (`[2, 5, 8]`).
    
10. **A Negative Slice:** A list of items is `inventory = ['itemA', 'itemB', 'itemC', 'itemD']`. Use a negative slice to get the last two items.
    

### 4. Modifying Lists (10 Exercises)

1. **Adding a New Agent:** The team list is `team = ['Alpha', 'Bravo']`. Add a new agent, `'Charlie'`, to the end of the list using `.append()`. Print the new list.
    
2. **Changing a Mission Status:** A list is `status = ['Pending', 'In Progress', 'Failed']`. Change the last item to `'Complete'`. Print the list.
    
3. **Inserting a Priority Task:** The list is `tasks = ['briefing', 'mission']`. Insert the task `'priority_check'` at the beginning of the list using `.insert()`.
    
4. **Removing a Canceled Mission:** The list is `missions = ['recon', 'attack', 'retreat']`. Remove the `'attack'`mission from the list.
    
5. **Removing the Last Item:** The list is `log = ['entry1', 'entry2', 'entry3']`. Use `.pop()` to remove the last item from the list and print the removed item.
    
6. **Combining Lists:** You have `list1 = ['a', 'b']` and `list2 = ['c', 'd']`. Use `.extend()` to add all items from `list2` to `list1`.
    
7. **Changing a Specific Item:** The list is `codes = ['123', '456', '789']`. Change the item at index 1 to `'555'`.
    
8. **Removing a Known Item:** The list is `tools = ['wrench', 'hammer', 'screwdriver']`. Remove `'hammer'` from the list.
    
9. **Clearing a List:** A list is `temp_data = ['data1', 'data2', 'data3']`. Use `.clear()` to remove all items from the list. Print the empty list.
    
10. **Inserting at the End:** The list is `checkpoints = ['A', 'B']`. Use `.insert()` to add `'C'` at the end. (Hint: you'll need the length of the list).
    

### 5. Essential List Methods (10 Exercises)

1. **Count the Items:** The list is `tasks = ['recon', 'recon', 'intel', 'report']`. Use `len()` to find out how many tasks there are.
    
2. **How Many Recons?** Use `.count()` on the list from the previous exercise to find out how many times `'recon'` appears.
    
3. **Sort the Roster:** The list is `roster = ['Bravo', 'Alpha', 'Charlie']`. Use `.sort()` to sort the list alphabetically. Print the sorted list.
    
4. **Reverse the Log:** The list is `log = ['log1', 'log2', 'log3']`. Use `.reverse()` to print the log in reverse order.
    
5. **Find the Index:** The list is `targets = ['north', 'south', 'east', 'west']`. Use `.index()` to find the index of `'east'`.
    
6. **Create a Copy:** The list is `original_plan = ['A', 'B', 'C']`. Create a copy of this list in a new variable `backup_plan` using `.copy()`. Add a new item `'D'` to `original_plan` and print both lists to show the copy wasn't affected.
    
7. **Find the First Occurrence:** The list is `locations = ['A', 'B', 'A', 'C']`. Use `.index()` to find the index of the first `'A'`.
    
8. **Clear the Database:** A list is `database = ['user1', 'user2', 'user3']`. Use `.clear()` to empty the database.
    
9. **Add a Sub-Team:** You have `team1 = ['alpha', 'bravo']` and `sub_team = ['gamma', 'delta']`. Use `.extend()`to add `sub_team` to `team1`.
    
10. **Check for an Item:** How would you check if the item `'beta'` is in the list `agents = ['alpha', 'gamma', 'delta']`? (Hint: Use the `in` keyword).