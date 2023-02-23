import pandas as pd

#Training datasets
trainingDf = pd.read_csv('BackEnd\\Personality Test\\Data\\train.csv')
trainingDf['Gender'].replace({'Male':1, 'Female':0}, inplace=True)
trainingX = trainingDf.drop(columns=['Personality (Class label)'])
trainingy = trainingDf["Personality (Class label)"]

#Testing datasets
testingDf = pd.read_csv('BackEnd\\Personality Test\\Data\\test.csv')
testingDf['Gender'].replace({'Male':1, 'Female':0}, inplace=True)
testingX = testingDf.drop(columns=['Personality (class label)'])
testingy = testingDf["Personality (class label)"]