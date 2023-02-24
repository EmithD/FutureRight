import joblib

model = joblib.load('BackEnd\\Models\\PersonalityTestLogisticRegression.joblib')

genderInput = float(input("Enter your gender: "))
age = float(input("Enter your age: "))
openness = float(input("Enter your openness rate: "))
neuroticism = float(input("Enter your neuroticism rate:"))
conscientiousness = float(input("Enter your conscientiousness: "))
agreeable = float(input("Enter your agreeable rate: "))
extraversion = float(input("Enter your extraversion rate: "))

testArray = [[genderInput, age, openness, neuroticism, conscientiousness, agreeable, extraversion]]

print(model.predict(testArray))