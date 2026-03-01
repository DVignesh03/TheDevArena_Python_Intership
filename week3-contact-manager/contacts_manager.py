import json
import re
from datetime import datetime
import csv
import os

FILENAME = "contacts_data.json"

# --- HELPERS & VALIDATION ---

def validate_PHnumber(phone):
    digits = re.sub(r'\D', '', phone)
    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None

def validate_Email(email):
    if not email: return True # Optional field
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# --- CORE CRUD FUNCTIONS ---

def add_contact(contacts):
    print("\n--- ADD NEW CONTACT ---")
    while True:
        name = input("Enter contact name: ").strip()
        if name: break
        print("Name cannot be empty!")

    while True:
        phone = input("Enter phone number: ").strip()
        is_valid, cleaned_phone = validate_PHnumber(phone)
        if is_valid:
            if cleaned_phone in contacts:
                print(f"[!] Phone number {cleaned_phone} already exists for {contacts[cleaned_phone]['name']}")
                return
            break
        print("Invalid phone number! (10-15 digits required)")
    
    while True:
        email = input("Enter email (Optional): ").strip()
        if not email or validate_Email(email): break
        print("Invalid email format!")

    address = input("Enter address (Optional): ").strip()
    group = input("Enter group (FRIENDS/WORK/FAMILY/OTHER): ").strip().title() or "Other"

    contacts[cleaned_phone] = {
        'name': name,
        'email': email if email else "N/A",
        'address': address if address else "N/A",
        'group': group,
        'created_at': datetime.now().isoformat()
    }
    print(f"<#> Contact '{name}' added successfully!")

def search_contacts(contacts):
    term = input("Enter name or phone to search: ").lower()
    results = {k: v for k, v in contacts.items() if term in v['name'].lower() or term in k}
    
    if not results:
        print("[-] No contacts found.")
    else:
        print(f"\nFound {len(results)} results:")
        for phone, info in results.items():
            print(f"Name: {info['name']} | Phone: {phone} | Group: {info['group']}")
    return results

def update_contact(contacts):
    print("\n--- UPDATE CONTACT ---")
    phone = input("Enter the phone number to update: ").strip()
    if phone not in contacts:
        print("[-] Contact not found.")
        return

    print(f"Updating: {contacts[phone]['name']}. (Press Enter to keep current value)")
    
    new_name = input(f"New Name [{contacts[phone]['name']}]: ").strip()
    if new_name: contacts[phone]['name'] = new_name
    
    new_email = input(f"New Email [{contacts[phone]['email']}]: ").strip()
    if new_email and validate_Email(new_email): contacts[phone]['email'] = new_email
    
    new_group = input(f"New Group [{contacts[phone]['group']}]: ").strip()
    if new_group: contacts[phone]['group'] = new_group.title()

    print("[+] Contact updated successfully!")

def delete_contact(contacts):
    print("\n--- DELETE CONTACT ---")
    phone = input("Enter the phone number to delete: ").strip()
    if phone in contacts:
        confirm = input(f"Are you sure you want to delete {contacts[phone]['name']}? [y/n]: ").lower()
        if confirm == 'y':
            del contacts[phone]
            print("[NOTICE] Contact deleted.")
    else:
        print("[ERROR] Contact not found.")

def display_all_contacts(contacts):
    if not contacts:
        print("\n[INFO] Contact list is empty.")
        return
    print("\n" + "=" * 85)
    print(f"{'Name':<20} | {'Phone':<15} | {'Group':<10} | {'Email'}")
    print("-" * 85)
    for phone, info in contacts.items():
        print(f"{info['name'][:20]:<20} | {phone:<15} | {info['group']:<10} | {info['email']}")
    print("=" * 85)

# --- ADVANCED FEATURES ---

def export_to_csv(contacts):
    if not contacts:
        print("[-] Nothing to export.")
        return
    try:
        with open("contacts_export.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Phone", "Name", "Email", "Group", "Address"])
            for phone, info in contacts.items():
                writer.writerow([phone, info['name'], info['email'], info['group'], info['address']])
        print("[+] Exported to contacts_export.csv successfully!")
    except Exception as e:
        print(f"[!] Export failed: {e}")

def view_statistics(contacts):
    if not contacts:
        print("[-] No data to show.")
        return
    groups = [info['group'] for info in contacts.values()]
    print("\n--- STATISTICS ---")
    print(f"Total Contacts: {len(contacts)}")
    for g in set(groups):
        print(f"- {g}: {groups.count(g)}")

# --- FILE OPERATIONS ---

def load_contacts():
    if not os.path.exists(FILENAME): return {}
    try:
        with open(FILENAME, 'r') as f:
            return json.load(f)
    except: return {}

def save_contacts(contacts):
    with open(FILENAME, 'w') as f:
        json.dump(contacts, f, indent=4)

# --- MAIN INTERFACE ---

def main():
    contacts = load_contacts()
    while True:
        print("\n" + "="*30 + "\n   Contact Manager System\n" + "="*30)
        print("1. Add New Contact\n2. Search Contacts\n3. Update Contact\n4. Delete Contact")
        print("5. View All Contacts\n6. Export to CSV\n7. View Statistics\n0. Exit")
        choice = input("\nEnter choice: ").strip()

        if choice == "1": add_contact(contacts)
        elif choice == "2": search_contacts(contacts)
        elif choice == "3": update_contact(contacts)
        elif choice == "4": delete_contact(contacts)
        elif choice == "5": display_all_contacts(contacts)
        elif choice == "6": export_to_csv(contacts)
        elif choice == "7": view_statistics(contacts)
        elif choice == "0":
            save_contacts(contacts)
            print("Data saved. Goodbye!")
            break
        else: print("[!] Invalid choice.")
        
        # Auto-save after every modification
        if choice in ["1", "3", "4"]:
            save_contacts(contacts)

if __name__ == "__main__":
    main()