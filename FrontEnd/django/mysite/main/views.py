from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import joblib
import os
from django.conf import settings
import csv

# Create your views here.

finalPersonality = []
streamArray = []


def careerRecommendation(stream, personality, academic_performance):

    theStreams = {
        0: 'arts',
        1: 'commerce',
        2: 'physical science',
        3: 'biological science',
        4: 'engineering technology',
        5: 'BIOSYSTEMS TECHNOLOGY'
    }

    finallyStream = theStreams[stream]

    careers = []
    path = os.path.join(settings.BASE_DIR, 'mysite\\TrainSet.csv')
    with open(path) as csvfile:
        csvreader = csv.DictReader(csvfile)

        # loop through rows
        for row in csvreader:
            if row['Stream'] == finallyStream:
                if row['Personality'] == personality:
                    if row['Academic Performance'] == academic_performance:
                        careers.append(row['Career'])
    return careers


def index(response):
    return render(response, "main/base.html", {})


def about_us(response):
    return render(response, "main/about_us.html", {})


def help(response):
    return render(response, "main/help.html", {})


def start_test(response):
    return render(response, "main/Start_Test.html", {})


@csrf_exempt
def review_test(response):

    if response.method == 'POST':

        stream = int(response.POST['stream'])
        streamArray.clear()
        streamArray.append(stream)
        sub_1 = int(response.POST['subject1'])
        sub_1_r = int(response.POST['sub1_result'])
        sub_2 = int(response.POST['subject2'])
        sub_2_r = int(response.POST['sub2_result'])
        sub_3 = int(response.POST['subject3'])
        sub_3_r = int(response.POST['sub3_result'])
        gen_eng = int(response.POST['gen_english'])

        academicValues = [
            [stream, sub_1, sub_1_r, sub_2, sub_2_r, sub_3, sub_3_r, gen_eng]]

        path = os.path.join(settings.BASE_DIR,
                            'mysite\\academicPerformance.joblib')
        model = joblib.load(path)

        finalPred = model.predict(academicValues)[0]

        print(stream, finalPersonality[0], finalPred)

        context = {'academics': finalPred,
                   'personality': finalPersonality[0], 'careers': careerRecommendation(stream, finalPersonality[0], finalPred)}

    return render(response, "main/Review_Test.html", context)


def therm_use(response):
    return render(response, "main/therm_use.html", {})


@csrf_exempt
def test(response):

    if response.method == 'POST':

        age = int(response.POST['age'])
        gender_str = str(response.POST['gender'])

        if gender_str == 'Male':
            gender_value = 1
        else:
            gender_value = 0

        openness = int(response.POST['openness'])
        neuroticism = int(response.POST['neuroticism'])
        conscientiousness = int(response.POST['conscientiousness'])
        agreeableness = int(response.POST['agreeableness'])
        extraversion = int(response.POST['extraversion'])

        personality_values_1 = [[gender_value, age, openness,
                                 neuroticism, conscientiousness, agreeableness, extraversion]]

        path = os.path.join(settings.BASE_DIR,
                            'mysite\\PersonalityTestLogisticRegression.joblib')
        model = joblib.load(path)

        finalPredPersonality = model.predict(personality_values_1)[0]
        finalPersonality.clear()
        finalPersonality.append(finalPredPersonality)

    return render(response, "main/acedemic_test.html", {})
