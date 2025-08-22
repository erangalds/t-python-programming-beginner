# ==============================================================================
# SOLUTIONS FOR HANDS-ON TUPLES EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 35 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: What are Tuples?
# ------------------------------------------------------------------------------

# Question 1: Creating a Classified File
# Thought Process: A tuple is created using parentheses () with items separated
# by commas.
mission_file = ('Operation Nightfall', 'Active', 101)
print(mission_file)

# Question 2: Secret Coordinates
# Thought Process: Coordinates are fixed, so a tuple is a good choice.
rendezvous_coords = (34.05, -118.24)
print(rendezvous_coords)

# Question 3: Agent Ranks
# Thought Process: We create a tuple of integers.
ranks = (1, 2, 3, 4, 5)
print(ranks)

# Question 4: A Single Code
# Thought Process: A tuple with a single item requires a trailing comma to
# be recognized as a tuple.
secret_code = ('CODE_ALPHA',)
print(secret_code)

# Question 5: Mixed Data
# Thought Process: Tuples can store different data types, just like lists.
secure_data = ('User: Admin', 12345, False)
print(secure_data)

# Question 6: Immutable List
# Thought Process: The tuple itself is immutable, but it can contain a list
# which is mutable.
unbreakable_list = ('a', 'b', 'c')
print(unbreakable_list)

# Question 7: Mission Numbers
# Thought Process: We create a tuple of integers.
mission_numbers = (77, 88, 99)
print(mission_numbers)

# Question 8: Status Log
# Thought Process: The log of statuses is stored in a tuple of strings.
status_log = ('Received', 'Processed', 'Archived')
print(status_log)

# Question 9: A Tuple of Tuples
# Thought Process: We create a tuple where each item is a nested tuple.
database_entry = (('Bond', '007'), ('Bourne', '010'))
print(database_entry)

# Question 10: Empty Tuple
# Thought Process: An empty tuple is created with empty parentheses.
empty_file = ()
print(empty_file)


# ------------------------------------------------------------------------------
# Section 2: Accessing and Slicing
# ------------------------------------------------------------------------------

# Question 1: First Agent
# Thought Process: The first item in a tuple is at index 0.
agents = ('Alpha', 'Bravo', 'Charlie')
first_agent = agents[0]
print(first_agent)

# Question 2: Last Status
# Thought Process: The last item can be accessed with index 2 or index -1.
status = ('pending', 'in progress', 'complete')
last_status_positive = status[2]
last_status_negative = status[-1]
print(last_status_positive)
print(last_status_negative)

# Question 3: Third Number
# Thought Process: The third item is at index 2.
codes = (10, 20, 30, 40)
third_number = codes[2]
print(third_number)

# Question 4: Second to Last Record
# Thought Process: The second to last item is at index -2.
records = ('fileA', 'fileB', 'fileC')
second_to_last = records[-2]
print(second_to_last)

# Question 5: Decoding the Middle
# Thought Process: The slice starts at index 2 and ends before index 4.
data = ('start', 'end', 'key', 'code', 'final')
decoded_tuple = data[2:4]
print(decoded_tuple)

# Question 6: First Two Items
# Thought Process: We slice from the beginning up to, but not including, index 2.
data = ('101', '102', '103', '104')
first_two = data[:2]
print(first_two)

# Question 7: Slicing to the End
# Thought Process: We slice from index 1 to the end.
log = ('read', 'write', 'delete', 'commit')
last_three = log[1:]
print(last_three)

# Question 8: Every Other Entry
# Thought Process: We use a step of 2 to skip every other item.
entries = ('A', 'skip', 'B', 'skip', 'C')
decoded_entries = entries[::2]
print(decoded_entries)

# Question 9: Reverse the Tuple
# Thought Process: A step of -1 reverses the tuple.
numbers = (1, 2, 3, 4, 5)
reversed_numbers = numbers[::-1]
print(reversed_numbers)

# Question 10: Extracting the Year
# Thought Process: The year '2024' is at index 1.
report = ('Report', '2024', 'Confidential')
year = report[1]
print(year)


# ------------------------------------------------------------------------------
# Section 3: Using Tuple Methods
# ------------------------------------------------------------------------------

# Question 1: Count the Items
# Thought Process: We use the len() function to find the number of items.
tasks = ('recon', 'intel', 'report')
num_tasks = len(tasks)
print(num_tasks)

# Question 2: How Many Intel Reports?
# Thought Process: The .count() method counts the number of occurrences.
reports = ('intel', 'recon', 'intel', 'summary')
intel_count = reports.count('intel')
print(intel_count)

# Question 3: Find the Index
# Thought Process: The .index() method returns the index of the first match.
plan = ('step1', 'step2', 'step3')
index_of_step3 = plan.index('step3')
print(index_of_step3)

# Question 4: Unpack a Profile
# Thought Process: We assign the items of the tuple to new variables in order.
profile = ('Agent 007', 'Active', 'Alpha')
agent_name, agent_status, agent_codename = profile
print(agent_name, agent_status, agent_codename)

# Question 5: Count a Number
# Thought Process: The .count() method works for numbers too.
data = (1, 5, 2, 8, 5)
count_fives = data.count(5)
print(count_fives)

# Question 6: Find the First Occurrence
# Thought Process: The .index() method only finds the first occurrence.
locations = ('HQ', 'HQ', 'Safehouse', 'HQ')
first_hq_index = locations.index('HQ')
print(first_hq_index)

# Question 7: Check the Length
# Thought Process: We use len() to get the count and compare it to 2.
credentials = ('user', 'password')
is_two_items = len(credentials) == 2
print(is_two_items)

# Question 8: Multiple Unpacking
# Thought Process: We unpack the tuple into three separate variables.
address = ('123', 'Secret St.', 'Spyville')
number, street, city = address
print(city)

# Question 9: Count a String
# Thought Process: We use .count() to find how many times 'alert' appears.
log = ('alert', 'warning', 'alert')
alert_count = log.count('alert')
print(alert_count)

# Question 10: Find the Index of a Number
# Thought Process: We use .index() to find the index of the number 30.
numbers = (10, 20, 30, 40)
index_of_30 = numbers.index(30)
print(index_of_30)


# ------------------------------------------------------------------------------
# Section 4: The Immutable Challenge
# ------------------------------------------------------------------------------

# Question 1: The Failed Reassignment
# Thought Process: We're attempting to change a tuple item, which is not allowed.
# mission_status = ('pending', 'in progress')
# mission_status[0] = 'complete'
# The code above will raise a TypeError: 'tuple' object does not support item assignment.

# Question 2: The Failed Append
# Thought Process: We're attempting to add an item to a tuple, which is not
# a supported operation.
# agent_list = ('Alpha', 'Bravo')
# agent_list.append('Charlie')
# The code above will raise an AttributeError: 'tuple' object has no attribute 'append'.

# Question 3: The Failed Removal
# Thought Process: We're trying to remove an item from a tuple, which is
# not a supported operation.
# task_list = ('recon', 'intel')
# task_list.remove('recon')
# The code above will raise an AttributeError: 'tuple' object has no attribute 'remove'.

# Question 4: A Tuple with a Mutable Item
# Thought Process: While the tuple itself can't be changed, its items can be.
# Since the second item is a list, we can modify it.
confidential = ('Key-1', ['log_a', 'log_b'])
confidential[1].append('log_c')
print(confidential)

# Question 5: Converting to a List
# Thought Process: We can convert a tuple to a list, make changes, and
# convert it back to a tuple.
roster_tuple = ('Bond', 'M')
roster_list = list(roster_tuple)
roster_list.append('Q')
final_roster_tuple = tuple(roster_list)
print(final_roster_tuple)
