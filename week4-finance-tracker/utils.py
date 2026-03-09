import os

def get_valid_float(prompt):
    """Ensures the user enters a valid decimal number for amounts."""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("[!] Amount cannot be negative.")
                continue
            return value
        except ValueError:
            print("[!] Invalid input. Please enter a number.")

def format_currency(amount):
    """Simple helper to keep currency display consistent."""
    return f"${amount:,.2f}"

def clear_screen():
    """Clears the terminal screen based on the OS."""
    os.system('cls' if os.name == 'nt' else 'clear')