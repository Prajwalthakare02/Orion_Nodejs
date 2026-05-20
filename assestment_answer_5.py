# ==========================================
# Python Error Handling Demonstration
# ==========================================

print("=== Starting Error Handling Demonstration ===\n")

# --- 1. The try, except, else, finally Blocks ---
print("--- 1. Core Error Blocks ---")
def divide_numbers(a, b):
    print(f"Attempting to divide {a} by {b}...")
    try:
        result = a / b
    except ZeroDivisionError:
        print(" -> Error Caught: Cannot divide by zero!")
    else:
        print(f" -> Success! The result is {result}")
    finally:
        print(" -> [Finally Block]: Execution complete. Cleaning up resources...\n")

divide_numbers(10, 2)  # Will succeed (triggers else)
divide_numbers(10, 0)  # Will fail (triggers except)


# --- 2. Handling Specific Exceptions First ---
print("--- 2. Specific Exceptions vs General Exceptions ---")
def process_input(user_input):
    print(f"Processing input: '{user_input}'")
    try:
        number = int(user_input)
        result = 100 / number
        print(f" -> Result: {result}")
    except ValueError:
        print(" -> ValueError Caught: Please enter a valid integer, not a string.")
    except ZeroDivisionError:
        print(" -> ZeroDivisionError Caught: 100 cannot be divided by zero.")
    except Exception as e:
        # This catches anything else we didn't think of (Avoid putting this first!)
        print(f" -> General Exception Caught: Something went wrong: {e}")
    print("-" * 20)

process_input("hello")  # Triggers ValueError
process_input("0")      # Triggers ZeroDivisionError


# --- 3. Using the 'raise' Keyword for Business Rules ---
print("\n--- 3. Enforcing Business Logic with 'raise' ---")
def register_user(age):
    print(f"Attempting to register user with age: {age}")
    if age < 0:
        # Manually triggering an error for invalid logic
        raise ValueError("Business Rule Violation: Age cannot be negative.")
    elif age < 18:
        print(" -> User is a minor.")
    else:
        print(" -> User successfully registered.")

try:
    register_user(-5)
except ValueError as e:
    print(f" -> Caught Custom Error: {e}")


# --- 4. Custom Exception Classes ---
print("\n--- 4. Creating Custom Exceptions ---")
# Defining a custom error by inheriting from the base Exception class
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    print(f"Attempting to withdraw ${amount} from balance of ${balance}")
    if amount > balance:
        raise InsufficientFundsError(f"Withdrawal denied: Short by ${amount - balance}.")
    
    new_balance = balance - amount
    print(f" -> Success. New balance: ${new_balance}")
    return new_balance

try:
    withdraw(50, 100)
except InsufficientFundsError as e:
    print(f" -> Transaction Failed: {e}")

print("\n=== Demonstration Complete ===")