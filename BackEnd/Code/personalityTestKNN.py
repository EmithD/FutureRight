import datasetClass

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

modelKNN = KNeighborsClassifier()
modelKNN.fit(datasetClass.X_train_split, datasetClass.y_train_split)

predictionKNN = modelKNN.predict(datasetClass.X_test_split)

score = accuracy_score(datasetClass.y_test_split, predictionKNN)
print(score)