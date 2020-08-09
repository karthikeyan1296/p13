from django.urls import path
from rsk1 import views
app_name="rsk1"

urlpatterns = [
    path('trail/',views.trail,name="trail"),
    path('profile/',views.profile,name="profile"),
    path('base/',views.base,name="base"),
    path('home/',views.home,name="home"),
]