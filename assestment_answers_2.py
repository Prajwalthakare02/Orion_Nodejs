# ==========================================
# Python Data Structures Assessment Solutions
# ==========================================

print("=== Starting Data Structures Assessment ===\n")

# --- Q1. Reference Behavior ---
print("--- Q1. Reference Behavior ---")
data = [1, 2, 3]
ref = data
ref.append(4)
print("Output:", data)

# --- Q2. Tuple and Mutability ---
print("\n--- Q2. Tuple and Mutability ---")
t = (1, [2, 3], 4)
t[1].append(5)
print("Output:", t)

# --- Q3. Dictionary Key Collision ---
print("\n--- Q3. Dictionary Key Collision ---")
d = {1: 'A', True: 'B', 1.0: 'C'}
print("Length:", len(d))
print("Dictionary:", d)

# --- Q4. Set Duplicate Handling ---
print("\n--- Q4. Set Duplicate Handling ---")
s = {1, 2, 3}
s.add(2)
s.add(4)
print("Output:", s)

# --- Q5. Invalid Dictionary Access ---
print("\n--- Q5. Invalid Dictionary Access ---")
student = {'name': 'John', 'age': 25}
try:
    print(student[0])
except KeyError as e:
    print(f"Expected Error Caught: KeyError - {e}")
    print("Explanation: Dictionaries are accessed by keys (like 'name'), not numerical indices.")

# --- Q6. Nested Data Access ---
print("\n--- Q6. Nested Data Access ---")
data_nested = {'users': ['A', 'B', 'C'], 'scores': (10, 20, 30)}
print("Output:", data_nested['users'][1], data_nested['scores'][2])

# --- Q7. Copy vs Reference ---
print("\n--- Q7. Copy vs Reference ---")
a = [1, 2, 3]
b = a.copy()
b.append(4)
print("Output a:", a, "| Output b:", b)

# --- Q8. Removing Duplicates using Set ---
print("\n--- Q8. Removing Duplicates using Set ---")
nums = [1, 2, 2, 3, 4, 4]
unique = list(set(nums))
print("Output:", unique)

# --- Q9. Dictionary Update ---
print("\n--- Q9. Dictionary Update ---")
d_update = {'a': 1, 'b': 2}
d_update['a'] = d_update.get('a', 0) + 5
print("Output:", d_update)

# --- Q10. Best Data Structure ---
print("\n--- Q10. Best Data Structure ---")
print("Answer: Set (Because duplicates are not allowed)")

# --- Q11. Shallow Copy Issue ---
print("\n--- Q11. Shallow Copy Issue ---")
data_shallow = {'a': [1, 2], 'b': [3, 4]}
copy_data = data_shallow.copy()
copy_data['a'].append(5)
print("Original Data Output:", data_shallow)

# --- Q12. Fixed Data Scenario ---
print("\n--- Q12. Fixed Data Scenario ---")
print("Answer: Tuple (Because GPS coordinates are fixed pairs and tuples are immutable)")

# --- Q13. Performance Comparison ---
print("\n--- Q13. Performance Comparison ---")
print("Answer: Set (Sets use hash tables offering O(1) lookups, while Lists are O(n))")

# --- Q14. List + Dictionary Access ---
print("\n--- Q14. List + Dictionary Access ---")
data_list_dict = [{'name': 'A'}, {'name': 'B'}]
print("Output:", data_list_dict[1]['name'])

# --- Q15. Invalid Set Element ---
print("\n--- Q15. Invalid Set Element ---")
try:
    s_invalid = set([[], []])
except TypeError as e:
    print(f"Expected Error Caught: TypeError - {e}")
    print("Explanation: Sets require hashable (immutable) elements. Lists cannot be placed inside sets.")

# --- Q16. Identify Data Structures ---
print("\n--- Q16. Identify Data Structures ---")
a_type = [1, 2, 3]
b_type = (1, 2, 3)
c_type = {'x': 1}
d_type = {1, 2, 3}
print(f"a is {type(a_type)}")
print(f"b is {type(b_type)}")
print(f"c is {type(c_type)}")
print(f"d is {type(d_type)}")

# --- Q17. Practical Program ---
print("\n--- Q17. Practical Program ---")
my_nums = [15, 20, 15, 30, 40]
clean_list = list(set(my_nums))
print(f"Original: {my_nums}")
print(f"Final unique list: {clean_list}")

# --- Q18. Dictionary Program ---
print("\n--- Q18. Dictionary Program ---")
student_data = {'name': 'Prajwal', 'marks': 88}
print(f"Initial: {student_data}")
student_data['marks'] = 95
print(f"Updated: {student_data}")

# --- Q19. Tuple Program ---
print("\n--- Q19. Tuple Program ---")
my_date = (2026, 5, 20)
print(f"Formatted Date: {my_date[0]}-{my_date[1]:02d}-{my_date[2]}")

# --- Q20. Mixed Structure Output ---
print("\n--- Q20. Mixed Structure Output ---")
data_mixed = {'a': [1, 2], 'b': (3, 4)}
print("Output:", data_mixed['a'][1] + data_mixed['b'][0])

print("\n=== Assessment Complete ===")