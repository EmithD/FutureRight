import datasetClass

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

modelNB = GaussianNB()
modelNB.fit(datasetClass.main_train_array_X, datasetClass.main_train_y)

predictionsNB = modelNB.predict(datasetClass.main_test_X)
score = accuracy_score(datasetClass.test_y, predictionsNB)

print("NB = ", score)