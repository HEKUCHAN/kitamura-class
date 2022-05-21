from django.shortcuts import render

from forms import CalcBmiForm
from calc import calculate_bmi
from message import results_message, type_message

def calcbmi(request):
    params = {
        'forms': CalcBmiForm,
        'result': '',
        'type': ''
    }

    if request.method == 'POST':
        params["forms"] = CalcBmiForm(request.POST)
        bmi = calculate_bmi(float(request.POST['height'])), float(request.POST['width'])
        bmi = round(bmi, 1)
        params["result"] = str(results_message(bmi))
        params["type"] = str(type_message(bmi))

    return render(request, 'calcbmi.html', params)