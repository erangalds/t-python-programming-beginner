# ==============================================================================
# SOLUTIONS FOR HANDS-ON DICTIONARIES EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 20 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: What are Dictionaries?
# ------------------------------------------------------------------------------

# Question 1: Creating an Agent Profile
# Thought Process: Dictionaries are created with curly braces {} and key-value
# pairs separated by a colon.
agent_profile = {'codename': 'Spectre', 'rank': 'Top Agent'}
print(agent_profile)

# Question 2: Mission Report
# Thought Process: We create a dictionary with string and integer values.
report = {'mission_id': 101, 'status': 'Success', 'location': 'HQ'}
print(report)

# Question 3: Login Credentials
# Thought Process: The keys and values are strings.
logins = {'user': 'admin', 'password': 'secure_pass'}
print(logins)

# Question 4: Mixed Data
# Thought Process: A dictionary can hold different data types.
status_update = {'date': '2023-10-27', 'threat_level': 8}
print(status_update)

# Question 5: Empty Dossier
# Thought Process: An empty dictionary is created with empty curly braces {}.
new_agent_dossier = {}
print(new_agent_dossier)


# ------------------------------------------------------------------------------
# Section 2: Accessing and Modifying Items
# ------------------------------------------------------------------------------

# Question 1: Accessing an Agent's Rank
# Thought Process: We access the value by putting the key in square brackets.
roster = {'Alpha': 'Rookie', 'Bravo': 'Veteran'}
bravo_rank = roster['Bravo']
print(bravo_rank)

# Question 2: Adding a New Agent
# Thought Process: We add a new key-value pair by assigning a value to a
# new key.
team = {'A1': 'Spy', 'A2': 'Analyst'}
team['A3'] = 'Sniper'
print(team)

# Question 3: Updating a Status
# Thought Process: We access an existing key and assign it a new value.
mission = {'objective': 'Secure', 'status': 'Pending'}
mission['status'] = 'Complete'
print(mission)

# Question 4: Accessing a Mission ID
# Thought Process: We access the value of the 'mission_id' key.
records = {'mission_id': 'M-77', 'agent': 'James'}
mission_id = records['mission_id']
print(mission_id)

# Question 5: Adding a New Field
# Thought Process: We add a new key-value pair to the dictionary.
config = {'server': 'main', 'port': 8080}
config['protocol'] = 'HTTP'
print(config)


# ------------------------------------------------------------------------------
# Section 3: Removing Items and Getting Keys/Values
# ------------------------------------------------------------------------------

# Question 1: Removing a Declassified Record
# Thought Process: The `del` keyword is used to remove a key-value pair.
classified = {'record1': 'data', 'record2': 'data', 'declassified': 'old'}
del classified['declassified']
print(classified)

# Question 2: Popping an Item
# Thought Process: The `.pop()` method removes the key and returns its value.
log = {'event1': 'login', 'event2': 'failed login'}
removed_value = log.pop('event2')
print(removed_value)

# Question 3: Getting All Keys
# Thought Process: The `.keys()` method returns a view of the dictionary's keys.
inventory = {'itemA': 1, 'itemB': 2}
all_keys = inventory.keys()
print(all_keys)

# Question 4: Getting All Values
# Thought Process: The `.values()` method returns a view of the values.
status_levels = {'A': 'High', 'B': 'Medium'}
all_values = status_levels.values()
print(all_values)

# Question 5: Getting All Items
# Thought Process: The `.items()` method returns a view of the key-value pairs.
report = {'agent': 'Alpha', 'status': 'Active'}
all_items = report.items()
print(all_items)


# ------------------------------------------------------------------------------
# Section 4: Other Useful Dictionary Methods
# ------------------------------------------------------------------------------

# Question 1: Count the Records
# Thought Process: The `len()` function returns the number of key-value pairs.
dossier = {'A': 'record', 'B': 'record', 'C': 'record'}
num_records = len(dossier)
print(num_records)

# Question 2: Safely Get a Value
# Thought Process: The `.get()` method is safer than direct access because it
# won't raise an error if the key is missing.
settings = {'timeout': 30, 'attempts': 3}
attempts = settings.get('attempts')
print(attempts)

# Question 3: Handle a Missing Key
# Thought Process: We can provide a default value to the `.get()` method.
settings = {'timeout': 30, 'attempts': 3}
user_id = settings.get('user_id', 'unknown')
print(user_id)

# Question 4: Update the Credentials
# Thought Process: The `.update()` method merges a dictionary into another.
credentials = {'user': 'agent_x'}
credentials.update({'password': 'secret'})
print(credentials)

# Question 5: Check for a Key
# Thought Process: The `in` keyword checks for the existence of a key.
mission_data = {'location': 'Paris', 'target': 'hotel'}
is_location_present = 'location' in mission_data
print(is_location_present)