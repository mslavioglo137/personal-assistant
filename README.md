# Personal Assistant

A command-line Personal Assistant developed in Python.

The application allows users to manage contacts and notes, store data between sessions, and quickly search information through a convenient command-line interface.

---

## Features

### 📇 Contact Management

* Add contacts
* Add full contacts with all information at once
* International phone number validation
* Add email addresses
* Add physical addresses
* Add birthdays
* Edit phone numbers
* Delete contacts
* Search contacts by name, phone number, email, or address
* Display upcoming birthdays within a specified number of days

### 📝 Notes Management

* Create notes
* Edit notes
* Delete notes
* Display all notes
* Search notes by title
* Clear all notes

### 🏷️ Tags

* Add tags to notes
* Search notes by tags
* Prevent duplicate tags

### 💾 Data Persistence

* Automatic saving using Pickle
* Contacts and notes remain available after application restart

---

## Installation

Clone the repository:

```bash
git clone https://github.com/mslavioglo137/personal-assistant.git
cd personal-assistant
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
python -m assistant.main
```

or

```bash
python3 -m assistant.main
```

---

## Available Commands

### 📇 Contacts

```text
add-full "name" phone email "address" birthday
add "name" phone
change "name" old_phone new_phone
phone "name"
all
find text
delete "name"
```

### 🎂 Birthdays

```text
add-birthday "name" DD.MM.YYYY
show-birthday "name"
birthdays days
```

### 📧 Additional Information

```text
add-email "name" email
add-address "name" "address"
```

### 📝 Notes

```text
add-note "title" content
show-notes
find-note "title"
edit-note "title" new_content
delete-note "title"
clear-notes
```

### 🏷️ Tags

```text
add-tag "title" tag
find-tag tag
```

### ⚙️ Other

```text
hello
help
close
exit
```

---

## Examples

Create a contact:

```text
add "Maryna Slavioglo" +380999076997
```

Create a contact with full information:

```text
add-full "Maryna Slavioglo" +380999076997 maryna@gmail.com "Valencia Spain" 26.10.1984
```

Create a note:

```text
add-note "Shopping List" Buy milk bread eggs and cheese
```

Add a tag:

```text
add-tag "Shopping List" food
```

Search notes by tag:

```text
find-tag food
```

Show birthdays for the next 30 days:

```text
birthdays 30
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* Pickle Serialization
* Git
* GitHub

---

## Author

**Maryna Slavioglo**

Python Programming Final Project

### Acknowledgements

Special thanks to ChatGPT for assistance with project planning, debugging, feature design, testing ideas, and documentation improvements during development. 
