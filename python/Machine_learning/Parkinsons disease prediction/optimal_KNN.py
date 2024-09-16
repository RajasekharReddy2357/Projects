import csv
import math
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib.pyplot as plt

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

max_accuracy = 0
best_k = None
best_train_percent = None
best_k_accuracies = [0] * 20  
train_percent_acc = []
best_predictions = []
best_actual_labels = []

for train_percent in range(60, 81, 1):
    train_data, test_data = train_test_split(data, test_size=(100 - train_percent)/100, random_state=30)
    k_accuracies = [0] * 20 
    
    for k in range(1, 21):
        predictions = [predict_classification(get_neighbors(train_data, test, k)) for test in test_data]
        actual_labels = get_labels(test_data)
        accuracy = accuracy_score(actual_labels, predictions)
        k_accuracies[k-1] = accuracy  
        
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            best_k = k
            best_train_percent = train_percent
            best_k_accuracies = k_accuracies[:]  
            best_predictions = predictions
            best_actual_labels = actual_labels

    train_percent_acc.append(max(k_accuracies))  

plt.figure()
plt.plot(range(60, 81, 1), train_percent_acc)
plt.title('Training Percentage vs Maximum Accuracy')
plt.xlabel('Training Percentage')
plt.ylabel('Maximum Accuracy')
plt.grid(True)
plt.show()

plt.figure()
plt.plot(range(1, 21), best_k_accuracies)
plt.title(f'k Value vs Accuracy for Best Training Percentage: {best_train_percent}%')
plt.xlabel('k Value')
plt.ylabel('Accuracy')
plt.grid(True)
plt.show()

print(f"Best training percentage: {best_train_percent}%")
print(f"Optimal k value: {best_k}")
print(f"Maximum Accuracy: {max_accuracy}")

print("Confusion Matrix for Best Model:")
print(confusion_matrix(best_actual_labels, best_predictions))

print("Classification Report for Best Model:")
print(classification_report(best_actual_labels, best_predictions))
