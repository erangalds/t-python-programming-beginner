# Python Dictionaries: The Agent's Dossier 🕵️‍♀️

Welcome back, Junior Agent\! Your next lesson is on **dictionaries**, a powerful Python data type. Think of a dictionary as an agent's dossier, where each piece of information is organized with a clear label. Instead of using a numbered index, you access information using a unique **key**.

In Python, you create a dictionary by placing a sequence of `key: value` pairs inside curly braces `{...}`, with each pair separated by a comma.

## 1. What are Dictionaries?

A dictionary is a collection of **key-value pairs**. Each `key` is a unique identifier (like a name or ID number), and it's associated with a `value` (like an agent's name or a mission status). Unlike lists, dictionaries are **unordered** and **mutable**, meaning you can change, add, or remove entries after the dictionary is created.

**Example Code:**

```python
# A dictionary of agent IDs and their codenames
agent_dossier = {
    'ID-001': 'Agent Alpha',
    'ID-002': 'Agent Bravo',
    'ID-003': 'Agent Charlie'
}
print(f"Agent dossier: {agent_dossier}")

# A dictionary with mixed data types
mission_status = {
    'mission_name': 'Operation Shadow',
    'status': 'In Progress',
    'progress_percent': 75
}
print(f"Mission status: {mission_status}")

# An empty dictionary
empty_folder = {}
print(f"Empty folder: {empty_folder}")
```



## 2. Accessing and Modifying Items: Looking Up Information 🔍

To access a value in a dictionary, you use its associated key inside square brackets `[...]`. This is different from lists, where you use a numerical index. You can also easily add new key-value pairs or update the value of an existing key.

**Example Code:**

```python
agent_dossier = {'ID-001': 'Agent Alpha', 'ID-002': 'Agent Bravo'}

# Access a value using its key
agent_name = agent_dossier['ID-001']
print(f"Agent name for ID-001: {agent_name}")

# Add a new key-value pair
agent_dossier['ID-003'] = 'Agent Charlie'
print(f"Updated dossier after adding a new agent: {agent_dossier}")

# Update the value for an existing key
agent_dossier['ID-002'] = 'Agent Beta'
print(f"Updated dossier after reassigning ID-002: {agent_dossier}")
```



## 3. Removing Items and Getting Keys/Values 🗑️

You have a few ways to remove information from a dictionary. You can also get a view of all the keys, all the values, or all the key-value pairs in the dictionary.

**Example Code:**

```python
mission_records = {
    'recon': 'Complete',
    'infiltration': 'In Progress',
    'extraction': 'Pending'
}

# Remove a key-value pair using `del`
del mission_records['recon']
print(f"Records after deleting 'recon': {mission_records}")

# Remove a key and get its value using `.pop()`
status = mission_records.pop('infiltration')
print(f"Popped status: {status}")
print(f"Records after popping 'infiltration': {mission_records}")

# Get a view of all keys
all_keys = mission_records.keys()
print(f"All keys: {all_keys}")

# Get a view of all values
all_values = mission_records.values()
print(f"All values: {all_values}")

# Get a view of all key-value pairs
all_items = mission_records.items()
print(f"All items: {all_items}")
```



## 4. Other Useful Dictionary Methods 🔧

Dictionaries come with a handful of methods that make them incredibly useful for managing data.

| Method           | What it does                                                                  |
| ---------------- | ----------------------------------------------------------------------------- |
| `len()`          | Finds the **number of key-value pairs** in the dictionary.                    |
| `.get()`         | Retrieves a value for a key, but returns `None` (or a default) if the key doesn't exist. |
| `.update()`      | Merges another dictionary or key-value pairs into the current one. |
| `.clear()`       | Removes all key-value pairs from the dictionary. |
| `in` keyword     | Checks if a key exists in the dictionary. |

**Example Code:**

```python
agent_logins = {'alpha_001': 'secure_pass', 'bravo_002': 'top_secret'}

# Get the length
num_logins = len(agent_logins)
print(f"Number of logins: {num_logins}")

# Use .get() to safely retrieve a value
status_code = agent_logins.get('bravo_002')
print(f"Status for bravo_002: {status_code}")

# Get a non-existent key with a default value
non_existent = agent_logins.get('charlie_003', 'Not found')
print(f"Status for charlie_003: {non_existent}")

# Update the dictionary
new_logins = {'delta_004': 'classified'}
agent_logins.update(new_logins)
print(f"Logins after update: {agent_logins}")

# Check if a key exists
is_alpha_present = 'alpha_001' in agent_logins
print(f"Is alpha_001 present? {is_alpha_present}")

# Clear the dictionary
agent_logins.clear()
print(f"Logins after clearing: {agent_logins}")
```



## Hands-On Exercises: Dossier Puzzles 🧩

It's time for your mission\! Use your new dictionary skills to manage agent dossiers and complete these tasks.

### 1. What are Dictionaries? (5 Exercises)

1.  **Creating an Agent Profile:** An agent's profile includes a `codename` of `'Spectre'` and a `rank` of `'Top Agent'`. Create a dictionary called `agent_profile` with these two key-value pairs and print it.
2.  **Mission Report:** Create a dictionary `report` with `mission_id` as `101`, `status` as `'Success'`, and `location` as `'HQ'`. Print the dictionary.
3.  **Login Credentials:** Create a dictionary `logins` with two key-value pairs: `user` with the value `'admin'` and `password` with the value `'secure_pass'`. Print the dictionary.
4.  **Mixed Data:** Create a dictionary `status_update` with a `date` of `'2023-10-27'` and `threat_level` of `8`. Print the dictionary.
5.  **Empty Dossier:** You have an empty file for a new agent. Create an empty dictionary called `new_agent_dossier` and print it.

### 2. Accessing and Modifying Items (5 Exercises)

1.  **Accessing an Agent's Rank:** The dictionary is `roster = {'Alpha': 'Rookie', 'Bravo': 'Veteran'}`. Access and print the rank of `'Bravo'`.
2.  **Adding a New Agent:** The dictionary is `team = {'A1': 'Spy', 'A2': 'Analyst'}`. Add a new agent with the key `'A3'` and the value `'Sniper'`. Print the updated dictionary.
3.  **Updating a Status:** The dictionary is `mission = {'objective': 'Secure', 'status': 'Pending'}`. Change the `status` to `'Complete'`. Print the dictionary.
4.  **Accessing a Mission ID:** The dictionary is `records = {'mission_id': 'M-77', 'agent': 'James'}`. Access and print the `mission_id`.
5.  **Adding a New Field:** The dictionary is `config = {'server': 'main', 'port': 8080}`. Add a new field with the key `'protocol'` and value `'HTTP'`. Print the updated dictionary.

### 3. Removing Items and Getting Keys/Values (5 Exercises)

1.  **Removing a Declassified Record:** The dictionary is `classified = {'record1': 'data', 'record2': 'data', 'declassified': 'old'}`. Use `del` to remove the `'declassified'` record. Print the dictionary.
2.  **Popping an Item:** The dictionary is `log = {'event1': 'login', 'event2': 'failed login'}`. Use `.pop()` to remove the `'event2'` item and print the removed value.
3.  **Getting All Keys:** The dictionary is `inventory = {'itemA': 1, 'itemB': 2}`. Use the `.keys()` method to get all the keys. Print the result.
4.  **Getting All Values:** The dictionary is `status_levels = {'A': 'High', 'B': 'Medium'}`. Use the `.values()` method to get all the values. Print the result.
5.  **Getting All Items:** The dictionary is `report = {'agent': 'Alpha', 'status': 'Active'}`. Use the `.items()` method to get all the key-value pairs. Print the result.

### 4. Other Useful Dictionary Methods (5 Exercises)

1.  **Count the Records:** The dictionary is `dossier = {'A': 'record', 'B': 'record', 'C': 'record'}`. Use `len()` to find the number of records.
2.  **Safely Get a Value:** The dictionary is `settings = {'timeout': 30, 'attempts': 3}`. Use `.get()` to retrieve the value for `'attempts'`.
3.  **Handle a Missing Key:** Use `.get()` on the same `settings` dictionary to retrieve a non-existent key, like `'user_id'`, and provide a default value of `'unknown'`. Print the result.
4.  **Update the Credentials:** The dictionary is `credentials = {'user': 'agent_x'}`. Use `.update()` to add a new key-value pair `{'password': 'secret'}`. Print the updated dictionary.
5.  **Check for a Key:** The dictionary is `mission_data = {'location': 'Paris', 'target': 'hotel'}`. Use the `in` keyword to check if the key `'location'` exists in the dictionary. Print `True` or `False`.

-----

