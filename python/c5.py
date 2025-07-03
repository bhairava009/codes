class Book:
    def __init__(self,title,author,price):

        self.title=title
        self.author=author
        self.price=price

books=[Book("human","u.singh",877),Book("science","s.singh",988),Book("physics","y.schadra",333),Book("maths","vsinghna",499)
]
print("Title of all the books above price of 500")
for book in books:
    if book.price  > 500:
        print(book.title)


