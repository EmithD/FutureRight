import datasetClass

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

modelRandomForest = RandomForestClassifier()
modelRandomForest.fit(datasetClass.trainingX, datasetClass.trainingy)

predictionsRandomForest = modelRandomForest.predict(datasetClass.testingX)

score = accuracy_score(datasetClass.testingy, predictionsRandomForest)

print("Random Forest = ", score)