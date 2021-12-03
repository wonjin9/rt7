from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing),
    path('aboutus/', views.aboutus),
    path('contact/', views.contact),
    path('partners/', views.partners),
    path('portfolio/', views.portfolio),
    path('do/', views.do),
]