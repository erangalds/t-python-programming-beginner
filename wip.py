# Let's get the word "CODE" out of a longer string
full_message = "ENCRYPT_CODE_MESSAGE"
# The word "CODE" starts at index 8 and ends just before index 12
secret_code = full_message[8:12]
print(f"The secret code is: {secret_code}")

# Slice from the beginning to a specific index (index 7)
first_part = full_message[:7]
print(f"The first part is: {first_part}")

# Slice from a specific index (index 13) to the end
last_part = full_message[13:]
print(f"The last part is: {last_part}")

# Grab every other letter using a step of 2
hidden_message = "S E C R E T"
every_other = hidden_message[::2]
print(f"The hidden message is: {every_other}")

# Get every third character, starting from the second character (index 1)
agent_list = "Agent_Alpha_Beta_Gamma"
third_letters = agent_list[1::3]
print(f"The third letters are: {third_letters}")

# Slice a specific range with a step
coordinates = "34.0522, -118.2437"

# This gets the numbers, skipping the comma and space
numbers_only = coordinates[2:17:3]
print(f"The coordinates numbers are: {numbers_only}")

# Using a negative step to reverse a string
password = "SECRET"
reversed_password = password[::-1]
print(f"The reversed password is: {reversed_password}")

# Grabbing a slice from the end of the string
full_report = "Mission Report 2025-08-01"
year = full_report[-10:-6]
print(f"The year of the report is: {year}")

# Slicing with a negative start and positive end index
coded_message = "DECODING_IN_PROGRESS"
slice_part = coded_message[-10:14]
print(f"The sliced part is: {slice_part}")