from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def MSD(request):
    return HttpResponse('<h2>Dhoni is best Cricketer..</h2>')

def Raina(request):
    return HttpResponse('<h2>Raina is best cricketer..</h2>')
