#---------- User Class ----------
class User:
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books={}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email=address
        print("{}'s email has been udpated".format(self.name))

    def __repr__(self):
        return("User: {name} -> Email: {email}; Books Read: {books}".format(name=self.name,email=self.email,books=len(self.books)))

    def __eq__(self, other_user):
        if self.name==other_user.name and self.email==other_user.email:
            return True
        else:
            return False
        
    def read_book(self, book, rating=None):
        if rating:
            if type(rating)==int:
                if rating>=0 and rating<=4:
                    self.books[book] = rating
                else:
                    print("Invalid Rating (Out of Range)")
            else:
                print("Invalid Rating (Non-Integer)") 
        
    def get_average_rating(self):
        count=0
        total=0
        for book in self.books:
            count+=1
            total+=self.books[book]
        return total/count
         
        
#---------- Parent Book Class ----------
class Book:
    def __init__(self, title, isbn):
        self.title=title
        self.isbn=isbn
        self.ratings=[]

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn

    def set_isbn(self, new_isbn):
        if type(new_isbn)==int:
            self.isbn=new_isbn
            print("The ISBN for \"{}\" has been udpated".format(self.title))
        else:
            print("Not a valid ISBN.")

    def add_rating(self, rating):
        if type(rating)==int:
            if rating>=0 and rating<=4:
                self.ratings.append(rating)
            else:
                print("Invalid Rating (Out of Range)")
        else:
            print("Invalid Rating (Non-Integer)")   
            
    def __eq__(self, other_book):
        if self.title==other_book.title and self.isbn==other_book.isbn:
            return True
        else:
            return False
        
    def __repr__(self):
        return self.title
    
    def get_average_rating(self):
        count=0
        total=0
        for item in self.ratings:
            count+=1
            total+=item
        return total/count
    
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    
#---------- Fiction Class (Book Child) ----------
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author=author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)
    
    
#---------- Non_Fiction Class (Book Child) ----------
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject=subject
        self.level=level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)
    
    
#---------- TomeRater Class ----------
class TomeRater:
    def __init__(self):
        self.users={}
        self.books={}

    def create_book(self, title, isbn):
        return Book(title, isbn)
        
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)
        
    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)        
        
    def add_book_to_user(self, book, email, rating=None):
        try:
            self.users[email].read_book(book, rating)
            if rating:
                book.add_rating(rating)
            try:
                self.books[book]+=1
            except KeyError:
                self.books[book]=1
        except KeyError:
            print("No user with email {}!".format(email))
    
    def add_user(self, name, email, books=None):
        if "@" in email and (".com" in email or ".edu" in email or ".org" in email):           
            if email not in self.users:
                self.users[email]=User(name, email)
            else:
                return "There is already a user with this email address."
            if books:
                for book in books:
                    self.add_book_to_user(book, email)
        else:
            return "Please enter a valid email address."
        
    def __repr__(self):
        return "This library contains {numbooks} books and has {numusers} users.".format(numbooks=len(self.books), numusers=len(self.users))
    
    def print_catalog(self):
        for item in self.books.keys():
            if self.books[item] > 1:
                timevar="times"
            else:
                timevar="time"
            print(str(item) + " (Read " + str(self.books[item]) + " " + timevar + ")")
    
    def print_users(self):
        for person in self.users:
            print(self.users[person])
    
    def most_read_book(self):
        max_value=0
        for key, value in self.books.items():
            if value > max_value:
                max_value=value
                max_key=key
        if self.books[max_key] > 1:
            timevar="times"
        else:
            timevar="time"
        return (str(max_key) + " (Read " + str(self.books[max_key]) + " " + timevar + ")")
       
    def highest_rated_book(self):
        max_average=0
        for key in self.books.keys():
            tempavg=key.get_average_rating()
            if tempavg > max_average:
                max_average=tempavg
                max_key=key
        return (str(max_key) + " (Average Rating: " + str(max_average) + ")")
        
    def most_positive_user(self):
        max_average=0
        for user in self.users:
            tempavg=self.users[user].get_average_rating()
            if tempavg > max_average:
                max_average=tempavg
                max_user=self.users[user]
        return (str(max_user.name) + " (Average Rating: " + str(max_average) + ")")
        
        
        
        
        