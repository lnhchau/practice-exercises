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
        return self.books_df.append(new_row,ignore_index=True)
    
    def delete_book(self,isbn_code):
        return self.books_df.drop(self.books_df[self.books_df['isbn_code'] == isbn_code].index)
    
    def show_all_books(self):
        return self.books_df.values
    
    def find_book_by_author(self,author):
        return self.books_df.loc[self.books_df['author'] == author].values
    
    def find_book_by_year(self,year):
        return self.books_df.loc[self.books_df['year'] == year].values

if __name__ == '__main__':
    exercise = int(input("Choose the exercise: "))
    if exercise == 1:
        cicrle = Circle(radius=3)
        print(cicrle.calculate_area())

        rectangle = Rectangle(width=3,height=5)
        print(rectangle)

        square = Square(side=2)
        print(square.calculate_area())
    elif exercise == 5:
        import pandas as pd
        df = pd.DataFrame({'title': ['The Catcher in the Rye', 'To Kill a Mockingbird', 'The Great Gatsby'], 'author': ['J.D. Salinger', 'Harper Lee', 'F. Scott Fitzgerald'], 'year': [1951, 1960, 1925], 'pages': [224, 336, 180], 'isbn_code': ['978-3-16-148410-0', '978-3-16-148411-0', '978-3-16-148412-0']})
        library = Library(df)
        print(library.show_all_books())
        print(library.find_book_by_author("Harper Lee"))