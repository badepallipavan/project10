from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2_bye(request):
    return render(request,'app2_bye.html')

    