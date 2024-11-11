class BookLover():
    '''This class collects and stores the names of books read by individuals as well as+
    the ratings (on a scale of 1 to 5) these individuals give to these books.+
    The class will also check book titles to minimize, preferably avoid, duplicate entries.'''
    
    import pandas as pd
    
    #default parameters
    num_books = 0 
    book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
    
    def __init__(self, name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        '''
        Initialize required variables 
        '''
        self.name = name # string: name of the person entering book data
        self.email = email # string: name of the person entering book data
        self.fav_genre = fav_genre # string: person’s favorite book genre
        self.num_books = num_books
        self.book_list = book_list
        
    def add_book(book_name, book_rating):
        '''
        Add the name(s) of the book(s) read along with a 1 to 5 rating
        '''
        new_book = pd.DataFrame({
            'book_name': [book_name], 
            'book_rating': [book_rating]
        })

        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        
    def has_read(book_name):
        '''
        Takes book_name (string) as input and determines if the person has read the book
        '''
        is_on_list = [i for i in book_list if book_name(i) == book_name]
        
    def num_books_read():
        '''
        Print the number of books in the list
        '''
        print(len(book_list))
    
    def fav_books():
        '''
        List of books with a rating of 3, 4, or 5
        '''
        get_fav_books = [i for i in book_list if book_rating(i) >= 3]
        print(get_fav_books)