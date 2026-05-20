# ==========================================
# Python Functions Assessment Solutions
# ==========================================

print("=== Starting Functions Assessment ===\n")

# --- Q1. Function Return Trap ---
print("--- Q1. Function Return Trap ---")
def func1(x):
    return x + 2
result = func1(func1(3))
print("Output:", result)

# --- Q2. Missing Return Behavior ---
print("\n--- Q2. Missing Return Behavior ---")
def add(a, b):
    print(a + b)
print("Output:")
result = add(2, 3)
print(result)

# --- Q3. Default Argument Override ---
print("\n--- Q3. Default Argument Override ---")
def power(x, y=2):
    return x ** y
try:
    print(power(3, None))
except TypeError as e:
    print(f"Expected Error Caught: TypeError - {e}")
    print("Explanation: Passing None overrides the default 2, and you cannot raise an int to the power of None.")

# --- Q4. Mutable Default Trap ---
print("\n--- Q4. Mutable Default Trap ---")
def append_item(item, lst=[]):
    lst.append(item)
    return lst
print("Output 1:", append_item(1))
print("Output 2:", append_item(2))

# --- Q5. Multiple Return Unpacking Error ---
print("\n--- Q5. Multiple Return Unpacking ---")
def get_vals():
    return 1, 2, 3
try:
    a, b = get_vals()
    print(a, b)
except ValueError as e:
    print(f"Expected Error Caught: ValueError - {e}")
    print("Explanation: The function returns 3 values, but we only provided 2 variables to unpack them into.")

# --- Q6. Function as Argument ---
print("\n--- Q6. Function as Argument ---")
def square(x):
    return x * x
def apply(f, val):
    return f(val)
print("Output:", apply(square, 4))

# --- Q7. Lambda Inside Function ---
print("\n--- Q7. Lambda Inside Function ---")
def calc(x):
    return (lambda y: y + x)(5)
print("Output:", calc(3))

# --- Q8. Shadowing Variable ---
print("\n--- Q8. Shadowing Variable ---")
def shadow_func(x):
    x = x + 5
    return x
x_val = 10
print("Output:", shadow_func(x_val), x_val)

# --- Q9. Nested Function Scope ---
print("\n--- Q9. Nested Function Scope ---")
def outer(x):
    def inner():
        return x * 2
    return inner()
print("Output:", outer(5))

# --- Q10. Return vs Print ---
print("\n--- Q10. Return vs Print ---")
def test():
    print('Hello')
print("Output:")
res = test()
print(res)

# --- Q11. Lambda with Condition ---
print("\n--- Q11. Lambda with Condition ---")
cond_func = lambda x: x if x > 5 else x * 2
print("Output:", cond_func(3), cond_func(6))

# --- Q12. Function Overwrite ---
print("\n--- Q12. Function Overwrite ---")
def greet():
    return 'Hi'
def greet():
    return 'Hello'
print("Output:", greet())

# --- Q13. Default Argument Evaluation ---
print("\n--- Q13. Default Argument Evaluation ---")
try:
    # We use exec() here because normally, Python crashes at the exact moment 
    # it tries to parse this definition, preventing the rest of the script from running.
    exec("def bad_func(a, b=a+1):\n    return b")
except NameError as e:
    print(f"Expected Error Caught: NameError - {e}")
    print("Explanation: Default arguments are evaluated at definition time. 'a' is not defined yet.")

# --- Q14. Tuple Return Usage ---
print("\n--- Q14. Tuple Return Usage ---")
def return_tup():
    return 2, 4
x_tup = return_tup()
print("Output:", x_tup * 2)

# --- Q15. Function Calling Order ---
print("\n--- Q15. Function Calling Order ---")
def a_func():
    return 5
def b_func():
    return a_func() + 2
print("Output:", b_func())

# --- Q16. Recursive Thinking ---
print("\n--- Q16. Recursive Thinking ---")
def recur_f(n):
    return n if n == 1 else n * recur_f(n - 1)
print("Output:", recur_f(3))

print("\n==========================================")
print("           SECTION B: PRACTICAL           ")
print("==========================================\n")

# --- Q17. Logical Function (Lambda) ---
print("--- Q17. Logical Function ---")
is_even = lambda x: x % 2 == 0
print("is_even(4):", is_even(4))
print("is_even(7):", is_even(7))

# --- Q18. Multi-Return Program ---
print("\n--- Q18. Multi-Return Program ---")
def analyze_list(data):
    total = sum(data)
    avg = total / len(data) if data else 0
    length = len(data)
    return total, avg, length

test_list = [10, 20, 30, 40]
print(f"Analyzing {test_list}:")
print("Result (Sum, Avg, Length):", analyze_list(test_list))

# --- Q19. Default + Input ---
print("\n--- Q19. Default + Input ---")
def greet_user(name='Guest'):
    print(f"Greeting: Hello, {name}!")

user_input = input("Enter a name (or press Enter to use default): ")
if user_input.strip():
    greet_user(user_input)
else:
    greet_user()

# --- Q20. Practical Function ---
print("\n--- Q20. Practical Function ---")
def get_powers(n):
    return n**2, n**3

num = 4
sq, cb = get_powers(num)
print(f"Number: {num}")
print(f"Square: {sq}, Cube: {cb}")

print("\n=== Assessment Complete ===")