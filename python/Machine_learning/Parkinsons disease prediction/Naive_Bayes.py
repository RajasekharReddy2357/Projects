import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

sns.set_style("darkgrid")
data = pd.read_csv('parkinsons.csv')
numeric_data = data.select_dtypes(include=[np.number])
corr = numeric_data.corr(method="pearson")
cmap = sns.diverging_palette(250, 354, 80, 60, center='dark', as_cmap=True)
plt.figure(figsize=(10, 8))
sns.heatmap(corr, vmax=1, vmin=-.5, cmap=cmap, square=True, linewidths=.2)
plt.show()
data = data.drop(['name'], axis=1)

corr_matrix = data.corr().abs()
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
highly_correlated_features = [column for column in upper.columns if any(upper[column] > 0.90)]
data = data.drop(columns=highly_correlated_features)
updated_corr = data.corr(method="pearson")
plt.figure(figsize=(10, 8))
sns.heatmap(updated_corr, vmax=1, vmin=-.5, cmap=cmap, square=True, linewidths=.2)
plt.title("Correlation Heatmap After Removing Highly Correlated Features")
plt.show()

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

train, test = train_test_split(data, test_size=0.25, random_state=30)
features = data.columns.drop('status')  
X_train = train[features].values
Y_train = train['status'].values
X_test = test[features].values
Y_test = test['status'].values
Y_pred = naive_bayes_gaussian(train, X_test, 'status', features)
conf_matrix = confusion_matrix(Y_test, Y_pred)
accuracy = accuracy_score(Y_test, Y_pred)
class_report = classification_report(Y_test, Y_pred)
print("Confusion Matrix:")
print(conf_matrix)
print("\nAccuracy:", accuracy)
print("\nClassification Report:")
print(class_report)