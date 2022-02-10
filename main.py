from Item import Item

Item.read_csv('data.csv')
print(Item.all)

Item.mergeSort(Item.all)
print(Item.all)

