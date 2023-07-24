from django.urls import path
from .views import registration, thank_you, createpost

urlpatterns = [
    path("", registration, name="register"),
    path("thank-you", thank_you),
    path("sign-in", createpost, name="signin") # type: ignore
]