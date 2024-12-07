from .forms import UserRegister
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import webbrowser
from .models import *


def menu(request):
    text = 'Природные товары для красоты и здоровья!'
    list = ['надежная упаковка', 'высокое качество продукции', 'вся продукция сертифицирована']
    context = {
        'text': text,
        'list': list
    }
    return render(request, 'fourth_task\menu.html', context)


def platform(request):
    return render(request, 'fourth_task\platform.html')


def buyer(request):
    Buyers = Buyer.objects.all()
    context = {
        "Buyers": Buyers,
    }
    return render(request, 'fourth_task\platform.html', context)


def games(request):
    title = 'КАТОЛОГ ИГР'
    Games = Game.objects.all()
    context = {
        'title': title,
        'Games':Games
    }
    return render(request, 'fourth_task\games.html', context)



def registration_page(request):
    users_buyer = Buyer.objects.all()
    users = [i.name for i in users_buyer]
    info = {}
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            #Обработка данных формы
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif username in users:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse(f"{webbrowser.open("http://127.0.0.1:8000/platform/")}!")
            else:
                Buyer.objects.create(
                    name=username,
                    balance=1000,
                    age=int(age)
                )
                return HttpResponseRedirect("/platform/")
    else:
        form = UserRegister()
    return render(request, 'fourth_task/registration_page.html', {'form': form, 'info': info})


def cart(request):
    return render(request, 'fourth_task/cart.html')
# Create your views here.
