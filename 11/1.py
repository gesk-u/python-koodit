class Publication:
    def __init__(self, name):
        self.name = name
    def print_info(self):
        return f"Name: {self.name}"
class Book(Publication):
    def __init__(self, name, author, page):
        super().__init__(name)
        self.author = author
        self.page = page
    def print_info(self):
        base_info = super().print_info()
        print(f"{base_info}; Author: {self.author}; Number of pages: {self.page}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
    def print_info(self):
        base_info = super().print_info()
        print(f"{base_info}; Chief editor: {self.editor};")

book1 = Book("Compartment No. 6 ", "Rosa Liksom", 192)

mag1 = Magazine("Donald Duck", "Aki Hyyppä")

publications = [book1, mag1]


for p in publications:
    p.print_info()
