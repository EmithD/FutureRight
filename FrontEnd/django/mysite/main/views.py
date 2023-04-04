from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import joblib
import os
from django.conf import settings

# Create your views here.


def index(response):
    return render(response, "main/base.html", {})


def about_us(response):
    return render(response, "main/about_us.html", {})


def help(response):
    return render(response, "main/help.html", {})


def start_test(response):
    return render(response, "main/start_test.html", {})


def review_test(response):
    return render(response, "main/review_test.html", {})


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

        finalPred = model.predict(personality_values_1)[0]

    return render(response, "main/Review_Test.html", {'personality': finalPred})


# @csrf_exempt
# def academicTest(repsonse):

#     if repsonse.method == 'POST':
