class Book:
    def __init__(self, title, author):
         self.name:str
         self.author:str
         self.avaiable_num:int
   

class Library:
    def __init__(self):
        
        self.books =[]
        
        
    def addBook(self, book: Book):
        self.books.append(book)
        
    def showBooks():
        #show list of book./
        
        return self.books
    def find_books(self, name: str) -> list[Book]:
        """
        find specific book
        """
        matches = []
        for book in self.books:
            if book.title.lower() == name.lower():
                matches.append(book)
        return matches
    
    