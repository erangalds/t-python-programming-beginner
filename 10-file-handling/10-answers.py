# ==============================================================================
# SOLUTIONS FOR HANDS-ON FILE HANDLING EXERCISES
# ==============================================================================
# This document contains the Python code and a detailed thought process
# for each of the 10 story-based questions.
# The code is organized into sections that match the exercises.
# ==============================================================================

# Note: The file creation for each question is included in the solution for
# a self-contained, runnable example.

import csv
import json

# ------------------------------------------------------------------------------
# Section 1: Basic File Operations (`open`, `close`, `with`)
# ------------------------------------------------------------------------------

# Question 1: Write a Mission Log
# Thought Process: We open the file in write mode ('w'), write content, and then close it.
try:
    file = open('mission_log.txt', 'w')
    file.write("Mission start: 0800")
finally:
    file.close()

# Question 2: Read a Secret Note
# Thought Process: First, we create the file. Then, we open it in read mode ('r'), read
# the content, print it, and close the file.
with open('note.txt', 'w') as f:
    f.write("The eagle has landed.")

file = open('note.txt', 'r')
content = file.read()
print(content)
file.close()

# Question 3: Append a Log Entry
# Thought Process: We create the file first. Then we open it in append mode ('a')
# and use '\n' to add a new line before writing the new content.
with open('activity.txt', 'w') as f:
    f.write("1. Reconnaissance\n")

with open('activity.txt', 'a') as f:
    f.write("2. Report findings")

with open('activity.txt', 'r') as f:
    full_content = f.read()
    print(full_content)

# Question 4: Safe Reading
# Thought Process: The 'with' statement automatically handles opening and closing the file.
with open('message.txt', 'w') as f:
    f.write("Secure the asset.")
with open('message.txt', 'r') as f:
    content = f.read()
    print(content)

# Question 5: Safe Writing
# Thought Process: The 'with' statement is the standard for safe file writing.
with open('transfer.txt', 'w') as f:
    f.write("Intel transfer complete.")
print("File 'transfer.txt' written successfully.")

# ------------------------------------------------------------------------------
# Section 2: Structured Data (`csv`, `json`)
# ------------------------------------------------------------------------------

# Question 1: Write Agent CSV
# Thought Process: We use csv.writer to write rows to the file. 'newline=""'
# is a best practice to prevent blank rows.
with open('team_roster.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Agent_ID', 'Name'])
    writer.writerow(['A01', 'James'])
    writer.writerow(['A02', 'Maria'])
print("File 'team_roster.csv' written successfully.")

# Question 2: Read Agent CSV
# Thought Process: We use csv.reader to iterate through the rows of the CSV file.
with open('team_roster.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Question 3: Write Mission JSON
# Thought Process: The json.dump() function converts a Python dictionary to a JSON string
# and writes it to a file. 'indent=4' makes the file human-readable.
mission_details = {
    "mission": "Operation Falcon",
    "status": "active",
    "priority": 1
}
with open('mission.json', 'w') as jsonfile:
    json.dump(mission_details, jsonfile, indent=4)
print("File 'mission.json' written successfully.")

# Question 4: Read Mission JSON
# Thought Process: The json.load() function reads a JSON file and returns a
# Python dictionary.
with open('mission.json', 'r') as jsonfile:
    data = json.load(jsonfile)
    print(data["priority"])

# Question 5: Handle a TSV File
# Thought Process: The csv.reader can handle tab-separated values by setting the
# 'delimiter' parameter to '\t'.
with open('secrets.tsv', 'w', newline='') as tsvfile:
    tsv_writer = csv.writer(tsvfile, delimiter='\t')
    tsv_writer.writerow(['Key', 'Value'])
    tsv_writer.writerow(['Code', 'Red'])
    tsv_writer.writerow(['Level', '7'])

with open('secrets.tsv', 'r', newline='') as tsvfile:
    tsv_reader = csv.reader(tsvfile, delimiter='\t')
    for row in tsv_reader:
        print(row)
