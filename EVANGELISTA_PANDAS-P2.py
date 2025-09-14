import pandas as pd

cars = pd.read_csv("cars.csv")

odd = cars[cars.index%2 == 1].head(5)
print(odd)

print(cars.loc[cars['Model']=='Mazda RX4'])
print(cars.loc[(cars['Model']=='Camaro Z28'), ['Model','cyl']])
print(cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L', 'Honda Civic']), ['Model', 'cyl','gear']])
