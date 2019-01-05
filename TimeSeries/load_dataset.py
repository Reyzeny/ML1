from pandas import Series
from pandas import read_csv

#series = read_csv('../Datasets/daily-total-female-births-in-cal.csv', header=0)
series = Series.from_csv('../Datasets/daily-total-female-births-in-cal.csv', header=0)
print(series.head())