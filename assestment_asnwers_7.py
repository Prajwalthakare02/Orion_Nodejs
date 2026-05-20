# ==========================================
# Python Object-Oriented Programming (OOP)
# ==========================================

print("=== Starting OOP Demonstration ===\n")

# --- Section 1: The Base Class (The Blueprint) ---
print("--- 1. Base Class & Object Instantiation ---")

class Vehicle:
    """
    Acts as a blueprint for any standard vehicle.
    """
    # The Constructor (__init__) initializes the object's data
    # 'self' represents the specific instance of the object being created
    def __init__(self, brand, model):
        self.brand = brand          # Instance Attribute
        self.model = model          # Instance Attribute
        self.speed = 0              # Default starting attribute

    # Method defining object behavior
    def accelerate(self, amount):
        self.speed += amount
        print(f" -> The {self.brand} {self.model} accelerated by {amount} km/h. Current Speed: {self.speed} km/h.")

    def brake(self):
        self.speed = 0
        print(f" -> The {self.brand} {self.model} came to a complete stop.")

# Creating real-world instances (Objects) from the class blueprint
print("Instantiating 'car1' as a Tesla Model 3...")
car1 = Vehicle("Tesla", "Model 3")  

# Triggering behaviors on the object
car1.accelerate(50)
car1.accelerate(30)
car1.brake()
print("-" * 40)


# --- Section 2: Inheritance & Extension ---
print("\n--- 2. Inheritance and the super() Function ---")

# ElectricVehicle is a child class that inherits from the Vehicle parent class
class ElectricVehicle(Vehicle):
    """
    Inherits core features from Vehicle, but extends functionality for EVs.
    """
    def __init__(self, brand, model, battery_capacity):
        # BEGINNER TRAP ALERT: Forgetting to call the parent constructor!
        # super() references the parent class, allowing us to reuse its initialization logic.
        super().__init__(brand, model)
        
        # Adding a unique attribute specific ONLY to child instances
        self.battery_capacity = battery_capacity 
        self.battery_level = 100

    # Adding a unique behavior specific ONLY to child instances
    def charge_battery(self):
        self.battery_level = 100
        print(f" -> Charging completed. The {self.brand}'s {self.battery_capacity} kWh battery is full.")

    # Demonstrating Method Overriding (Modifying parent behavior)
    def accelerate(self, amount):
        self.speed += amount
        self.battery_level -= (amount * 0.1) # EVs lose battery when accelerating
        print(f" -> [EV Mode] {self.brand} surged forward! Speed: {self.speed} km/h | Battery: {self.battery_level}%")

print("Instantiating 'ev1' as a Tata Nexon EV...")
ev1 = ElectricVehicle("Tata", "Nexon EV", "40.5")

# ev1 uses the OVERRIDDEN accelerate method
ev1.accelerate(60)

# ev1 uses the UNIQUE child method
ev1.charge_battery()

# ev1 still has access to base methods from the parent class that weren't overridden
ev1.brake()


# --- Section 3: Summary of Beginner Pitfalls ---
print("\n" + "="*40)
print("  Summary of Handled Beginner Mistakes")
print("="*40)
print("1. Forgetting 'self': Methods require 'self' as their first argument so they know which object instance to modify.")
print("2. Missing super(): Without super().__init__(), child classes will fail to inherit attributes initialized in the base class.")
print("3. Class vs Object Confusion: 'Vehicle' is the cookie-cutter (Class). 'car1' is the actual cookie (Object).")

print("\n=== Demonstration Complete ===")