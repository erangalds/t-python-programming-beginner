# ==============================================================================
# SOLUTIONS FOR HANDS-ON LOOPS EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 15 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# ------------------------------------------------------------------------------
# Section 1: `for` Loops
# ------------------------------------------------------------------------------

# Question 1: Iterate Over a Team
# Thought Process: The 'for' loop assigns each item in the list to the variable 'agent'
# one by one.
agents = ['Alpha', 'Bravo', 'Charlie']
for agent in agents:
    print(agent)

# Question 2: Count Down
# Thought Process: We use range(start, stop, step) to count backwards. The stop
# value is exclusive.
for i in range(5, 0, -1):
    print(i)

# Question 3: Process Mission Reports
# Thought Process: We iterate through the list and print a formatted string for each item.
reports = ['Report A', 'Report B', 'Report C']
for report in reports:
    print(f"Processing: {report}")

# Question 4: Count Up
# Thought Process: We use range(stop) which starts at 0 and goes up to (but not including) 5.
for i in range(5):
    print(i)

# Question 5: Iterate Over a String
# Thought Process: Strings are sequences, so a 'for' loop can iterate over their characters.
word = "secret"
for char in word:
    print(char)

# ------------------------------------------------------------------------------
# Section 2: `while` Loops
# ------------------------------------------------------------------------------

# Question 1: Password Attempts
# Thought Process: The loop continues as long as attempts_left is positive.
# We must decrement attempts_left inside the loop to avoid an infinite loop.
attempts_left = 3
while attempts_left > 0:
    print("Attempting to connect...")
    attempts_left -= 1

# Question 2: Waiting for Data
# Thought Process: The loop runs until the boolean condition becomes True.
data_received = False
# In a real scenario, this would be a real data check, here we simulate it
temp_counter = 0
while not data_received:
    print("Waiting for data...")
    temp_counter += 1
    if temp_counter == 1:
        data_received = True
print("Data received.")

# Question 3: Intel Download
# Thought Process: The loop runs until progress is no longer less than 100.
progress = 0
while progress < 100:
    print(f"Download progress: {progress}%")
    progress += 20
print(f"Download progress: {progress}%")

# Question 4: Security Check
# Thought Process: The loop continues as long as the threat_level is positive.
threat_level = 5
while threat_level > 0:
    print(f"Threat level is high. Engaging protocols...")
    threat_level -= 1
print("Threat level is nominal.")

# Question 5: Infinite Loop (with a catch)
# Thought Process: The 'break' statement is used to exit the loop after a condition is met.
counter = 0
while True:
    print("Scanning...")
    counter += 1
    if counter >= 3:
        print("Scan complete. Breaking loop.")
        break

# ------------------------------------------------------------------------------
# Section 3: Controlling Loops
# ------------------------------------------------------------------------------

# Question 1: Break on Target Found
# Thought Process: The loop checks each item, and if the condition is met, it stops
# with 'break'.
locations = ['A', 'B', 'C', 'TARGET', 'D']
for location in locations:
    if location == 'TARGET':
        print("Target found! Mission complete.")
        break
    print(f"Checking location: {location}")

# Question 2: Continue on Error
# Thought Process: 'continue' skips the rest of the current iteration and moves to the next.
log = ['OK', 'ERROR', 'OK', 'ERROR', 'OK']
for entry in log:
    if entry == 'ERROR':
        print("Skipping error...")
        continue
    print(f"Processing log: {entry}")

# Question 3: Password Attempts (with break)
# Thought Process: The loop breaks early once the password is "guessed".
password_guess = "secret_code"
for attempt in range(1, 4):
    print(f"Attempt number {attempt}...")
    if attempt == 2:
        if password_guess == "secret_code": # Check if the guess matches
            print("Password accepted!")
            break
else:
    print("Out of attempts.")

# Question 4: Skip Odd Numbers
# Thought Process: We check for an odd number using the modulo operator (%) and
# use 'continue' to skip the print statement.
for number in range(1, 10):
    if number % 2 != 0:
        continue
    print(number)

# Question 5: Search and Exit
# Thought Process: The loop will go through each item, and if a 'high' threat is found,
# it will stop immediately.
threats = ['low', 'low', 'high', 'low']
for threat in threats:
    print(f"Threat level: {threat}")
    if threat == 'high':
        print("High threat detected, aborting mission!")
        break
