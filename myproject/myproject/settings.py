import logging

from django.shortcuts import render

logger = logging.getLogger(__name__)

def home(request):
    html = "<h1>Добро пожаловать на мой первый Django-сайт!</h1><p>Здесь вы найдете много интересной информации о проекте и обо мне.</p>"
    logger.info('Посещена главная страница')
    return render(request, 'first_app/home.html', {'html': html})

def about(request):
    html = "<h1>Обо мне</h1><p>Привет! Меня зовут [ваше имя]. Я учусь программировать на Django и рад приветствовать вас на моем сайте.</p>"
    logger.info('Посещена страница "О себе"')
    return render(request, 'first_app/about.html', {'html': html})

# settings.py

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']



