from django.urls import path
from .views import mylogin, mylogaut, myregistration

app_name = 'profiles'

urlpatterns = [
    path('login/', mylogin, name='login'),
    path('logaut/', mylogaut, name='logaut'),
    path('registration/', myregistration, name='registration'),
]