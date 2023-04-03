import joblib

age = 17
gender_value = 1
openness = 7
neuroticism = 4
conscientiousness = 7
agreeableness = 3
extraversion = 2

personality_values_1 = [[gender_value, age, openness, neuroticism,
                         conscientiousness, agreeableness, extraversion]]


model = joblib.load(
    'BackEnd\\Models\\PersonalityTestLogisticRegression.joblib')
print(model.predict(personality_values_1))
