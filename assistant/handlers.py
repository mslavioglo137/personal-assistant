from assistant.address_book import (
    AddressBook,
    Record,
    Phone
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
def birthdays(book: AddressBook):

    upcoming_birthdays = book.get_upcoming_birthdays()

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
