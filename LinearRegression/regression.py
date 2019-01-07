from csv import reader

def split_test_train(dataset, split=0.60):
    train_row_no = split * len(dataset)
    for i in range(len(dataset)):
        

def load_csv(filename):
    dataset = open(filename)
    lines = reader(dataset)
    data = list(lines)
    for row in data:
        convert_each_item_to_float(row)
    return data

def convert_each_item_to_float(row):
    for i in range(len(row)):
        row[i] = float(row[i].strip())

def mean(array):
    total = 0.0
    for i in range(len(array)):
        total+=array[i]
    return total/len(array)

def calculate_coefficient(claim_array, amount_array, mean_claim, mean_amount):
    up = 0.0
    down = 0.0
    for i in range(len(claim_array)):
        up_val = (claim_array[i]-mean_claim) * (amount_array[i]-mean_amount)
        up+=up_val
        down+=(claim_array[i]-mean_claim)**2
    return up/down

def calculate_constant(mean_amount, mean_claim, b1):
    return mean_amount - (b1 * mean_claim)
    

def simple_linear_regression(dataset):
    claim_array = [row[0] for row in dataset]
    amount_array = [row[1] for row in dataset]
    print(claim_array)
    print(len(claim_array))
    print(amount_array)
    print(len(amount_array))
    mean_claim = mean(claim_array)
    mean_amount = mean(amount_array)
    b1 = calculate_coefficient(claim_array, amount_array, mean_claim, mean_amount)
    b0 = calculate_constant(mean_amount, mean_claim, b1)
    print("model is y=%f + %fx" % (b0, b1))
    return b0, b1

def predict(claim):     #will return amount
    filename = '../Datasets/swedish-insurance.csv'
    #dataset = load_csv(filename)
    dataset = [[1, 1], [2, 3], [4, 3], [3, 2], [5, 5]]
    b0, b1 = simple_linear_regression(dataset)
    amount = b0 + (b1 * claim)
    return amount

#print(load_csv('../Datasets/swedish-insurance.csv'))
print(predict(1))