# ==============================================================================
# SOLUTIONS FOR HANDS-ON SETS EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 20 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: What are Sets?
# ------------------------------------------------------------------------------

# Question 1: Create a Briefing Set
# Thought Process: A set automatically removes duplicates. The second 'target info'
# will be discarded. The order may not be consistent.
briefing_points = {'target info', 'entry point', 'target info'}
print(briefing_points)

# Question 2: Mission Objectives
# Thought Process: We create a set with three unique string items.
mission_objectives = {'Secure', 'Sabotage', 'Destroy'}
print(mission_objectives)

# Question 3: Unique Agents
# Thought Process: We use the set() constructor to convert the list to a set,
# which automatically handles duplicates.
agent_list = ['Agent A', 'Agent B', 'Agent A']
unique_agents = set(agent_list)
print(unique_agents)

# Question 4: Codewords
# Thought Process: We create a set with two string items.
codewords = {'phoenix', 'chimera'}
print(codewords)

# Question 5: Empty Set
# Thought Process: To create an empty set, we must use the set() constructor.
# Using {} creates an empty dictionary.
no_intel = set()
print(no_intel)


# ------------------------------------------------------------------------------
# Section 2: Adding and Removing Items
# ------------------------------------------------------------------------------

# Question 1: Add a New Task
# Thought Process: We use the .add() method to add a single item.
tasks = {'recon', 'infiltrate'}
tasks.add('extract')
print(tasks)

# Question 2: Add a Duplicate
# Thought Process: The .add() method simply ignores duplicates without raising
# an error.
tasks = {'recon', 'infiltrate'}
tasks.add('infiltrate')
print(tasks)

# Question 3: Remove a Point
# Thought Process: The .remove() method removes a specific item.
points = {'A', 'B', 'C'}
points.remove('B')
print(points)

# Question 4: Pop a Random Item
# Thought Process: The .pop() method removes and returns an arbitrary item.
log = {'login', 'logout', 'failed login'}
popped_item = log.pop()
print(popped_item)

# Question 5: Add Multiple Items
# Thought Process: The .update() method can add multiple items from an iterable
# like a list or another set.
files = {'A', 'B'}
files.update(['C', 'D'])
print(files)


# ------------------------------------------------------------------------------
# Section 3: Set Operations
# ------------------------------------------------------------------------------

# Question 1: Combine Two Teams
# Thought Process: The .union() method combines all unique items from both sets.
team_alpha = {'Agent 001', 'Agent 002'}
team_bravo = {'Agent 002', 'Agent 003'}
all_agents = team_alpha.union(team_bravo)
print(all_agents)

# Question 2: Find Shared Agents
# Thought Process: The .intersection() method finds items common to both sets.
team_alpha = {'Agent 001', 'Agent 002'}
team_bravo = {'Agent 002', 'Agent 003'}
shared_agents = team_alpha.intersection(team_bravo)
print(shared_agents)

# Question 3: Agents on Team Alpha Only
# Thought Process: The .difference() method finds items in the first set but
# not in the second.
team_alpha = {'Agent 001', 'Agent 002'}
team_bravo = {'Agent 002', 'Agent 003'}
alpha_only = team_alpha.difference(team_bravo)
print(alpha_only)

# Question 4: Check for Disjoint Sets
# Thought Process: The .isdisjoint() method returns True if there are no
# common items.
active = {'A1', 'A2'}
inactive = {'A3', 'A4'}
are_disjoint = active.isdisjoint(inactive)
print(are_disjoint)

# Question 5: All Agents from Both Teams
# Thought Process: The `|` operator is a shorthand for the union() method.
team_alpha = {'Agent 001', 'Agent 002'}
team_bravo = {'Agent 002', 'Agent 003'}
all_agents = team_alpha | team_bravo
print(all_agents)


# ------------------------------------------------------------------------------
# Section 4: Other Useful Set Methods
# ------------------------------------------------------------------------------

# Question 1: Count the Unique Items
# Thought Process: A set automatically handles duplicates upon creation.
data = {'A', 'B', 'C', 'A'}
num_items = len(data)
print(num_items)

# Question 2: Check for an Item
# Thought Process: The `in` keyword is used for membership testing in a set.
inventory = {'lockpick', 'knife', 'flashlight'}
has_knife = 'knife' in inventory
print(has_knife)

# Question 3: Check for a Subset
# Thought Process: The .issubset() method checks if all items in one set
# are present in another.
required = {'stealth', 'hacking'}
agent_skills = {'stealth', 'hacking', 'combat'}
has_required_skills = required.issubset(agent_skills)
print(has_required_skills)

# Question 4: Check for a Superset
# Thought Process: The .issuperset() method checks if a set contains all
# the items of another set.
required = {'stealth', 'hacking'}
agent_skills = {'stealth', 'hacking', 'combat'}
is_superset = agent_skills.issuperset(required)
print(is_superset)

# Question 5: Clear the Intel
# Thought Process: The .clear() method removes all items from the set.
intel = {'classified', 'top_secret'}
intel.clear()
print(intel)
