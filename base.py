import os
import sys
import datetime


class Comic:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.qty = kwargs['qty']
        self.price = kwargs['price']
        self.publisher = kwargs['publisher']
        self.author = kwargs['author']
        self.illustrator = kwargs['illustrator']
        self.last_date_sold = datetime.date

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(
                        self.name, self.publisher,
                        self.qty, self.price,
                        self.author, self.illustrator)


print("Welcome to your collection manager.\n")
while True:
    name = input("Please enter the name of the comic you wish to enter to your collection: ")
    qty = int(input("Please enter the quantity of the comic: "))
    price = int(input("Please enter the price of the comic: "))
    publisher = input("Please enter the publisher of the comic: ")
    author = input("Please enter the author of the comic: ")
    illustrator = input("Please enter the illustrator of the comic: ")
    comic = Comic(name, qty, price, publisher, author, illustrator)
