from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Главная страница')


"""def group_posts(request):
    return HttpResponse('Список мороженого')"""


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def group_posts(request, slug):
    return HttpResponse(f'Пост: {slug}')