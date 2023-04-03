import joblib

acedemicPerformance = joblib.load(
    'BackEnd\\Models\\academicPerformance.joblib')

predictions = acedemicPerformance.predict([[2, 31, 2, 11, 4, 8, 2, 0]])

print(predictions)
