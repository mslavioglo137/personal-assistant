from assistant.address_book import AddressBook

from assistant.notes import NotesBook

from assistant.storage import (
    save_data,
    load_data
)

from assistant.handlers import (
    add_note,
    delete_note,
    find_note,
    parse_input,
    add_contact,
    change_contact,
    show_notes,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    add_email,
    add_address,
    find_contact,
    delete_contact
)


def main():

    book = load_data(
        "addressbook.pkl",
        AddressBook
    )

    notes_book = load_data(
        "notesbook.pkl",
        NotesBook
    )

    print("Welcome to Personal Assistant!")

    print("""
Available commands:
hello

add [name] [+countrycode_number]
change [name] [old_phone] [new_phone]
phone [name]
all

add-birthday [name] [DD.MM.YYYY]
show-birthday [name]
birthdays

add-email [name] [email]
add-address [name] [address]

find [text]
delete [name]

add-note [title] [content]
show-notes
find-note [title]
delete-note [title]

close or exit
""")

    while True:

        user_input = input("Enter a command: ")

        if not user_input:

            continue

        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:

            save_data(
                book,
                "addressbook.pkl"
            )

            save_data(
                notes_book,
                "notesbook.pkl"
            )

            print("Good bye!")

            break

        elif command == "hello":

            print("How can I help you?")

        elif command == "add":

            print(add_contact(args, book))

        elif command == "change":

            print(change_contact(args, book))

        elif command == "phone":

            print(show_phone(args, book))

        elif command == "all":

            print(show_all(book))

        elif command == "add-birthday":

            print(add_birthday(args, book))

        elif command == "show-birthday":

            print(show_birthday(args, book))

        elif command == "birthdays":

            print(birthdays(book))

        elif command == "add-email":

            print(add_email(args, book))

        elif command == "add-address":

            print(add_address(args, book))

        elif command == "find":

            print(find_contact(args, book))

        elif command == "delete":

            print(delete_contact(args, book))

        elif command == "add-note":

            print(add_note(args, notes_book))

        elif command == "show-notes":

            print(show_notes(notes_book))

        elif command == "find-note":

            print(find_note(args, notes_book))

        elif command == "delete-note":

            print(delete_note(args, notes_book))

        else:

            print("Invalid command.")


if __name__ == "__main__":

    main()