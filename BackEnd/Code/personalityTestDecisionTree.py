import datasetClass

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

modelDecisionTree = DecisionTreeClassifier()
modelDecisionTree.fit(datasetClass.trainingX, datasetClass.trainingy)

predictionsDecTree = modelDecisionTree.predict(datasetClass.testingX)

score = accuracy_score(datasetClass.testingy, predictionsDecTree)

print(score)