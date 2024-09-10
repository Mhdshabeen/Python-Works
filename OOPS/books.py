  # __init__() practice

class book():
    def __init__(self,title,author,price,language):

        self.title=title
        self.author=author
        self.price=price
        self.language=language

    def display_book(self):

        print(self.title,self.author,self.price,self.language)

book_instance=book("Adu jeevitham","Basheer",123,"malayalam")

book_instance.display_book()