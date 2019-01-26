from random import seed
from csv import reader
from random import randrange

def load_csv(filename):
    dataset = []
    with open (filename, "r") as file:
        lines = reader(file)
        for row in lines:
            if not row:
                continue
            dataset.append(row)
    return dataset


def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def str_column_to_int(dataset, column):
    class_values = [row[column] for row in dataset]
    unique_items = set(class_values)
    lookup = dict()
    classification = dict()
    for i, value in enumerate(unique_items):
        lookup[value] = i
        classification[i] = value
    for row in dataset:
        row[column] = lookup[row[column]]
    return classification

def cross_validation_split(dataset, n_folds):
	dataset_split = list()
	dataset_copy = list(dataset)
	fold_size = int(len(dataset) / n_folds)
	for i in range(n_folds):
		fold = list()
		while len(fold) < fold_size:
			index = randrange(len(dataset_copy))
			fold.append(dataset_copy.pop(index))
		dataset_split.append(fold)
	return dataset_split


def train_test_split(dataset, split=0.6):
    train = []
    dataset_copy = [row for row in dataset]
    train_row_no = split * len(dataset_copy)
    while len(train) < train_row_no:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy


# Calculate accuracy percentage
def accuracy_metric(actual, predicted):
	correct = 0
	for i in range(len(actual)):
		if actual[i] == predicted[i]:
			correct += 1
	return correct / float(len(actual)) * 100.0




def train_weights(dataset, l_rate, n_epoch):
    weights = [0.0 for row in dataset[0]]
    for i in range(n_epoch):
        sum_error = 0.0
        for row in dataset:
            prediction = predict(row, weights)
            error = row[-1] - prediction
            sum_error += error
            weights[0] = weights[0] + (l_rate * error)
            for i in range(len(row)-1):
                weights[i+1] = weights[i+1] + (l_rate * error * row[i])
        #print('>epoch=%d, lrate=%.3f, error=%.3f' % (n_epoch, l_rate, sum_error))
    return weights
        

def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
    scores = list()
    for fold in folds:
        train_set = list(folds)
        train_set.remove(fold)
        train_set = sum(train_set, [])
        test_set = list()
        for row in fold:
            row_copy = list(row)
            test_set.append(row_copy)
            #row_copy[-1] = None
        predicted = algorithm(train_set, test_set, *args)
        actual = [row[-1] for row in fold]
        accuracy = accuracy_metric(actual, predicted)
        scores.append(accuracy)
    return scores


def predict(row, weight):
    activation = weight[0]
    for i in range(len(row)-1):
        activation += (weight[i+1] * row[i])
    return 1 if activation >= 0 else 0


def perceptron(train, test, l_rate, n_epoch, classification):
    predictions = list()
    weights = train_weights(train, l_rate, n_epoch)
    for row in test:
        prediction = predict(row, weights)
        predictions.append(prediction)
        print("acutal is ", classification[row[-1]], " predicted is ", classification[prediction])
    return predictions


seed(1)
dataset = load_csv("/home/pelumi/Documents/ML/Datasets/sonar-data.csv")
for i in range(len(dataset[0])-1):
    str_column_to_float(dataset, i)
classification = str_column_to_int(dataset, len(dataset[0])-1)  #should return { men: 1, women: 2 }
print("classification is ", classification)

n_folds = 5
l_rate = 0.00001
n_epoch = 5000
scores = evaluate_algorithm(dataset, perceptron, n_folds, l_rate, n_epoch, classification)
print('Scores: %s' % scores)
print('Mean Accuracy: %.3f%%' % (sum(scores)/float(len(scores))))
