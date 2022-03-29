import pandas
house = pandas.read_csv('boston.csv')
print(house)
print(house.head(1))
print(house.describe())