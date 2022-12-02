class Book:
    def _init_(self, title, author, publisher, price, royalty, copies):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.royalty = royalty
        self.copies = copies

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_publisher(self):
        return self.publisher
    def get_price(self):
        return self.price

    def set_title(self,x):
        self.title=x
    def set_author(self,x):
        self.author=x
    def set_publisher(self,x):
        self.publisher=x
    def set_price(self,x):
        self.price=x
    def set_copies(self,x):
        self.copies=x

    def royalty_method(self):
        if self.copies <= 500:
            self.royalty =0.1*self.price*self.copies
        if self.copies >500 and self.copies<=1500:
            self.royalty=0.1*self.price*500+0.125*self.price*(self.copies-500)
        if self.copies>1500:
            self.royalty=0.1*self.price*500+0.125*self.price*1000+0.15*self.price*(self.copies - 1500)

            return self.royalty

class Ebook (Book):
    def _init_(self,title,author,publisher,price,royalty, copies,format):
        super()._init_(self,title,author,publisher,price,royalty,copies)
        self.format = format

    def set_format(self,x):
        self.format=x
    def get_format(self):
        return self.format

    def royalty_method(self):
        if self.copies <= 500:
            self.royalty =0.1*self.price*self.copies
        if self.copies >500 and self.copies<=1500:
            self.royalty=0.1*self.price*500+0.125*self.price*(self.copies-500)
        if self.copies>1500:
            self.royalty=0.1*self.price*500+0.125*self.price*1000+0.15*self.price*(self.copies - 1500)

            return 0.88*self.royalty

B1= Ebook()
B1.set_title("Mahanayak")
B1.set_author('Vishwash_Patil')
B1.set_publisher('Rajahans')
B1.set_price(500)
B1.set_format("PDF")
print("Title of the book is:",B1.get_title())
print("Author of the book is:",B1.get_author())
print("Publisher of the book is:",B1.get_publisher())
print("Price of the book is:",B1.get_price())

B1.set_copies(2000)
B1.royalty_method()

print("Royalty of a book is",B1.royalty_method())





            
