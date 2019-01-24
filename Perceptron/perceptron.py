import reader from csv

def load_csv(filename):
    dataset = []
    with open filename as file:
        lines = reader(file)
        for row in lines:
            if row:
                dataset.append(row)
        return dataset