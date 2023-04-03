import joblib

age = 22
gender_value = 0
openness = 6
neuroticism = 3
conscientiousness = 7
agreeableness = 5
extraversion = 4

personality_values_1 = [[gender_value, age, openness, neuroticism,
                         conscientiousness, agreeableness, extraversion]]


model = joblib.load(
    'BackEnd\\Models\\PersonalityTestLogisticRegression.joblib')
print(model.predict(personality_values_1))
