import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

data = pd.read_csv('parkinsons.csv')

data = data.drop(['name'], axis=1)

corr_matrix = data.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
highly_correlated_features = [column for column in upper.columns if any(upper[column] > 0.90)]
data = data.drop(columns=highly_correlated_features)

def calculate_prior(df, Y):
    classes = sorted(df[Y].unique())
    prior = [len(df[df[Y] == i]) / len(df) for i in classes]
    return prior

def calculate_likelihood_gaussian(df, feat_name, feat_val, Y, label):
    df = df[df[Y] == label]
    mean, std = df[feat_name].mean(), df[feat_name].std()
    p_x_given_y = (1 / (np.sqrt(2 * np.pi) * std)) * np.exp(-((feat_val - mean) ** 2 / (2 * std ** 2)))
    return p_x_given_y

def naive_bayes_gaussian(df, X, Y, features):
    prior = calculate_prior(df, Y)
    labels = sorted(df[Y].unique())

    Y_pred = []
    for x in X:
        likelihood = [1] * len(labels)
        for j in range(len(labels)):
            for i, feature in enumerate(features):
                likelihood[j] *= calculate_likelihood_gaussian(df, feature, x[i], Y, labels[j])

        post_prob = [1] * len(labels)
        for j in range(len(labels)):
            post_prob[j] = likelihood[j] * prior[j]

        Y_pred.append(np.argmax(post_prob))

    return np.array(Y_pred)

def evaluate_model(test_size):
    train, test = train_test_split(data, test_size=test_size, random_state=30)
    features = data.columns.drop('status')  
    X_train = train[features].values
    Y_train = train['status'].values
    X_test = test[features].values
    Y_test = test['status'].values

    Y_pred = naive_bayes_gaussian(train, X_test, 'status', features)

    accuracy = accuracy_score(Y_test, Y_pred)
    conf_matrix = confusion_matrix(Y_test, Y_pred)
    class_report = classification_report(Y_test, Y_pred)

    return accuracy, conf_matrix, class_report

results = {}

for split in np.arange(0.1, 0.31, 0.01):
    accuracy, conf_matrix, class_report = evaluate_model(split)
    results[split] = accuracy

best_split = max(results, key=results.get)
best_accuracy, best_conf_matrix, best_class_report = evaluate_model(best_split)
best_training_percentage = (1 - best_split) * 100

print(f"Training Percentage: {best_training_percentage:.2f}%")
print(f"Accuracy: {best_accuracy}")
print("Confusion Matrix:")
print(best_conf_matrix)
print("Classification Report:")
print(best_class_report)
print("\n")

train_sizes = [(1 - k) * 100 for k in results.keys()]
accuracies = list(results.values())
plt.figure(figsize=(10, 6))
plt.plot(train_sizes, accuracies, marker='o')
plt.title('Training Percentage vs. Accuracy')
plt.xlabel('Training Percentage (%)')
plt.ylabel('Accuracy')
plt.grid(True)
plt.show()