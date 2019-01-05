from random import randrange
from random import seed
from csv import reader

def load_dataset(filename):
    file = open(filename, "r")
    lines = reader(file)
    dataset = list(lines)
    return dataset


def train_test_split(dataset, split=0.60):
    train = list()
    no_of_rows_needed = split * len(dataset)
    #print(dataset)
    
    dataset_copy = [row for row in dataset if row]
    
    while len(train) < no_of_rows_needed:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy


seed(1)
filename = 'iris.csv'
dataset = load_dataset(filename)
train, test = train_test_split(dataset)
print(test)
