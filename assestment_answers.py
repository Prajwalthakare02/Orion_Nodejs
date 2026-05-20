# ==========================================
# Python Basics Hiring Assessment Solutions
# ==========================================

print("=== Starting Assessment ===")

# --- Q1. Nested Conversion Trap ---
print("\n--- Q1. Nested Conversion Trap ---")
x = input("Q1 - Enter number (e.g., 3): ")
y = int(x * 2)
z = int(x) * 2
print("Output:", y, z)

# --- Q2. Power Operator Trap ---
print("\n--- Q2. Power Operator Trap ---")
a = 2
b = 3
result = a ** b ** 2
print("Output:", result)

# --- Q3. String Addition vs Number Addition ---
print("\n--- Q3. String Addition vs Number Addition ---")
num = input("Q3 - Enter number (e.g., 4): ")
print("Output string addition:", num + "5")
print("Output number addition:", int(num) + 5)

# --- Q4. Multi-Layer Conversion ---
print("\n--- Q4. Multi-Layer Conversion ---")
a = "4"
b = "5"
print("Output:", int(a + b) + int(a) * int(b))

# --- Q5. Boolean Conversion Trap ---
print("\n--- Q5. Boolean Conversion Trap ---")
print("Output:", bool("0") + bool(0) + bool(""))

# --- Q6. Negative Floor Division Trap ---
print("\n--- Q6. Negative Floor Division Trap ---")
print("Output floor division:", -7 // 2)
print("Output standard division:", -7 / 2)

# --- Q7. Input Duplication Trap ---
print("\n--- Q7. Input Duplication Trap ---")
num = input("Q7 - Enter number (e.g., 2): ")
print("Output concatenated int:", int(num + num))
print("Output added int:", int(num) + int(num))

# --- Q8. Operator Precedence ---
print("\n--- Q8. Operator Precedence ---")
a = 3
b = 2
c = 4
result = a + b * c ** b // a
print("Output:", result)

# --- Q9. Conversion Timing Trap ---
print("\n--- Q9. Conversion Timing Trap ---")
num = input("Q9 - Enter number (e.g., 3): ")
result = int(num * int(num))
print("Output:", result)

# --- Q10. Combined Expression ---
print("\n--- Q10. Combined Expression ---")
a = "2"
b = 3
result = int(a) + int(a * b) + int(a) * b
print("Output:", result)

# --- Q11. Error Identification ---
print("\n--- Q11. Error Identification ---")
value = input("Q11 - Enter value: ")
try:
    print(value / 2)
except TypeError as e:
    print(f"Expected Error Caught: TypeError - {e}")
    print("Explanation: You cannot divide a string from an input() by an integer.")

# --- Q12. Arithmetic with Conversion ---
print("\n--- Q12. Arithmetic with Conversion ---")
x = "12"
y = "3"
result = int(x) // int(y) + int(x) % int(y)
print("Output:", result)

# --- Q13. String and Arithmetic Mix ---
print("\n--- Q13. String and Arithmetic Mix ---")
x = "5"
print("Output:", x * 2 + str(3))

# --- Q14. Input Handling ---
print("\n--- Q14. Input Handling ---")
age = input("Q14 - Enter age (e.g., 25): ")
print("Next year age (String trap):", age + "1")
print("Correct next year age:", int(age) + 1)

# --- Q15. Operator Precedence and Brackets ---
print("\n--- Q15. Operator Precedence and Brackets ---")
a = 10
b = 3
print("Output 1:", a + b * 2)
print("Output 2:", (a + b) * 2)
print("Output 3:", a % b ** 2)

# --- Q16. Data Type Identification ---
print("\n--- Q16. Data Type Identification ---")
a = "25"
b = 25
c = 25.0
d = True
print(f"a = {a} is type: {type(a)}")
print(f"b = {b} is type: {type(b)}")
print(f"c = {c} is type: {type(c)}")
print(f"d = {d} is type: {type(d)}")

# --- Q17. Practical Program ---
print("\n--- Q17. Practical Program ---")
user_num = input("Enter a number to double: ")
print("Original number:", user_num)
print("Doubled as string result:", user_num * 2)
print("Doubled as numeric result:", int(user_num) * 2)

# --- Q18. Salary Calculation Program ---
print("\n--- Q18. Salary Calculation Program ---")
yearly_salary = float(input("Enter yearly salary: "))
monthly_salary = yearly_salary / 12
salary_with_bonus = yearly_salary + (yearly_salary * 0.10)
print(f"Monthly salary: {monthly_salary:.2f}")
print(f"Salary after 10% bonus: {salary_with_bonus:.2f}")

# --- Q19. User Profile Program ---
print("\n--- Q19. User Profile Program ---")
profile_name = input("Enter your name: ")
profile_age = input("Enter your age: ")
profile_height = input("Enter your height: ")
print(f"Profile: {profile_name} is {profile_age} years old and {profile_height} tall.")

# --- Q20. Mixed Behavior Output ---
print("\n--- Q20. Mixed Behavior Output ---")
x = "10"
y = 2
print("Output 1:", int(x) + y)
print("Output 2:", x * y)
print("Output 3:", int(x * y))

print("\n=== Assessment Complete ===")