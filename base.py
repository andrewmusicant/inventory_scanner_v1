import datetime
import psycopg2


class Comic:
    # def __init__(self, **kwargs):
    #     self.name = kwargs['name']
    #     self.qty = kwargs['qty']
    #     self.price = kwargs['price']
    #     self.publisher = kwargs['publisher']
    #     self.author = kwargs['author']
    #     self.illustrator = kwargs['illustrator']
    #     self.date_recieved = datetime.date
    #     self.last_date_sold = datetime.date
    def __init__(self, name, qty, price, publisher, author, illustrator):
        self.name = name
        self.qty = qty
        self.price = price
        self.publisher = publisher
        self.author = author
        self.illustrator = illustrator
        self.date_recieved = datetime.date
        self.last_date_sold = datetime.date

    def save(self):
        con = psycopg2.connect(database='inventory_system', user='Envy')
        cur = con.cursor()

        cur.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
        id SERIAL PRIMARY KEY,
        name varchar, qty numeric, price decimal,
        publisher varchar, author varchar,
        illustrator varchar, date_recieved varchar,
        last_date_sold varchar)''')

        data = (self.name, self.qty, self.price, self.publisher, self.author, self.illustrator, self.date_recieved, self.last_date_sold)
        cur.execute('INSERT INTO inventory (name, qty, price, publisher, author, illustrator, date_recieved, last_date_sold) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)', data)
        cur.execute('SELECT id FROM inventory where name = %s AND qty = %s AND price = %s AND publisher = %s AND author = %s AND illustrator = %s AND date_recieved = %s AND last_date_sold = %s', data)

        con.commit()
        cur.close()
        con.close()

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(
                        self.name, self.publisher,
                        self.qty, self.price,
                        self.author, self.illustrator)


def main():
    print("\nWelcome to your collection manager.\n")
    name = input("Please enter the name of the comic you wish to enter to your collection: ")
    qty = int(input("Please enter the quantity of the comic: "))
    price = float(input("Please enter the price of the comic: "))
    publisher = input("Please enter the publisher of the comic: ")
    author = input("Please enter the author of the comic: ")
    illustrator = input("Please enter the illustrator of the comic: ")
    comic = Comic(name, qty, price, publisher, author, illustrator)
    comic.save()

if __name__ == '__main__':
    main()
