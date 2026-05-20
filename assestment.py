# ========================================================
# Python Standard Library: JSON and OS Modules Demonstration
# ========================================================

import os
import json

print("=== Starting Standard Library Demonstration ===\n")

# --- Section 1: Interacting with the OS Module ---
print("--- 1. Operating System Interactions (os module) ---")

# Getting and displaying the current working directory path
current_dir = os.getcwd()
print(f"Current Working Directory: {current_dir}")

# Defining target directory paths and file paths dynamically
target_folder = "storage_center"
target_file = os.path.join(target_folder, "payload.json")

# Checking if directory exists; if not, create it safely
if not os.path.exists(target_folder):
    print(f" -> Path '{target_folder}' not found. Creating directory...")
    os.makedirs(target_folder)
else:
    print(f" -> Directory '{target_folder}' already verified.")

print(f"Target File Pathway: {target_file}")
print("-" * 60)


# --- Section 2: In-Memory JSON (json.dumps vs json.loads) ---
print("\n--- 2. In-Memory JSON String Serialization ---")

# Initial Python Dictionary mapping user configurations
user_profile = {
    "username": "prajwal_dev",
    "access_level": "admin",
    "active_status": True,
    "metrics": [94.5, 88.2, 91.0]
}

# Serializing dictionary directly into an in-memory JSON formatted string
# 'dumps' stands for Dump String
json_string = json.dumps(user_profile, indent=4)
print("[Python Dict serialized to JSON String via json.dumps()]:")
print(json_string)

# Deserializing the JSON string back into an active Python Dictionary
# 'loads' stands for Load String
parsed_dict = json.loads(json_string)
print(f"\n -> Verification: Re-constructed data type is {type(parsed_dict)}")
print(f" -> Extracted Username: {parsed_dict['username']}")
print("-" * 60)


# --- Section 3: File-Based JSON (json.dump vs json.load) ---
print("\n--- 3. File-Based Disk I/O Serialization ---")

# BEGINNER TRAP AVOIDED: We use json.dump() without an 's' to write directly to files
print(f"Streaming data directly to disk at '{target_file}'...")
with open(target_file, 'w') as file_stream:
    json.dump(user_profile, file_stream, indent=4)
print(" -> Disk write completed successfully.")

# Verification step: Read and deserialize the JSON payload directly from disk
print(f"Reading data back from disk at '{target_file}'...")
if os.path.exists(target_file):
    with open(target_file, 'r') as file_stream:
        disk_data = json.load(file_stream) # Loading data structure directly from file stream
    print(" -> Disk read completed successfully.")
    print(f" -> Verified Content from File: Admin Status = {disk_data['active_status']}")
else:
    print(" -> Error: Target file could not be verified on disk.")


# --- Section 4: Summary of Common Beginner Pitfalls ---
print("\n" + "="*60)
print("  Summary of Handled Beginner Mistakes")
print("="*60)
print("1. Method Confusion (dump vs dumps): 'dumps' manipulates strings in memory. 'dump' handles file objects streaming to disk.")
print("2. Path Assumptions: Always use os.path.exists() before writing or reading files to prevent standard FileNotFoundError crashes.")
print("3. Hardcoded Paths: Using os.path.join() ensures paths resolve correctly across Windows, Mac, and Linux environments.")

print("\n=== Demonstration Complete ===")