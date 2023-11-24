from django.urls import path
from .views import apartment_listing

urlpatterns = [
    path("", apartment_listing, name="home"  )
]