import re
from collections import UserDict
from datetime import datetime, timedelta

# Базовий клас для всіх полів
class Field:

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


# Клас для зберігання імені контакту
class Name(Field):
    pass


# Клас для зберігання та валідації номера телефону
class Phone(Field):

    def __init__(self, value):

        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain 10 digits.")

        super().__init__(value)

# Клас для зберігання та валідації email
class Email(Field):

    def __init__(self, value):

        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(pattern, value):

            raise ValueError("Invalid email format.")

        super().__init__(value)

# Клас для зберігання адреси
class Address(Field):
    pass

# Клас для зберігання та валідації дня народження
class Birthday(Field):

    def __init__(self, value):

        try:

            birthday = datetime.strptime(value, "%d.%m.%Y")

            super().__init__(birthday)

        except ValueError:

            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):

        return self.value.strftime("%d.%m.%Y")


# Клас для зберігання інформації про контакт
class Record:

    def __init__(self, name):

        self.name = Name(name)

        self.phones = []

        self.email = None

        self.address = None

        self.birthday = None


    # Додавання номера телефону до контакту
    def add_phone(self, phone):

        self.phones.append(Phone(phone))

    # Видалення номера телефону
    def remove_phone(self, phone):

        for p in self.phones:

            if p.value == phone:

                self.phones.remove(p)

                return

    # Редагування існуючого номера телефону
    def edit_phone(self, old_phone, new_phone):

        for p in self.phones:

            if p.value == old_phone:

                p.value = Phone(new_phone).value

                return

        raise ValueError("Phone number not found.")

    # Пошук номера телефону
    def find_phone(self, phone):

        for p in self.phones:

            if p.value == phone:

                return p

        return None

    # Додавання дня народження
    def add_birthday(self, birthday):

        self.birthday = Birthday(birthday)
    
    # Додавання email
    def add_email(self, email):

        self.email = Email(email)

    # Додавання адреси
    def add_address(self, address):

        self.address = Address(address)

    # Текстове представлення контакту
    def __str__(self):

        phones = "; ".join(p.value for p in self.phones)

        birthday = f", birthday: {self.birthday}" if self.birthday else ""

        email = f", email: {self.email.value}" if self.email else ""

        address = f", address: {self.address.value}" if self.address else ""

        return (
            f"Contact name: {self.name.value}, "
            f"phones: {phones}"
            f"{birthday}"
            f"{email}"
            f"{address}"
        )



# Клас для зберігання та керування контактами
class AddressBook(UserDict):

    # Додавання нового запису до адресної книги
    def add_record(self, record):

        self.data[record.name.value] = record

    # Пошук контакту за ім’ям
    def find(self, name):

        return self.data.get(name)

    # Видалення контакту за ім’ям
    def delete(self, name):

        if name in self.data:

            del self.data[name]

    # Отримання списку найближчих днів народження
    def get_upcoming_birthdays(self):

        today = datetime.today().date()

        upcoming_birthdays = []

        for record in self.data.values():

            # Пропускаємо контакти без дня народження
            if record.birthday is None:

                continue

            birthday = record.birthday.value.date()

            # Замінюємо рік на поточний
            birthday_this_year = birthday.replace(year=today.year)

            # Якщо день народження вже минув цього року,
            # переносимо його на наступний рік
            if birthday_this_year < today:

                birthday_this_year = birthday_this_year.replace(
                    year=today.year + 1
                )

            # Обчислюємо різницю в днях
            delta_days = (birthday_this_year - today).days

            # Перевіряємо дні народження на наступні 7 днів
            if 0 <= delta_days <= 7:

                congratulation_date = birthday_this_year

                # Якщо день народження на вихідних,
                # переносимо привітання на понеділок
                if congratulation_date.weekday() >= 5:

                    days_to_monday = 7 - congratulation_date.weekday()

                    congratulation_date += timedelta(days=days_to_monday)

                upcoming_birthdays.append({
                    "name": record.name.value,
                    "birthday": congratulation_date.strftime("%d.%m.%Y")
                })

        return upcoming_birthdays