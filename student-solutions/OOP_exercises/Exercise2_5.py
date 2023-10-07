import math
# Exercise 1
pi = math.pi
class Shape:
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return self.radius**2*pi
    def calculate_perimeter(self):
        return self.radius*2*pi
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def calculate_area(self):
        return self.width * self.height
    def calculate_perimeter(self):
        return (self.width + self.height)*2
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

# Exercise 5
class Book:
    def __init__(self,title,author,year,pages,isbn_code):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.isbn_code = isbn_code

class Library:

    def __init__(self,books_df):
        self.books_df = books_df
    def add_new_book(self,book):
        new_row = {'title': book.title, 'author': book.author, 'year': book.year, 'pages': book.pages, 'isbn_code': book.isbn_code}
        self.books_df = self.books_df.append(new_row,ignore_index=True)
        return self.books_df
    
    def delete_book(self,isbn_code):
        self.books_df = self.books_df.drop(self.books_df[self.books_df['isbn_code'] == isbn_code].index)
        return self.books_df
    
    def show_all_books(self):
        return self.books_df.values
    
    def find_book_by_author(self,author):
        return self.books_df.loc[self.books_df['author'] == author].values
    
    def find_book_by_year(self,year):
        return self.books_df.loc[self.books_df['year'] == year]

if __name__ == '__main__':
    exercise = int(input("Choose the exercise: "))
    if exercise == 1:
        cicrle = Circle(radius=3)
        print(cicrle.calculate_area())

        rectangle = Rectangle(width=3,height=5)
        print(rectangle.calculate_area())

        square = Square(side=2)
        print(square.calculate_area())
    elif exercise == 5:
        import pandas as pd
        df = pd.DataFrame({'title': ['The Catcher in the Rye', 'To Kill a Mockingbird'], 'author': ['J.D. Salinger', 'Harper Lee'], 'year': [1951, 1960], 'pages': [224, 336], 'isbn_code': ['978-3-16-148410-0', '978-3-16-148411-0']})
        library = Library(df)
        new_book = Book('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 180, '978-3-16-148412-0')
        print("1. show_all_books: ", library.show_all_books())
        print("2. find_book_by_author: ", library.find_book_by_author("Harper Lee"))
        print("3. add_new_book: ", library.add_new_book(new_book))
        print("4. delete_book: ", library.delete_book('978-3-16-148411-0'))