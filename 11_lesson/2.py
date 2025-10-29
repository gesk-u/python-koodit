class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, page):
        super().__init__(name)
        self.author = author
        self.page = page
    def print_info(self):
        print(f"Name: {self.name}; Author: {self.author}; Number of pages: {self.page}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor
    def print_info(self):
        print(f"Name: {self.name}; Chief editor: {self.editor};")

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
book2 = Book("1984", "George Orwell", 328)

mag1 = Magazine("National Geographic", "Susan Goldberg")
mag2 = Magazine("Time", "Edward Felsenthal")
mag3 = Magazine("Forbes", "Steve Forbes")


publications = []

publications.append(book1)
publications.append(book2)
publications.append(mag1)
publications.append(mag2)
publications.append(mag3)

for p in publications:
    p.print_info()


