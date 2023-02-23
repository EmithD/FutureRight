import datasetClass

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

modelLogReg = LogisticRegression()
modelLogReg.fit(datasetClass.trainingX, datasetClass.trainingy)

predictionsLogReg = modelLogReg.predict(datasetClass.testingX)

score = accuracy_score(datasetClass.testingy, predictionsLogReg)
print("Logistic Regression = ", score)