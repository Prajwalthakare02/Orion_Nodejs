# ==========================================
# Main Execution Script: Modules & Packages
# ==========================================

print("=== Starting Modules & Packages Demonstration ===\n")

# --- Section 1: Built-in Modules & Import Styles ---
print("--- 1. Utilizing Built-In Modules ---")

# Style A: Importing an entire module with an explicit Alias
import math as m
radius = 5
area = m.pi * (radius ** 2)
print(f" -> [Math Alias]: Area of circle with radius {radius} is {area:.2f}")

# Style B: Importing a specific object/function directly (Memory efficient)
from datetime import datetime
current_time = datetime.now()
print(f" -> [Specific Import]: Current Timestamp: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")

# Style C: Standard module import
import random
lucky_number = random.randint(1, 100)
print(f" -> [Standard Import]: Generated Random Lucky Number: {lucky_number}")
print("-" * 50)


# --- Section 2: Importing from a Custom Package ---
print("\n--- 2. Utilizing Custom Packages & Local Modules ---")

# Importing specific functions from our custom package directory structure
from finance_pkg.calculations import calculate_bonus, format_currency

base_salary = 75000
bonus_amount = calculate_bonus(base_salary)
total_payout = base_salary + bonus_amount

print(f"Base Salary: {format_currency(base_salary)}")
print(f" -> Calculated Payout Bonus: {format_currency(bonus_amount)}")
print(f"Total Professional Payout: {format_currency(total_payout)}")


# --- Section 3: Summary of Common Beginner Pitfalls ---
print("\n" + "="*50)
print("  Summary of Handled Beginner Mistakes")
print("="*50)
print("1. Wildcard Overuse (from module import *): Banned here because it causes namespace collisions.")
print("2. Module vs Package Confusion: 'calculations.py' is a single file (Module). 'finance_pkg' is the folder container (Package).")
print("3. Code Isolation: Separating calculations from main execution makes code highly scalable.")

print("\n=== Demonstration Complete ===")