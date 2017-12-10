from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello, World!")

def test(request):
    return render(request, 'riddles/test.html', {})

def post(request):
    return HttpResponse("Здравствуйте, " + request.GET['TEXT_1'] + " " + request.GET['TEXT_2'])
