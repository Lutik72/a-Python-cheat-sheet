from django.http import HttpResponse
from django.shortcuts import render


def about_page(request):
    template = 'about/index.html'
    title = "Меню - Уютная кофейня"

    context = {
        'title': title
    }
    return render(request, template, context)