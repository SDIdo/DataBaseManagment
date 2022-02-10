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

    # greater than by name
    def __gt__(self, other) -> bool:
        if self.name > other.name:
            return True
        return False

    # less than or equal by name
    def __le__(self, other) -> bool:
        if self.name <= other.name:
            return True
        return False

    # equals to by name
    def __eq__(self, other) -> bool:
        if self.name == other.name:
            return True
        return False


    @staticmethod
    def mergeSort(myList):        
        if len(myList) > 1:
            mid = len(myList)//2
            left = myList[:mid]
            right = myList[mid:]

            # recursion call on each half

            Item.mergeSort(left)
            Item.mergeSort(right)
        

            # Two iterations for traversing the two halves
            i = 0
            j = 0

            # iterator for the main list
            k = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    # the value from the left half has been used
                    myList[k] = left[i]
                    # Move the iterator forward
                    i+=1
                else:
                    myList[k] = right[j]
                    j += 1
                # move to the next slot
                k += 1

            # For all the remaining values
            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1
            
            while j < len(right):
                myList[k] = right[j]
                j += 1
                k += 1


    # @classmethod
    # def find_max(cls):
    #     res = []
    #     max = cls.all[0] # arbitrary
    #     for item in cls.all[1:]:
    #         if item > max:
    #             max = item
            

    @staticmethod
    def read_csv(file):
        file = open(file)
        # make sure it's a csv file.. 
        csvreader = csv.reader(file)
        next(csvreader) # throw the header
        for row in csvreader:
            Item.all.append(Item(row[0], float(row[1]), int(row[2])))
        file.close()
