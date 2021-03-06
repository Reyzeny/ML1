from csv import reader

def load_dataset(filename):
    file = open(filename, "r")
    lines = reader(file)
    data = list(lines)
    return data

def load_dataset2(filename):
    dataset = []
    with open(filename, "r") as file:
        lines = reader(file)
        for index, row in enumerate(lines):
            if not row:
                continue
            dataset.append(row)
            print(index, row)
    return dataset


def str_column_to_float(dataset, column):
    for row in dataset:
        if row:
            row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
    column_values = [row[column] for row in dataset if row]
    unique_values = set(column_values)
    lookup = dict()
    for i, value in enumerate(unique_values):
        lookup[value] = i
    for row in dataset:
        if row:
            row[column] = lookup[row[column]]
    return lookup


filename = 'iris.csv'
#dataset = load_dataset(filename)
print(load_dataset2(filename))
# str_column_to_float(dataset, 0)
# str_column_to_float(dataset, 1)
# str_column_to_float(dataset, 2)
# str_column_to_float(dataset, 3)
# print(str_column_to_int(dataset, 4))
# print(dataset)