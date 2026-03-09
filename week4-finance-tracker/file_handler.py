import json
import os
import shutil
import csv
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
    
    def export_to_csv(self, expenses, export_filename="data/expenses_report.csv"):
        """Exports the current expense list to a CSV file."""
        if not expenses:
            print("[!] No data to export.")
            return False
            
        try:
            with open(export_filename, mode='w', newline='') as f:
                writer = csv.writer(f)
                # Write the Header Row
                writer.writerow(["Date", "Amount", "Category", "Description"])
                
                # Write the Data Rows
                for e in expenses:
                    writer.writerow([e.date, e.amount, e.category, e.description])
            
            print(f"[SUCCESS] Data exported to {export_filename}")
            return True
        except IOError as e:
            print(f"[ERROR] CSV Export failed: {e}")
            return False