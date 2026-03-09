import sys
from expenses import Expense, ExpenseManager
from file_handler import FileHandler
from reports import Reporter
import utils

def main():
    # 1. Initialize our "Database" and "File Brain"
    manager = ExpenseManager()
    handler = FileHandler()
    
    # 2. Load existing data on startup
    saved_data = handler.load_data()
    if "expenses" in saved_data:
        for e in saved_data["expenses"]:
            manager.add_expense(Expense(e['date'], e['amount'], e['category'], e['description']))
        manager.budgets = saved_data.get("budgets", {})

    while True:
        utils.clear_screen()
        print("="*40)
        print("   PERSONAL FINANCE TRACKER PRO")
        print("="*40)
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Reports & Trends")
        print("4. Budget Settings")
        print("5. Data Management (Backup/Export)")
        print("0. Exit")
        print("="*40)
        
        choice = input("Select an option: ").strip()

        if choice == "1":
            # --- ADD EXPENSE ---
            date = input("Date (YYYY-MM-DD) [Enter for Today]: ").strip() or utils.get_today()
            amount = utils.get_valid_float("Amount: ")
            category = input("Category (Food/Rent/Bills/etc.): ").strip().title()
            desc = input("Description: ").strip()
            
            manager.add_expense(Expense(date, amount, category, desc))
            handler.save_data(manager.expenses, manager.budgets)
            input("\n[+] Expense added! Press Enter to continue...")

        elif choice == "2":
            # --- VIEW & FILTER ---
            print("\n--- ALL EXPENSES ---")
            expenses = manager.get_all_expenses()
            if not expenses:
                print("No expenses recorded yet.")
            else:
                for i, e in enumerate(expenses, 1):
                    print(f"{i}. {e.date} | {e.category:<10} | ${e.amount:>8.2f} | {e.description}")
            input("\nPress Enter to return to menu...")

        elif choice == "3":
            # --- REPORTS SUBMENU ---
            print("\n1. Category Breakdown\n2. Monthly Spending Trends\n3. Budget Status")
            rep_choice = input("Select report: ")
            if rep_choice == "1":
                Reporter.generate_category_summary(manager.expenses)
            elif rep_choice == "2":
                Reporter.generate_monthly_trend(manager.expenses)
            elif rep_choice == "3":
                Reporter.generate_budget_report(manager)
            input("\nPress Enter to return...")

        elif choice == "4":
            # --- BUDGET SETTINGS ---
            cat = input("Enter category to set budget for: ").strip().title()
            limit = utils.get_valid_float(f"Monthly limit for {cat}: ")
            manager.set_budget(cat, limit)
            handler.save_data(manager.expenses, manager.budgets)
            print(f"[+] Budget for {cat} set to ${limit:.2f}")
            input("\nPress Enter...")

        elif choice == "5":
            # --- DATA MANAGEMENT ---
            print("\n1. Create Manual Backup\n2. Export to CSV")
            data_choice = input("Select action: ")
            if data_choice == "1":
                handler.create_backup()
            elif data_choice == "2":
                handler.export_to_csv(manager.get_all_expenses())
                print("[+] Exported to data/expenses_export.csv")
            input("\nPress Enter...")

        elif choice == "0":
            handler.save_data(manager.expenses, manager.budgets)
            print("Data saved. Goodbye!")
            sys.exit()

if __name__ == "__main__":
    main()