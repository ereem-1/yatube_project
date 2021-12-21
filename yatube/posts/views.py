from django.shortcuts import HttpResponse, render

# Create your views here.
def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        # В словарь можно передать переменную
        'title': title,
        # А можно сразу записать значение в словарь. Но обычно так не делают
        'text': 'Главная страница',
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context)