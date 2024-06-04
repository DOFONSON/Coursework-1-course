from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})
def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})
def range(request):
    return render(request, 'main/range.html', {'title': 'Ассортимент'})
def profile(request):
    return render(request, 'main/profile.html', {'title': 'Профиль'})
def contact(request):
    return render(request, 'main/contact.html', {'title': 'Контакты'})