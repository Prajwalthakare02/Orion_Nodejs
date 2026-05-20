# Custom Module inside the finance_pkg folder

def calculate_bonus(salary):
    """
    Business rule logic isolated inside a custom module.
    """
    return salary * 0.10

def format_currency(amount):
    """
    Helper function to clean up financial display.
    """
    return f"₹{amount:,.2f}"