# Personal Assistant

A command-line Personal Assistant developed in Python.

The application allows users to manage contacts and notes, store data between sessions, and search information quickly through a convenient command-line interface.

## Features

### Contact Management

* Add contacts
* Store phone numbers
* International phone number validation
* Add email addresses
* Add physical addresses
* Add birthdays
* Edit contact information
* Delete contacts
* Search contacts by name, phone number, email, or address
* Display upcoming birthdays within a specified number of days

### Notes Management

* Create notes
* Edit notes
* Delete notes
* Display all notes
* Search notes by title
* Add tags to notes
* Search notes by tags
* Clear all notes

### Data Persistence

* Automatic data saving using pickle
* Contacts and notes are restored after restarting the application

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

## Run Application

```bash
python -m assistant.main
```

or

```bash
python3 -m assistant.main
```

## Available Commands

### Contacts

```text
add [name] [+countrycode_number]
change [name] [old_phone] [new_phone]
phone [name]
all
find [text]
delete [name]
```

### Birthdays

```text
add-birthday [name] [DD.MM.YYYY]
show-birthday [name]
birthdays [days]
```

### Additional Contact Information

```text
add-email [name] [email]
add-address [name] [address]
```

### Notes

```text
add-note [title] [content]
show-notes
find-note [title]
edit-note [title] [new_content]
delete-note [title]
clear-notes
```

### Tags

```text
add-tag [title] [tag]
find-tag [tag]
```

### Other

```text
hello
help
close
exit
```

## Example Usage

```text
add Maryna +380999076997
add-email Maryna maryna@gmail.com
add-address Maryna Valencia Spain
add-birthday Maryna 26.10.1984

add-note Python Learn decorators
add-tag Python programming

find-tag programming
birthdays 30
```

## Technologies

* Python 3
* Object-Oriented Programming (OOP)
* Pickle Serialization
* Git
* GitHub

## Author

Maryna Slavioglo
