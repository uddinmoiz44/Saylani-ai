from django.shortcuts import HttpResponse
def home(request):
    return HttpResponse("Hello Django") 
def contact(request):
    return HttpResponse("contact")
