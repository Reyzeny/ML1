def confusion_matrix(actual, predicted):
    unique = set(actual)
    matrix = [list() for x in unique]
    for i in range(len(unique)):
        matrix[i] = [0 for x in unique]
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i
    for i in range(len(actual)):
        x = lookup[actual[i]]
        y = lookup[predicted[i]]
        matrix[x][y] += 1
    return unique, matrix

def print_confusion_matrix(unique, matrix):
    print('a ', ' '.join(str(x) for x in unique))
    print('p---')
    for i, value in enumerate(unique):
        print(value,"|", ' '.join(str(x) for x in matrix[i]))

actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,1,0,0,1,0,1,1,1]
unique, matrix = confusion_matrix(actual, predicted)
print_confusion_matrix(unique, matrix)