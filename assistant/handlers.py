from assistant.address_book import (
    AddressBook,
    Record,
    Phone
)

from assistant.notes import (
    Note,
    NotesBook
)

from assistant.decorators import input_error

# Розбір введеної користувачем команди
def parse_input(user_input):

    cmd, *args = user_input.split()

    cmd = cmd.strip().lower()

    return cmd, *args


# Додавання нового контакту або нового номера
@input_error
def add_contact(args, book: AddressBook):

    name, phone, *_ = args

    record = book.find(name)

    if record is None:

        # Валідація номера до створення контакту
        Phone(phone)

        record = Record(name)

        record.add_phone(phone)

        book.add_record(record)

        return "Contact added."

    record.add_phone(phone)

    return "Contact updated."


# Зміна номера телефону
@input_error
def change_contact(args, book: AddressBook):

    name, old_phone, new_phone = args

    record = book.find(name)

    if record is None:
        raise KeyError

    record.edit_phone(old_phone, new_phone)

    return "Contact updated."


# Показати телефони контакту
@input_error
def show_phone(args, book: AddressBook):

    name = args[0]

    record = book.find(name)

    if record is None:
        raise KeyError

    return "; ".join(phone.value for phone in record.phones)

# Пошук контакту за будь-яким полем
@input_error
def find_contact(args, book: AddressBook):

    search_text = args[0].lower()

    found_contacts = []

    for record in book.data.values():

        found = False

        # Пошук по імені
        if search_text in record.name.value.lower():
            found = True

        # Пошук по телефонах
        for phone in record.phones:

            if search_text in phone.value:
                found = True

        # Пошук по email
        if (
            hasattr(record, "email")
            and record.email
            and search_text in record.email.value.lower()
        ):
            found = True

        # Пошук по адресі
        if (
            hasattr(record, "address")
            and record.address
            and search_text in record.address.value.lower()
        ):
            found = True

        if found:
            found_contacts.append(str(record))

    if not found_contacts:
        return "Contact not found."

    return "\n".join(found_contacts)

# Показати всі контакти
@input_error
def show_all(book: AddressBook):

    if not book.data:
        return "No contacts saved."

    return "\n".join(str(record) for record in book.data.values())

# Видалення контакту
@input_error
def delete_contact(args, book: AddressBook):

    name = args[0]

    record = book.find(name)

    if record is None:
        raise KeyError

    book.delete(name)

    return "Contact deleted."


# Додавання дня народження
@input_error
def add_birthday(args, book: AddressBook):

    name, birthday = args

    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_birthday(birthday)

    return "Birthday added."


# Показати день народження контакту
@input_error
def show_birthday(args, book: AddressBook):

    name = args[0]

    record = book.find(name)

    if record is None:
        raise KeyError

    if record.birthday is None:
        return "Birthday not found."

    return str(record.birthday)


# Показати найближчі дні народження
@input_error
def birthdays(args, book: AddressBook):

    try:
        days = int(args[0])

    except ValueError:

        return "Enter number of days."

    upcoming_birthdays = book.get_upcoming_birthdays(days)

    if not upcoming_birthdays:
        return "No upcoming birthdays."

    result = []

    for user in upcoming_birthdays:

        result.append(
            f"{user['name']}: {user['birthday']}"
        )

    return "\n".join(result)

# Додавання email
@input_error
def add_email(args, book: AddressBook):

    name, email = args

    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_email(email)

    return "Email added."
# Додавання адреси
@input_error
def add_address(args, book: AddressBook):

    name, *address = args

    record = book.find(name)

    if record is None:
        raise KeyError

    record.add_address(" ".join(address))

    return "Address added."

# Додавання нової нотатки
@input_error
def add_note(args, notes_book: NotesBook):

    title = args[0]

    content = " ".join(args[1:])

    note = Note(title, content)

    notes_book.add_note(note)

    return "Note added."


# Показати всі нотатки
@input_error
def show_notes(notes_book: NotesBook):

    if not notes_book.notes:

        return "No notes saved."

    return "\n\n".join(
        str(note)
        for note in notes_book.notes
    )


# Пошук нотатки за заголовком
@input_error
def find_note(args, notes_book: NotesBook):

    title = args[0]

    note = notes_book.find_note(title)

    if note is None:

        return "Note not found."

    return str(note)


# Видалення нотатки за заголовком
@input_error
def delete_note(args, notes_book: NotesBook):

    title = args[0]

    deleted = notes_book.delete_note(title)

    if not deleted:

        return "Note not found."

    return "Note deleted."

# Редагування нотатки
@input_error
def edit_note(args, notes_book: NotesBook):

    # Перший аргумент — заголовок нотатки
    title = args[0]

    # Усе інше — новий текст
    new_content = " ".join(args[1:])

    updated = notes_book.edit_note(
        title,
        new_content
    )

    if not updated:

        return "Note not found."

    return "Note updated."

# Додавання тегу до нотатки
@input_error
def add_tag(args, notes_book: NotesBook):

    title = args[0]

    tag = args[1]

    updated = notes_book.add_tag(
        title,
        tag
    )

    if not updated:

        return "Note not found."

    return "Tag added."

# Пошук нотаток за тегом
@input_error
def find_tag(args, notes_book: NotesBook):

    tag = args[0]

    found_notes = [
        note for note in notes_book.notes
        if any(
            tag.lower() == note_tag.lower()
            for note_tag in note.tags
        )
    ]

    if not found_notes:

        return "No notes found with this tag."

    return "\n\n".join(
        str(note)
        for note in found_notes
    )

# Видалити всі нотатки
@input_error
def clear_notes(notes_book: NotesBook):

    notes_book.notes.clear()

    return "All notes deleted."