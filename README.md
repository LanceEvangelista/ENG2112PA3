# ENG2112PA3

## Problem 1 

For problem one we are tasked with reading a csv file and presenting the specified data within the file such as the first 5 cars and last 5 cars, 
and cars that meet specific descriptions or specifications.

For this problem we will be using pandas a library within python that allows us to manipulate and present data.

```python

import pandas as pd
```

First we are tasked to show the first 5 cars in the csv file, to do such we can use the

`head()` command which always shows the first 5 data entries in the data set.

To show the last 5 cars we use

`tail()` which always shows the last 5 entries in a data set.

## Problem 2

For this problem the first task is to display the odd number indexed cars for this we can use

`cars[cars.index%2 == 1]` 

this tells the program to search within the cars csv file and the conditions in the `[]` tell it which indexes to consider.
for this first problem we want to get the odd numbered indexes, so we use boolean indexing by using modulo to get the cars in the odd numbered indexes
for this we used `car.index%2 == 1` as all numbers when divided by two with a remainder of one is a odd number.

`odd = cars[cars.index%2 == 1].head(5)`

Finally we can add `.head()` to the end to make the code know to only print the first 5 odd entries.

Next, to print the rows with only the model "Mazda RX4" we can use `.loc`. This command tells python to search in a specific row or column, we can use this to tell the program
to search for "Mazda RX4" in only the "Model" column within the cars ccsv file.

`cars.loc[cars['Model']=='Mazda RX4'])`

This command tells the program if it finds the model name "Mazda RX4" to be true, it will add it to the list of printed cars in the data table when printed.

If we want to display the amount of cylinders of a certain modal of car say "Camaro Z28" we can first search for the car using the same type of syntax `.loc`
further condtions just have to be added in order to only show the amount of cylinders.


`cars.loc[(cars['Model']=='Camaro Z28'), ['cyl']]`

Here python first searches for the car with the entry "Camaro Z28" under model
then using ['cyl'] we tell python to only display the cylinder column of that given entry.

Lastly if we want to determine the cylinder and gear type of multiple cars we can use `.loc` along with `.isin` syntax to index only the specified cars we want.

`cars.loc[cars['Model'].isin(['Mazda RX4 Wag','Ford Pantera L', 'Honda Civic']), ['Model', 'cyl','gear']]`

The portion: 
` .isin(['Mazda RX4 Wag','Ford Pantera L', 'Honda Civic']) ` 

tells the program to search for entries with these names in the 'Model' category. 
After indexing we can set the columns the program will print by using:

`['Model', 'cyl','gear']`

