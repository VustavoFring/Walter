from django.shortcuts import render
from django.http import HttpResponse

# запрос на отображение глав. страницы сайта (inde.html)
def index(request):
    return render(request, 'index.html')

# запрос на отображение страници топ продавцов
def top_sellers(request):
    return render(request, 'top-sellers.html')