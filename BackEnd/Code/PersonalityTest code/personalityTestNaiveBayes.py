import datasetClass

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

modelNB = GaussianNB()
modelNB.fit(datasetClass.trainingX, datasetClass.trainingy)

predictionsNB = modelNB.predict(datasetClass.testingX)
score = accuracy_score(datasetClass.testingy, predictionsNB)

print("NB = ", score)