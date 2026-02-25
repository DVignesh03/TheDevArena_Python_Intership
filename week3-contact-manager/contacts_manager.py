# Contact Management System
# Week 3 project

import json
import re
from datetime import datetime
import csv

def validate_PHnumber(phone):
    # validate and clean input number
    digits = re.sub(r'\D', '', phone)

    if 10 <= len(digits) <= 15:
        return True, digits
    return False, None

def validate_Email(email):
    # validate E-mail format
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def add_contact(contacts):
    # add new contact to the phonebook
    print("\n--- ADD NEW CONTACT ---")

    # get user inputs
    while True:
        name = input("Enter contact name: ").strip()
        if name:
            if name in contacts:
                print(f"Contact {name} already exists!")
                choice = input("Do you want to update instead (y/n)? ").lower()
                if choice == 'y':
                    update_contact(contacts, name)
                    return contacts
            break
        print("Name cannot be empty!")

    while True:
        phone = input("Enter phone number: ").strip()
        is_valid, cleaned_phone = validate_PHnumber(phone)
        if is_valid:
            break
        print("Invalid phone number! RETRY")
    
    while True:
        email = input("Enter email (OPTIONAL, press Enter to skip): ").strip() or "Other"
        if not email or validate_Email(email):
            break
        print("Invalid email format!")

    # additional information
    address = input("Enter address (OPTIONAL): ").strip()
    group = input("Enter group (FREINDS/WORK/FAMILY/OTHERS): ").strip() or "Other"

    # Store in dictionary
    contacts[cleaned_phone] = {
        'name': name,
        'email': email if email else None,
        'address': address if address else None,
        'group': group,
        'created_at': datetime.now().isoformat(),
        'updated_at': datetime.now().isoformat()
    }

    print(f"<#> Contact '{name}' added successfully!")
    return contacts

def update_contact(contacts, name):
    # Update existing contact
    print ("\n--- UPDATING CONTACT '{name}' ---")
    print("NOTE: Press Enter to skip a field")
    
    while True:
        phone = input("Enter phone number: ").strip()
        if phone:
            is_valid, cleaned_phone = validate_PHnumber(phone)
            if is_valid:
                break
            print("Invalid phone number! RETRY")
        break

    while True:
        email = input("Enter Email: ").strip() or "Other"
        if not email or validate_Email(email):
            break
        print("Invalid email format!")
    
    address = input("Enter address (OPTIONAL): ").strip()
    group = input("Enter group (FREINDS/WORK/FAMILY/OTHERS): ").strip() or "Other"

    # updating the data
    contacts[cleaned_phone] = {
        'email': email if email else None,
        'address': address if address else None,
        'group': group,
        'updated_at': datetime.now().isoformat()
    }


def search_contacts(contacts, search_term):
    # Search contacts by name (partial match)
    search_term = search_term.lower()
    results = {}

    for name, info in contacts.items():
        if search_term in name.lower():
            results[name] = info
    
    return results

def display_search_results(results):
    # Display search results in formatted way
    if not results:
        print("No contacts found.")
        return
    
    print(f"\nFound {len(results)} contact(s):")
    print("-" * 50)

    for i, (name, info) in enumerate(results.items(), 1):
        print(f"{i}. {name}")
        print(f"   📞 Phone: {info['phone']}")
        if info['email']:
            print(f"   📧 Email: {info['email']}")
        if info['address']:
            print(f"   📍 Address: {info['address']}")
        print(f"   👥 Group: {info['group']}")
        print()