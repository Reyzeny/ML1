from random import randrange

def cross_validate_split(dataset, fold=3):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset)/fold)
    for i in range(fold):
        dummy_data = list()
        while len(dummy_data) < fold_size:
            index = randrange(len(dataset_copy))
            dummy_data.append(dataset_copy.pop(index))
        dataset_split.append(dummy_data)
    return dataset_split

data = [ [1],[2], [3], [4], [5], [6], [7], [8], [9] ]
print(cross_validate_split(data, 4))
