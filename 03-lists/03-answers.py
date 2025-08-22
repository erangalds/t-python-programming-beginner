# ==============================================================================
# SOLUTIONS FOR HANDS-ON LISTS EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 50 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: What are Lists?
# ------------------------------------------------------------------------------

# Question 1: Creating a Gear List
# Thought Process: A list is created using square brackets []. Each item is a
# string and is separated by a comma.
gear_list = ['flashlight', 'map', 'compass']
print(gear_list)

# Question 2: Mission Log
# Thought Process: The mission log is a list of strings, so we put the text
# in quotes inside square brackets.
mission_log = ['Start', 'Proceed', 'Complete']
print(mission_log)

# Question 3: Agent Ratings
# Thought Process: The ratings are numbers, so we put them directly into the
# list without quotes.
ratings = [9.5, 8.0, 9.2]
print(ratings)

# Question 4: Mixed Data
# Thought Process: Lists can hold different data types, so we include a string,
# an integer, and a boolean value.
info = ['Agent 007', 5, True]
print(info)

# Question 5: Empty Inventory
# Thought Process: An empty list is created with empty square brackets [].
my_inventory = []
print(my_inventory)

# Question 6: Task List
# Thought Process: We create a list of strings to represent the tasks.
tasks = ['Plan', 'Execute', 'Report']
print(tasks)

# Question 7: Secret Numbers
# Thought Process: We create a list of integers.
secret_numbers = [10, 20, 30, 40]
print(secret_numbers)

# Question 8: Team Codewords
# Thought Process: We create a list of strings representing the codewords.
codewords = ['Falcon', 'Eagle', 'Raven']
print(codewords)

# Question 9: Security Levels
# Thought Process: We create a list of numbers representing security levels.
security_levels = [1, 2, 3, 4, 5]
print(security_levels)

# Question 10: A List of Lists
# Thought Process: The team roster is a list where each item is another list
# containing the agent's name and rank.
team_roster = [['Agent Alpha', 'Rookie'], ['Agent Bravo', 'Veteran']]
print(team_roster)


# ------------------------------------------------------------------------------
# Section 2: Accessing Items
# ------------------------------------------------------------------------------

# Question 1: First Tool
# Thought Process: The first item in a list is at index 0.
tools = ['lockpick', 'decoder', 'tracker']
first_tool = tools[0]
print(first_tool)

# Question 2: Last Objective
# Thought Process: The last item can be accessed with positive indexing (index 3)
# or negative indexing (index -1).
objectives = ['A', 'B', 'C', 'D']
last_objective_positive = objectives[3]
last_objective_negative = objectives[-1]
print(last_objective_positive)
print(last_objective_negative)

# Question 3: Third Mission
# Thought Process: The third item is at index 2.
missions = ['Spy', 'Rescue', 'Sabotage']
third_mission = missions[2]
print(third_mission)

# Question 4: Second to Last Gadget
# Thought Process: The second to last item is at index -2.
gadgets = ['camera', 'mic', 'laser']
second_to_last = gadgets[-2]
print(second_to_last)

# Question 5: Fourth Item
# Thought Process: The fourth item is at index 3.
data_points = [100, 200, 300, 400, 500]
fourth_item = data_points[3]
print(fourth_item)

# Question 6: Accessing the First and Last
# Thought Process: The first item is at index 0 and the last is at index -1.
codes = ['alpha', 'beta', 'gamma']
first_code = codes[0]
last_code = codes[-1]
print(f"First code: {first_code}")
print(f"Last code: {last_code}")

# Question 7: Second Element
# Thought Process: The second element is at index 1.
logs = ['entry1', 'entry2', 'entry3']
second_entry = logs[1]
print(second_entry)

# Question 8: Last Security Level
# Thought Process: The last item can be accessed using negative indexing (-1).
levels = [1, 2, 3]
last_level = levels[-1]
print(last_level)

# Question 9: Third Agent
# Thought Process: The third agent is at index 2.
agents = ['A-1', 'B-2', 'C-3', 'D-4']
third_agent = agents[2]
print(third_agent)

# Question 10: Last Coordinate
# Thought Process: The last coordinate is at index -1.
coordinates = [45, -78, 10]
last_coordinate = coordinates[-1]
print(last_coordinate)


# ------------------------------------------------------------------------------
# Section 3: Slicing Lists
# ------------------------------------------------------------------------------

# Question 1: Decoding a Sublist
# Thought Process: The sublist starts at index 2 and ends before index 4.
actions = ['start', 'wait', 'infiltrate', 'secure', 'extract']
core_actions = actions[2:4]
print(core_actions)

# Question 2: First Three Files
# Thought Process: We want to start at the beginning (index 0) and go up
# to, but not including, index 3. We can omit the start index.
files = ['file1', 'file2', 'file3', 'file4', 'file5']
first_three = files[:3]
print(first_three)

# Question 3: The Last Two Tasks
# Thought Process: We can slice from index -2 to the end of the list.
tasks = ['scan', 'download', 'upload', 'clean up']
last_two_tasks = tasks[-2:]
print(last_two_tasks)

# Question 4: Get the Middle
# Thought Process: We want items from index 1 up to, but not including, index 4.
secret_data = ['A', 'B', 'C', 'D', 'E']
middle_three = secret_data[1:4]
print(middle_three)

# Question 5: From Start to a Point
# Thought Process: We want to get items up to, but not including, index 2.
log_entries = ['log1', 'log2', 'log3', 'log4']
partial_log = log_entries[:2]
print(partial_log)

# Question 6: From a Point to the End
# Thought Process: We want to get items starting from index 2 to the end.
mission_stages = ['phase1', 'phase2', 'phase3', 'phase4']
final_stages = mission_stages[2:]
print(final_stages)

# Question 7: Every Other Item
# Thought Process: We use a step of 2 to grab every other item.
items = ['A', 'skip', 'B', 'skip', 'C']
decoded_items = items[::2]
print(decoded_items)

# Question 8: Reverse the List
# Thought Process: A step of -1 reverses the list.
numbers = [1, 2, 3, 4, 5]
reversed_numbers = numbers[::-1]
print(reversed_numbers)

# Question 9: Extracting a Range with a Step
# Thought Process: We start at index 1 and grab every third item.
codes = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_codes = codes[1::3]
print(sliced_codes)

# Question 10: A Negative Slice
# Thought Process: We can use negative indices for both start and end points
# to slice from the end of the list.
inventory = ['itemA', 'itemB', 'itemC', 'itemD']
last_two = inventory[-2:]
print(last_two)


# ------------------------------------------------------------------------------
# Section 4: Modifying Lists
# ------------------------------------------------------------------------------

# Question 1: Adding a New Agent
# Thought Process: We use the .append() method to add an item to the end.
team = ['Alpha', 'Bravo']
team.append('Charlie')
print(team)

# Question 2: Changing a Mission Status
# Thought Process: We access the last item using its index (-1) and assign it a
# new value.
status = ['Pending', 'In Progress', 'Failed']
status[-1] = 'Complete'
print(status)

# Question 3: Inserting a Priority Task
# Thought Process: We use the .insert() method with index 0 to add an item
# at the beginning.
tasks = ['briefing', 'mission']
tasks.insert(0, 'priority_check')
print(tasks)

# Question 4: Removing a Canceled Mission
# Thought Process: The .remove() method removes the first occurrence of a
# specified value.
missions = ['recon', 'attack', 'retreat']
missions.remove('attack')
print(missions)

# Question 5: Removing the Last Item
# Thought Process: The .pop() method removes the last item and returns it.
log = ['entry1', 'entry2', 'entry3']
removed_item = log.pop()
print(f"Removed item: {removed_item}")
print(f"Updated log: {log}")

# Question 6: Combining Lists
# Thought Process: The .extend() method adds all items from one list to another.
list1 = ['a', 'b']
list2 = ['c', 'd']
list1.extend(list2)
print(list1)

# Question 7: Changing a Specific Item
# Thought Process: We access the item at index 1 and assign it a new value.
codes = ['123', '456', '789']
codes[1] = '555'
print(codes)

# Question 8: Removing a Known Item
# Thought Process: We use the .remove() method to remove the string 'hammer'.
tools = ['wrench', 'hammer', 'screwdriver']
tools.remove('hammer')
print(tools)

# Question 9: Clearing a List
# Thought Process: The .clear() method removes all items from the list.
temp_data = ['data1', 'data2', 'data3']
temp_data.clear()
print(temp_data)

# Question 10: Inserting at the End
# Thought Process: The len() function gives us the index of where to add a new
# item to the end of the list.
checkpoints = ['A', 'B']
checkpoints.insert(len(checkpoints), 'C')
print(checkpoints)


# ------------------------------------------------------------------------------
# Section 5: Essential List Methods
# ------------------------------------------------------------------------------

# Question 1: Count the Items
# Thought Process: We use the len() function to find the number of items.
tasks = ['recon', 'recon', 'intel', 'report']
num_tasks = len(tasks)
print(num_tasks)

# Question 2: How Many Recons?
# Thought Process: The .count() method counts the number of occurrences of a value.
tasks = ['recon', 'recon', 'intel', 'report']
recon_count = tasks.count('recon')
print(recon_count)

# Question 3: Sort the Roster
# Thought Process: The .sort() method sorts the list in place, in alphabetical order.
roster = ['Bravo', 'Alpha', 'Charlie']
roster.sort()
print(roster)

# Question 4: Reverse the Log
# Thought Process: The .reverse() method reverses the order of the list in place.
log = ['log1', 'log2', 'log3']
log.reverse()
print(log)

# Question 5: Find the Index
# Thought Process: The .index() method returns the index of the first match.
targets = ['north', 'south', 'east', 'west']
index_of_east = targets.index('east')
print(index_of_east)

# Question 6: Create a Copy
# Thought Process: We use the .copy() method to create a new, independent list.
original_plan = ['A', 'B', 'C']
backup_plan = original_plan.copy()
original_plan.append('D')
print(f"Original list: {original_plan}")
print(f"Backup list: {backup_plan}")

# Question 7: Find the First Occurrence
# Thought Process: The .index() method only finds the first occurrence.
locations = ['A', 'B', 'A', 'C']
first_a_index = locations.index('A')
print(first_a_index)

# Question 8: Clear the Database
# Thought Process: The .clear() method removes all elements from the list.
database = ['user1', 'user2', 'user3']
database.clear()
print(database)

# Question 9: Add a Sub-Team
# Thought Process: We use the .extend() method to add all elements from the
# `sub_team` list to `team1`.
team1 = ['alpha', 'bravo']
sub_team = ['gamma', 'delta']
team1.extend(sub_team)
print(team1)

# Question 10: Check for an Item
# Thought Process: The `in` keyword is the most straightforward way to check for
# the presence of an item in a list. It returns a boolean value (True or False).
agents = ['alpha', 'gamma', 'delta']
is_beta_present = 'beta' in agents
print(is_beta_present)
