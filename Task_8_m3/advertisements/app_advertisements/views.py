from django.shortcuts import render
from django.http import HttpResponse

# запрос на отображение глав. страницы сайта (inde.html)
def index(reqest):
    return HttpResponse('успешное подключение')