# Personal Assistant

Command-line personal assistant for managing contacts and notes.

## Features

### Contact Management

* Add new contacts
* Store multiple phone numbers for one contact
* Add and manage birthdays
* Add email addresses
* Add physical addresses
* Edit phone numbers
* Delete contacts
* Search contacts by:

  * name
  * phone number
  * email
  * address
* View upcoming birthdays

### Data Validation

* International phone number support
* Phone numbers must contain from 10 to 15 digits
* Email format validation
* Birthday validation (`DD.MM.YYYY`)

### Data Storage

* Automatic saving of contacts using `pickle`
* Automatic loading of saved data when the application starts
* Data persists between sessions

## Project Structure

```text
personal-assistant/
│
├── assistant/
│   ├── __init__.py
│   ├── address_book.py
│   ├── decorators.py
│   ├── handlers.py
│   ├── main.py
│   ├── notes.py
│   └── storage.py
│
├── README.md
├── requirements.txt
├── setup.py
└── .gitignore
```

## Available Commands

### General

```text
hello
close
exit
```

### Contacts

```text
add [name] [phone]

change [name] [old_phone] [new_phone]

phone [name]

all

find-contact [search_text]

delete-contact [name]
```

### Birthday Management

```text
add-birthday [name] [DD.MM.YYYY]

show-birthday [name]

birthdays
```

### Email Management

```text
add-email [name] [email]
```

### Address Management

```text
add-address [name] [address]
```

## Installation

Clone repository:

```bash
git clone https://github.com/mslavioglo137/personal-assistant.git
```

Go to project directory:

```bash
cd personal-assistant
```

Create virtual environment:

```bash
python3 -m venv .venv
```

Activate virtual environment:

macOS / Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

## Run Application

```bash
python -m assistant.main
```

## Example Usage

```text
add Maryna +380999076997

add-email Maryna maryna@gmail.com

add-address Maryna Valencia Spain

add-birthday Maryna 26.10.1984

find-contact Valencia

all
```

## Current Development Status

Completed:

* Project architecture
* Address Book
* Phone validation
* International phone support
* Email validation
* Birthday management
* Contact search
* Persistent data storage

Planned:

* Notes management
* Tags support
* Search notes by tags
* Package installation support

```
```
