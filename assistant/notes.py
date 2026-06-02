# Клас для зберігання однієї нотатки
class Note:

    def __init__(self, title, content):

        self.title = title

        self.content = content

        self.tags = []

    def __str__(self):

        tags = ", ".join(self.tags)

        return (
            f"Title: {self.title}\n"
            f"Content: {self.content}\n"
            f"Tags: {tags}"
        )


# Клас для зберігання колекції нотаток
class NotesBook:
    def __init__(self):
        # список нотаток
        self.notes = []

    # Додати нову нотатку
    def add_note(self, note):
        if self.find_note(note.title):
            raise ValueError("Note with this title already exists.")
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