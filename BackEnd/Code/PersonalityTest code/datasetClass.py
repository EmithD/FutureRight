import pandas as pd
from sklearn.model_selection import train_test_split

#Training datasets
trainingDf = pd.read_csv('BackEnd\\Data\\PersonalityTest\\train.csv')
# trainingDf['Gender'].replace({'Male':1, 'Female':0}, inplace=True)
trainingX = trainingDf.drop(columns=['Personality (Class label)', 'Gender', 'Age'])
trainingy = trainingDf["Personality (Class label)"]

#Testing datasets
testingDf = pd.read_csv('BackEnd\\Data\\PersonalityTest\\test.csv')
# testingDf['Gender'].replace({'Male':1, 'Female':0}, inplace=True)
testingX = testingDf.drop(columns=['Personality (class label)', 'Gender', 'Age'])
testingy = testingDf["Personality (class label)"]

#Test_Train splitting the Training dataset
X_train_split, X_test_split, y_train_split, y_test_split= train_test_split(trainingX, trainingy, test_size=0.2)