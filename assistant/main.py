import shlex
from assistant.address_book import AddressBook
from assistant.notes import NotesBook

from assistant.storage import (
    save_data,
    load_data
)

from assistant.handlers import (
    parse_input,
    add_contact,
    change_contact,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    add_email,
    add_address,
    find_contact,
    delete_contact,
    add_note,
    show_notes,
    find_note,
    delete_note,
    edit_note,
    add_tag,
    find_tag,
    clear_notes,
    add_full_contact
)


def show_menu():

    print("""
==================================================
               PERSONAL ASSISTANT
==================================================

📇 CONTACTS

  add-full "name" phone email "address" birthday
  add "name" phone
  change "name" old_phone new_phone
  phone "name"
  all
  find text
  delete "name"

🎂 BIRTHDAYS

  add-birthday "name" DD.MM.YYYY
  show-birthday "name"
  birthdays days

📧 EXTRA INFO

  add-email "name" email
  add-address "name" "address"

📝 NOTES

  add-note "title" content
  show-notes
  find-note "title"
  edit-note "title" new_content
  delete-note "title"
  clear-notes

🏷️ TAGS

  add-tag "title" tag
  find-tag tag

⚙️ OTHER

  hello
  help
  close
  exit

==================================================

""")


def main():

    book = load_data(
        "addressbook.pkl",
        AddressBook
    )

    notes_book = load_data(
        "notesbook.pkl",
        NotesBook
    )

    print("\nWelcome to Personal Assistant!")
    print("Type 'help' to display the command menu.\n")

    show_menu()

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

        elif command == "help":

            show_menu()
        elif command == "add-full":

            print(add_full_contact(args, book))

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

            print(birthdays(args, book))

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

        elif command == "edit-note":

            print(edit_note(args, notes_book))

        elif command == "add-tag":

            print(add_tag(args, notes_book))

        elif command == "find-tag":

            print(find_tag(args, notes_book))

        elif command == "clear-notes":

            print(clear_notes(notes_book))

        else:

            print("Invalid command.")
            print("Type 'help' to see available commands.")


if __name__ == "__main__":

    main()