from django.shortcuts import render
import logging

# Получаем экземпляр логгера
logger = logging.getLogger(__name__)

# Представление для главной страницы
def home(request):
    html = """
    <h1>Добро пожаловать на мой первый Django-сайт!</h1>
    <p>Меня зовут [Ваше имя]. Я начинающий Django-разработчик и это мое первое приложение.</p>
    """
    # Сохраняем данные о посещении страницы в логи
    logger.info('Посетил главную страницу')
    return render(request, 'home.html', {'html': html})

# Представление для страницы "о себе"
def about(request):
    html = """
    <h1>Обо мне</h1>
    <p>Привет! Меня зовут [Ваше имя] и я увлеченный программист. Этот сайт создан мной с использованием Django.</p>
    """
    # Сохраняем данные о посещении страницы в логи
    logger.info('Посетил страницу "О себе"')
    return render(request, 'about.html', {'html': html})
