# Defining a base class called Person with attributes name and age.
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Defining a class Member that inherits from Person and has an additional attribute member_id.    
class Member(Person):
    def __init__(self,name, age, member_id):
        # initializing the name and age from the Person's class
        super().__init__(name, age)   
        # Adding anew attribute specific to member
        self.member_id = member_id

# Defining a class Librarian that inherits from Person and has an additional attribute employee_id
class Librarian(Person):
      def __init__(self,name, age, employee_id):
        # initializing the name and age from the Person's class
        super().__init__(name, age)   
        # Adding anew attribute specific to member
        self.employee_id = employee_id


# Defining a class Book with attributes title, author, and isbn   
class Book():
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

# Defining a class Library with an attribute books (a list of Book objects) and members (a list of Member objects)
class Library():
    def __init__(self, books = None, members = None):  
        if books is not None:
            self.books = list(books)
        else:
            self.books = []

        if members is not None:
            self.members = list(members)    
        else:
            self.members = []

    # Implementing methods in Library to add books and members.
    def add_books(self,book):
        if book not in self.books:
            self.books.append(book)

    def add_members(self,member):
        if member not in self.members:
            self.members.append(member)

    # Implementing a method in Library to simulate lending a book to a member
    def borrow_books(self, book):
        if book in self.books:
            self.books.remove(book)

    # Implement a method in Library to simulate returning a book
    def return_books(self,book):
        self.books.append(book)
