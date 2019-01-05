def accuracy(actual, prediction):
    correct = 0
    for i in range(len(actual)):
        if (actual[i]==prediction[i]):
            correct += 1
    return (correct/float(len(actual))) * 100.0


actual = [0,0,0,0,0,1,1,1,1,1]
predicted = [0,1,0,0,0,1,0,1,1,1]
print(accuracy(actual, predicted))