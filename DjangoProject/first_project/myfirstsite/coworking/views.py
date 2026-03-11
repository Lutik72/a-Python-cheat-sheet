from django.http import HttpResponse
from django.shortcuts import render


def coworking_page(request):
    template = "coworking/index.html"
    title = "Уютная кофейня"
    header1 = "💻 Коворкинг-зона"
    subtitle = "Коворкинг с ароматом кофе — твой второй офис в сердце города"

    context = {
        "title": title,
        "subtitle": subtitle,
        "header1" : header1,
    }
    return render(request, template, context)
