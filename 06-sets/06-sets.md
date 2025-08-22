# Python Sets: The Agent's Intel Briefing 🕵️‍♀️

Welcome back, Junior Agent\! Your next lesson is on **sets**, another fundamental data type in Python. Think of a set as a collection of unique, unordered pieces of intel. A set is most useful when you need to store a group of items and want to ensure there are no duplicates.

In Python, you create a set by placing a sequence of items inside curly braces `{...}`, but unlike dictionaries, there are no key-value pairs.

## 1. What are Sets?

A set is an **unordered collection of unique items**. This means two things:

1.  **Unique:** A set cannot contain duplicate values. If you try to add an item that already exists, the set will ignore it.
2.  **Unordered:** Items in a set do not have an index. You cannot access an item by its position, and the order of items may change.

Because they are unordered and unindexed, sets are not useful for storing data that needs a specific sequence or for retrieving a single item by its position. However, they are highly optimized for **membership testing** (checking if an item is in the set) and for performing mathematical operations like unions and intersections.

### Example Code:

```python
# A set of agent IDs (duplicates are automatically removed)
agent_ids = {'A-01', 'A-02', 'A-01', 'A-03'}
print(f"Agent IDs after creation: {agent_ids}")

# A set of mission objectives (unordered)
objectives = {'recon', 'infiltrate', 'exfil'}
print(f"Mission objectives: {objectives}")

# An empty set (must use set())
empty_briefing = set()
print(f"Empty briefing: {empty_briefing}")
```

-----

## 2. Adding and Removing Items ➕➖

Sets are **mutable**, so you can add and remove items after they've been created. Since sets are unordered, you can only add or remove a specific item, not one at a certain index.

### Example Code:

```python
# A set of current tasks
current_tasks = {'secure', 'report'}
print(f"Current tasks: {current_tasks}")

# Add a new task using .add()
current_tasks.add('monitor')
print(f"Tasks after adding 'monitor': {current_tasks}")

# Add a duplicate task (it will be ignored)
current_tasks.add('secure')
print(f"Tasks after trying to add 'secure' again: {current_tasks}")

# Remove a task using .remove()
current_tasks.remove('secure')
print(f"Tasks after removing 'secure': {current_tasks}")

# Remove a random item using .pop()
popped_task = current_tasks.pop()
print(f"Popped task: {popped_task}")
print(f"Tasks after popping: {current_tasks}")
```

-----

## 3. Set Operations: The Core of a Set's Power 💡

The most powerful feature of sets is their ability to perform mathematical set operations. These are essential for comparing and combining collections of data.

| Operator/Method    | What it does                                                                  |
| ------------------ | ----------------------------------------------------------------------------- |
| `union()` or `\|`  | Combines two sets, creating a new set with all unique items.                  |
| `intersection()` or `&` | Creates a new set with only the items that are present in both sets.     |
| `difference()` or `-`   | Creates a new set with items from the first set that are not in the second. |
| `isdisjoint()`     | Returns `True` if the two sets have no items in common.                       |

### Example Code:

```python
# Sets of agents for two different missions
mission_alpha = {'Agent Smith', 'Agent Jones', 'Agent Brown'}
mission_beta = {'Agent Brown', 'Agent Davis', 'Agent Wilson'}

# Union: All agents involved in either mission
all_agents = mission_alpha.union(mission_beta)
print(f"All agents involved: {all_agents}")

# Intersection: Agents on both missions
shared_agents = mission_alpha.intersection(mission_beta)
print(f"Agents on both missions: {shared_agents}")

# Difference: Agents only on Mission Alpha
alpha_only = mission_alpha.difference(mission_beta)
print(f"Agents only on Mission Alpha: {alpha_only}")

# Check if two sets are completely separate
are_disjoint = mission_alpha.isdisjoint(mission_beta)
print(f"Are the missions completely separate? {are_disjoint}")
```

-----

## 4. Other Useful Set Methods & Checks 🧹

| Method/Keyword  | What it does                                                              |
| --------------- | ------------------------------------------------------------------------- |
| `len()`         | Finds the **number of items** in the set.                                 |
| `in` keyword    | Checks if an item exists in the set. (Very fast\!)                         |
| `issubset()` or `<=` | Checks if all items of a set are in another set.                      |
| `issuperset()` or `>=` | Checks if a set contains all items of another set.                    |
| `.clear()`      | Removes all items from the set.                                           |

### Example Code:

```python
security_clearances = {'level_1', 'level_2', 'level_3'}
needed_clearances = {'level_1', 'level_2'}

# Get the length
num_levels = len(security_clearances)
print(f"Number of clearance levels: {num_levels}")

# Check for membership
is_level1_needed = 'level_1' in needed_clearances
print(f"Is level_1 needed? {is_level1_needed}")

# Check if one set is a subset of another
is_subset = needed_clearances.issubset(security_clearances)
print(f"Are all needed clearances available? {is_subset}")

# Check if a set is a superset
is_superset = security_clearances.issuperset(needed_clearances)
print(f"Do we have all needed clearances? {is_superset}")

# Clear the set
security_clearances.clear()
print(f"Clearances after wiping: {security_clearances}")
```

-----

## Hands-On Exercises: Briefing Room Puzzles 🧩

It's time to test your knowledge\! Use your new set skills to manage intel and complete these tasks.

### 1. What are Sets? (5 Exercises)

1.  **Create a Briefing Set:** Your briefing points are: `'target info'`, `'entry point'`, `'target info'`. Create a set `briefing_points` and print it. What happened to the duplicate?
2.  **Mission Objectives:** Create a set `mission_objectives` with the strings `'Secure', 'Sabotage', 'Destroy'`. Print the set.
3.  **Unique Agents:** A list of agents is `['Agent A', 'Agent B', 'Agent A']`. Convert this list to a set called `unique_agents` and print it to show only the unique names.
4.  **Codewords:** Create a set `codewords` with the strings `'phoenix'`, `'chimera'`. Print the set.
5.  **Empty Set:** You have no intel yet. Create an empty set called `no_intel` and print it.

### 2. Adding and Removing Items (5 Exercises)

1.  **Add a New Task:** The set of tasks is `tasks = {'recon', 'infiltrate'}`. Add a new task `'extract'` to the set. Print the set.
2.  **Add a Duplicate:** The set of tasks is `tasks = {'recon', 'infiltrate'}`. Try to add `'infiltrate'` again. Print the set and notice nothing changed.
3.  **Remove a Point:** The set of points is `points = {'A', 'B', 'C'}`. Remove `'B'` from the set. Print the set.
4.  **Pop a Random Item:** The set is `log = {'login', 'logout', 'failed login'}`. Use `.pop()` to remove a random item and print the removed item.
5.  **Add Multiple Items:** The set is `files = {'A', 'B'}`. Use `.update()` to add the items from a list `['C', 'D']`. Print the set.

### 3. Set Operations (5 Exercises)

1.  **Combine Two Teams:** Team Alpha is `{'Agent 001', 'Agent 002'}` and Team Bravo is `{'Agent 002', 'Agent 003'}`. Use a `union()` to find all unique agents across both teams.
2.  **Find Shared Agents:** Use the `intersection()` method on the two teams from the previous exercise to find the agents who are on both teams.
3.  **Agents on Team Alpha Only:** Use the `difference()` method on the two teams to find the agents who are only on Team Alpha.
4.  **Check for Disjoint Sets:** A set of active agents is `active = {'A1', 'A2'}` and a set of inactive agents is `inactive = {'A3', 'A4'}`. Use `isdisjoint()` to check if the sets are completely separate.
5.  **All Agents from Both Teams:** Use the `|` operator on the two team sets to get the union.

### 4. Other Useful Set Methods (5 Exercises)

1.  **Count the Unique Items:** The set is `data = {'A', 'B', 'C', 'A'}`. First, create the set, then use `len()` to find the number of unique items.
2.  **Check for an Item:** The set is `inventory = {'lockpick', 'knife', 'flashlight'}`. Use the `in` keyword to check if `'knife'` is in the set. Print `True` or `False`.
3.  **Check for a Subset:** A set of required skills is `required = {'stealth', 'hacking'}` and an agent's skills are `agent_skills = {'stealth', 'hacking', 'combat'}`. Use `issubset()` to check if the agent has all the required skills.
4.  **Check for a Superset:** Use `issuperset()` to check if `agent_skills` is a superset of `required` skills from the previous exercise.
5.  **Clear the Intel:** A set is `intel = {'classified', 'top_secret'}`. Use the `.clear()` method to empty the set. Print the result.

