import csv


class Item:
    all = []
    def __init__(self, name: str, price: float, quantity: int):
        # Assert
        assert price >= 0, f"Price field must be greater or equal to zero"
        assert quantity >= 0, f"Quantity field must be greater or equal to zero"
        self.__name = name
        self.__quantity = quantity
        self.__price = price
    
    @property
    def name(self):
        return self.__name

    @name.setter
    def set_name(self, value: str):
        self.__name = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def set_quantity(self, value: str):
        self.__quantity = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def set_price(self, value: str):
        self.__price = value

    def __repr__(self):
        return f"'{self.__class__.__name__}'({self.__name},{self.__price},{self.__quantity})"

    @staticmethod
    def read_csv(file):
        file = open(file)
        # make sure it's a csv file.. 
        csvreader = csv.reader(file)
        next(csvreader) # throw the header
        for row in csvreader:
            Item.all.append(Item(row[0], float(row[1]), int(row[2])))
        file.close()
