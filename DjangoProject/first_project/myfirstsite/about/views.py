from django.http import HttpResponse
from django.shortcuts import render


def about_page(request):
    template = 'about/index.html'
    return render(request, template)