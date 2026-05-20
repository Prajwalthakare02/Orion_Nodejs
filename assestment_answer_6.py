# ==========================================
# Python File Handling Demonstration
# ==========================================
import os

print("=== Starting File Handling Demonstration ===\n")
filename = "demo_data.txt"

# --- 1. Write Mode ('w') ---
# 'w' mode creates a new file or overwrites an existing one completely.
print("--- 1. Writing to a File ('w' mode) ---")
print(f"Creating '{filename}' and writing initial data...")

# Using the 'with' statement ensures the file is automatically closed.
with open(filename, 'w') as file:
    file.write("Hello! This is the first line of the file.\n")
    file.write("File handling in Python is powerful for permanent storage.\n")
print(" -> Write complete. File automatically closed.\n")


# --- 2. Append Mode ('a') ---
# 'a' mode adds new data to the end of the file without overwriting existing data.
print("--- 2. Appending to a File ('a' mode) ---")
print("Appending a new line to the existing file...")

with open(filename, 'a') as file:
    file.write("This line was appended later without deleting the old data.\n")
print(" -> Append complete.\n")


# --- 3. Read Mode ('r') ---
# 'r' mode opens the file for reading. It fails if the file doesn't exist.
print("--- 3. Reading from a File ('r' mode) ---")

# Method A: Read the entire file at once
print("[Reading Entire File]:")
with open(filename, 'r') as file:
    entire_content = file.read()
    print(entire_content)

# Method B: Read line by line (Better for large files)
print("[Reading Line by Line]:")
with open(filename, 'r') as file:
    line_number = 1
    for line in file:
        # strip() removes the extra newline character when printing
        print(f"Line {line_number}: {line.strip()}") 
        line_number += 1
print("\n -> Read complete.\n")


# --- 4. Handling Common Beginner Mistakes ---
print("--- 4. Handling Missing File Errors ---")
fake_filename = "does_not_exist.txt"
print(f"Attempting to read '{fake_filename}'...")

try:
    with open(fake_filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(" -> Error Caught: FileNotFoundError!")
    print(f" -> Explanation: You must handle missing files so the program doesn't crash.")

print("\n=== Demonstration Complete ===")