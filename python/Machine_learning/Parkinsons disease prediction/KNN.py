import csv
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report

def load_and_prepare_data(filepath):
    dataset = []
    with open(filepath, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            features = [float(row[i]) for i in range(1, len(row)-1)]  
            label = int(row[-1])  
            dataset.append(features + [label])  
    return dataset

def euclidean_distance(vector1, vector2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(vector1[:-1], vector2[:-1])))

def get_neighbors(train_set, test_instance, k):
    distances = [(train, euclidean_distance(train, test_instance)) for train in train_set]
    distances.sort(key=lambda x: x[1])
    return [train[0] for train in distances[:k]]

def predict_classification(neighbors):
    votes = {}
    for neighbor in neighbors:
        label = neighbor[-1]
        if label in votes:
            votes[label] += 1
        else:
            votes[label] = 1
    sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
    return sorted_votes[0][0]

def get_labels(data_set):
    return [row[-1] for row in data_set]

data = load_and_prepare_data("parkinsons.csv")

train_data, test_data = train_test_split(data, test_size=0.25, random_state=30)

k = int(input("Enter the number of neighbors (K): "))

predictions = [predict_classification(get_neighbors(train_data, test, k)) for test in test_data]
actual_labels = get_labels(test_data)

print("Confusion Matrix:")
try:
    print(confusion_matrix(actual_labels, predictions))
except Exception as e:
    print("Error in generating confusion matrix:", e)
print("Accuracy:")
print(accuracy_score(actual_labels, predictions))
print("Classification Report:")
print(classification_report(actual_labels, predictions))