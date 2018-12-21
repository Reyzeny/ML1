def dataset_minmax(dataset):
    minmax = list()
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        value_min = min(col_values)
        value_max = max(col_values)
        minmax.append([value_min, value_max])
    return minmax

def normalize(dataset, minmax):
    for row in dataset:
        for i in range(len(row)):
            row[i] = (row[i]-minmax[i][0]) / (minmax[i][1] - minmax[i][0])

dataset = [[50, 30], 
            [20, 90]]
print(dataset)
#calculate min and max for each column
minmax = dataset_minmax(dataset)
print(minmax)
normalize(dataset, minmax)
print(dataset)