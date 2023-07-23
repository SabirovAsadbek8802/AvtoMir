from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Accounts



# Create your views here.
def registration(request):
    return render(request, "register.html")


def thank_you(request):
    return render(request, "thank_you.html")


def create(request):
    if request.method == "POST":
        person = Accounts()
        person.first_name = request.POST.get("first_name")
        person.last_name = request.POST.get("last_name")
        person.username = request.POST.get("username")
        person.email = request.POST.get("email")
        person.password = request.POST.get("password")
        person.save()
    return HttpResponseRedirect("/sign-in")