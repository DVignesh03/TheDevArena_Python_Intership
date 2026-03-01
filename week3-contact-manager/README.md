# Contact Management System

## Project Description
A comprehensive contact management system built with Python using dictionaries and functions. This system allows users to manage their contacts with full CRUD operations, search functionality, and data persistence.

## What I learned
1. **Functions**: Creating reusable, orgainized code blocks
2. **Dictionaries**: Storing and retrieving data using key-value pairs
3. **String methods**: Advanced text manipulation and formatting
4. **file operations**: Saving and loading data from JSON files
5. **Input validation**: Ensuring data quality preventing errors
6. **Error handling**: Gracefully handling unexpected situations

## Features
- Add new contacts with validation
- Search contacts by name (partial matching supported)
- Update existing contact information
- Delete contacts with confirmation
- View all contacts with information
- View all contacts in formatted display
- Save contacts to JSON file automatically
- Load contacts from file on startup
- Export contacts to CSV format
- Contact statistics and analytics
- Phone number and email validation
- User-friendly menu interface
- Error handling for all operations

## How to run
* Navigate to project folder
* Install the requirements
* run the program: `python contact_manager.py`

## Challenges & Solutions
**Challenge**: Handling duplicate contact names
**Solution**: Added option to view all matches and select which to update
**Challenge**: Phone number validation across different formats
**Solution**: Created flexible validation function supporting multiple formats
**Challenge**: Efficient search with partial matching
**Solution**: Used dictionary comprehension with lower() for case-insensitive search
**Challenge**: Data persistence
**Solution**: used json module with proper error handling for file operations