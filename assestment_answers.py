# =======================================================
# Python Comprehensions & Functional Programming Solutions
# =======================================================

print("=== Starting Comprehensions & Functional Programming Demonstration ===\n")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# --- Section 1: Traditional Loop vs. List Comprehension ---
print("--- 1. Traditional Loop vs. List Comprehension ---")

# Method A: Traditional Imperative For-Loop
loop_squares = []
for num in [1, 2, 3, 4, 5]:
    loop_squares.append(num ** 2)
print("Traditional Loop Result:     ", loop_squares)

# Method B: Pythonic List Comprehension (Single optimized statement)
comp_squares = [num ** 2 for num in [1, 2, 3, 4, 5]]
print("List Comprehension Result:   ", comp_squares)
print("-" * 60)


# --- Section 2: Adding Conditions & Dictionary Comprehensions ---
print("\n--- 2. Conditionals & Dictionary Comprehensions ---")

# Filtering inside a list comprehension: Keep evens and square them
even_squares = [num ** 2 for num in numbers if num % 2 == 0]
print("Filtered Even Squares:       ", even_squares)

# Dictionary Comprehension: Mapping keys to calculated values instantly
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print("Dictionary Mapping (Name->Len):", name_lengths)
print("-" * 60)


# --- Section 3: Functional Programming (map, filter) vs Comprehensions ---
print("\n--- 3. Functional Programming (map & filter) ---")

base_data = [2, 4, 6, 8, 10]

# Using filter() to get values > 5, and map() to square them
# Lambda functions provide the inline execution logic
filtered_data = filter(lambda x: x > 5, base_data)
mapped_data = map(lambda x: x ** 2, filtered_data)

# BEGINNER TRAP ALERT: map and filter return lazy generators, not lists!
# We must explicitly convert them to lists to read the data.
print("Functional Pipeline Result:  ", list(mapped_data))

# The identical logic handled via a standard list comprehension for comparison
readable_comp = [x ** 2 for x in base_data if x > 5]
print("Equivalent Comp Result:      ", readable_comp)


# --- Section 4: Summary of Common Beginner Pitfalls ---
print("\n" + "="*60)
print("  Summary of Handled Beginner Mistakes")
print("="*60)
print("1. Lazy Evaluation Pitfall: Forgetting that map() and filter() output memory iterators until cast to a list().")
print("2. Overcomplicating Comprehensions: If a comprehension requires multiple lines or nested conditions, use a standard loop to preserve readability.")
print("3. Write-Only Code: Comprehensions should simplify syntax, not obscure it. Readability always wins in production ecosystems.")

print("\n=== Demonstration Complete ===")