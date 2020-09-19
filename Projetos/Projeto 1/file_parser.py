import csv

def parse_input_distance(file_path):
    distance_matrix = []
    with open(file_path) as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            distance_matrix.append(row)
    return distance_matrix
