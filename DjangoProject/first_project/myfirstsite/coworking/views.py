from .models import Tariff
from django.shortcuts import render


def coworking_page(request):
    template = "coworking/index.html"
    title = "Уютная кофейня"
    header1 = "💻 Коворкинг-зона"
    subtitle = "Коворкинг с ароматом кофе — твой второй офис в сердце города"
    tariffs = Tariff.objects.filter(is_active=True).order_by('order')
  
    context = {
        "title": title,
        "subtitle": subtitle,
        "header1" : header1,
        'tariffs': tariffs,
    }
    return render(request, template, context)
