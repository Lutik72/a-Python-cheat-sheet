from django.shortcuts import render


def about_page(request):
    template = 'about/index.html'
    title = "Меню - Уютная кофейня"
    subtitle = "Вдохновение в каждой чашке"

    context = {
        'title': title,
        "subtitle" : subtitle
    }
    return render(request, template, context)