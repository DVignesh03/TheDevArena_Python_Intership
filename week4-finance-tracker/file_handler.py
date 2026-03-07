import json
import os
import shutil
from datetime import datetime

class FileHandler:
    def __init__(self, filename="data/expenses.json"):
        self.filename = filename
        # Ensure the data directory exists
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)

    def save_data(self, expenses, budgets):
        """Converts Expense objects to dicts and saves to JSON."""
        try:
            data = {
                    "expenses": [e.to_dict() for e in expenses],
                    "budgets": budgets
            }
            with open(self.filename, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"[ERROR] Save failed: {e}")
            return False

    def load_data(self):
        """Loads data from JSON and returns a list of dictionaries."""
        if not os.path.exists(self.filename):
            return []
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return []

    def create_backup(self):
        """Creates a timestamped backup of the current data file."""
        if not os.path.exists(self.filename):
            return False
        
        backup_dir = "data/backups"
        os.makedirs(backup_dir, exist_ok=True)
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = f"{backup_dir}/expenses_backup_{timestamp}.json"
        
        shutil.copy2(self.filename, backup_path)
        print(f"[SUCCESS] Backup created at: {backup_path}")
        return True