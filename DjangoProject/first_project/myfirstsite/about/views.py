from django.shortcuts import render


def about_page(request):
    template = 'about/index.html'
    title = "Меню - Уютная кофейня"
    subtitle = "Вдохновение в каждой чашке"
    header1 = "☕ Наше меню"

    context = {
        'title': title,
        'header1' : header1,
        "subtitle" : subtitle
    }
    return render(request, template, context)