# Клас для зберігання однієї нотатки
class Note:

    def __init__(self, title, content):

        self.title = title

        self.content = content

        self.tags = []

    def __str__(self):

        tags = ", ".join(self.tags)

        if not tags:
           tags = "No tags"

        return (
            f"Title: {self.title}\n"
            f"Content: {self.content}\n"
            f"Tags: {tags}"
        )

    # Додати тег до нотатки
    def add_tag(self, tag):

        # Не дозволяємо дублікати тегів
        if tag.lower() not in [
            existing_tag.lower()
            for existing_tag in self.tags
        ]:

            self.tags.append(tag)


# Клас для зберігання колекції нотаток
class NotesBook:

    def __init__(self):

        # Список нотаток
        self.notes = []

    # Додати нову нотатку
    def add_note(self, note):

        if self.find_note(note.title):

            raise ValueError(
                "Note with this title already exists."
            )

        self.notes.append(note)

    # Знайти нотатку за заголовком
    def find_note(self, title):

        for note in self.notes:

            if note.title.lower() == title.lower():

                return note

        return None

    # Редагування тексту нотатки
    def edit_note(self, title, new_content):

        note = self.find_note(title)

        if note is None:

            return False

        note.content = new_content

        return True

    # Видалити нотатку
    def delete_note(self, title):

        note = self.find_note(title)

        if note:

            self.notes.remove(note)

            return True

        return False

    # Додати тег до нотатки
    def add_tag(self, title, tag):

        note = self.find_note(title)

        if note is None:

            return False

        note.add_tag(tag)

        return True
    
    # Знайти всі нотатки за тегом
    def find_by_tag(self, tag):

        found_notes = []

        for note in self.notes:

            for note_tag in note.tags:

                if tag.lower() == note_tag.lower():

                    found_notes.append(note)

            break

        return found_notes