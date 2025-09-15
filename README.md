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




