import datasetClass

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

modelDecisionTree = DecisionTreeClassifier()
modelDecisionTree.fit(datasetClass.X_train_split, datasetClass.y_train_split)

predictionsDecTree = modelDecisionTree.predict(datasetClass.X_test_split)

score = accuracy_score(datasetClass.y_test_split, predictionsDecTree)

print(score)