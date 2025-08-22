# **Python File Handling: The Agent's Data Storage 💾**

Welcome back, Junior Agent\! Today, we're tackling **file handling**, a critical skill for any programmer. File handling is how your programs read from and write to files on a computer's disk. Think of it as an agent's ability to access and manage secret intelligence files, from classified reports to encrypted logs.

Python's built-in functions make file operations simple and secure. The core of file handling is the `open()` function.

-----

## **1. The `open()` and `close()` Functions**

To work with a file, you must first **open** it. The `open()` function creates a **file object** that acts as a link to the file on your disk. It takes two primary arguments: the file path and the **mode**.

  - `'r'`: **Read** mode (default). Opens the file for reading. The file must exist.
  - `'w'`: **Write** mode. Opens for writing. **Creates a new file or overwrites an existing one.**
  - `'a'`: **Append** mode. Opens for writing, adding new content to the end of the file. Creates a new file if it doesn't exist.
  - `'x'`: **Create** mode. Creates a new file. Raises an error if the file already exists.
  - `'t'`: **Text** mode (default). Used for text files.
  - `'b'`: **Binary** mode. Used for non-text files like images or executables.

After you're done with a file, you must always **close** it using the `.close()` method. This frees up system resources.

**Example Code:**

```python
# Create and write to a new file
file_handle = open('secret_message.txt', 'w')
file_handle.write("Intel acquired. Rendezvous at 22:00.")
file_handle.close()

# Read from the file we just created
file_handle = open('secret_message.txt', 'r')
content = file_handle.read()
print(content)
file_handle.close()
```

-----

## **2. The `with open()` Statement: The Safest Method**

Manually closing files can be error-prone. What if your program crashes before `file.close()` is called?

The **`with` statement** provides a safer, more robust way to handle files. It automatically closes the file for you, even if an error occurs. This is the **preferred method** for all file operations.

**Example Code:**

```python
# Write to a file using 'with'
with open('agent_log.txt', 'w') as f:
    f.write("Log started.\n")
    f.write("Mission successful.")

# Read from the file using 'with'
with open('agent_log.txt', 'r') as f:
    log_content = f.read()
    print(log_content)
```

-----

## **3. Handling Specific File Types: The Data Dossiers**

Raw text files are useful, but real-world data is often structured. Python has built-in modules for handling common file types like CSV, TSV, and JSON.

### **`.csv` (Comma-Separated Values) and `.tsv` (Tab-Separated Values)**

These are common formats for tabular data, like a spreadsheet. Python's built-in `csv` module simplifies reading and writing these files.

  - **CSV:** Uses commas to separate values.
  - **TSV:** Uses tabs (`\t`) to separate values. You can specify the delimiter in the `csv` module.

**Example Code:**

```python
import csv

# Writing to a CSV file
with open('agents.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['ID', 'Name', 'Status']) # Write header row
    writer.writerow(['001', 'Alpha', 'Active'])
    writer.writerow(['002', 'Bravo', 'Inactive'])

# Reading from a CSV file
with open('agents.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

### **`.json` (JavaScript Object Notation)**

JSON is a lightweight data-interchange format often used for web services and storing hierarchical data. Python's `json` module can easily convert Python dictionaries and lists into JSON format and vice-versa.

**Example Code:**

```python
import json

# Python dictionary to write to JSON
agent_data = {
    "codename": "Phoenix",
    "rank": "Commander",
    "clearance": 7,
    "active": True
}

# Writing to a JSON file
with open('agent_profile.json', 'w') as f:
    json.dump(agent_data, f, indent=4)

# Reading from a JSON file
with open('agent_profile.json', 'r') as f:
    read_data = json.load(f)
    print(read_data["codename"])
```

-----

## **Hands-On Exercises: Data Dossier Puzzles 🧩**

It's time to test your file handling skills.

### **1. Basic File Operations (`open`, `close`, `with`) (5 Exercises)**

1.  **Write a Mission Log:** Use `open()` and `.write()` to create a file named `mission_log.txt` and write the single line `"Mission start: 0800"`. Don't forget to `close()` the file.
2.  **Read a Secret Note:** Create a file named `note.txt` with the content `"The eagle has landed."`. Then, use `open()` and `.read()` to read the entire content and print it. Remember to `close()` the file.
3.  **Append a Log Entry:** Create a file `activity.txt` with the content `"1. Reconnaissance"`. Use `open()` in append mode (`'a'`) to add a new line `"2. Report findings"` to the file. Then, read and print the entire file to confirm.
4.  **Safe Reading:** Use the `with open()` statement to read from a file named `message.txt` that contains the text `"Secure the asset."`. Print the content.
5.  **Safe Writing:** Use the `with open()` statement to write the text `"Intel transfer complete."` into a file named `transfer.txt`.

### **2. Structured Data (`csv`, `json`) (5 Exercises)**

1.  **Write Agent CSV:** Use the `csv` module to create a file named `team_roster.csv`. Write the following data to it:
      - Header: `Agent_ID`, `Name`
      - Row 1: `A01`, `James`
      - Row 2: `A02`, `Maria`
2.  **Read Agent CSV:** Read the `team_roster.csv` file you just created. Use a `for` loop to iterate through the rows and print each one.
3.  **Write Mission JSON:** Create a dictionary `mission_details` with the keys `"mission"`, `"status"`, and `"priority"` and corresponding values `"Operation Falcon"`, `"active"`, and `1`. Use the `json` module and the `with` statement to write this dictionary to a file named `mission.json`.
4.  **Read Mission JSON:** Read the `mission.json` file you just wrote. Load the data into a Python dictionary and print the value associated with the `"priority"` key.
5.  **Handle a TSV File:** Create a file `secrets.tsv` with the following content (using tabs for separation):
    `Key\tValue`
    `Code\tRed`
    `Level\t7`
    Use the `csv` module with the `delimiter='\t'` argument to read this file and print each row.


