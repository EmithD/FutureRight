import datasetClass

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

modelKNN = KNeighborsClassifier()
modelKNN.fit(datasetClass.trainingX, datasetClass.trainingy)

predictionKNN = modelKNN.predict(datasetClass.testingX)

score = accuracy_score(datasetClass.testingy, predictionKNN)
print("KNN = ", score)