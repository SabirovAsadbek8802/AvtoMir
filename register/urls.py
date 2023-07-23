from django.urls import path
from . import views

urlpatterns = [
    path("", views.registration, name="register"),
    path("thank-you", views.thank_you),
    path("sign-in", views.create, name="signin")
]