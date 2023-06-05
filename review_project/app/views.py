from django.shortcuts import render
from .forms import SalaryForm


def calc_salary(wage, time):
    return wage * time


def index(request):
    form = SalaryForm()
    message = ""
    if request.method == "POST":
        wage = int(request.POST["wage"])
        time = int(request.POST["time"])
        salary = calc_salary(wage, time)
        message = "あなたの給与は" + str(salary) + "円です。"
    return render(request, 'app/index.html', {
        'form': form,
        'message': message,
    })
