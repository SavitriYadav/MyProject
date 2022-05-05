from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('home/', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('contact/', views.contact, name='contact'),
    path('stephen/', views.stephen, name='stephen'),
    path('vanita/', views.vanita, name='vanita'),
    path('swapnil/', views.swapnil, name='swapnil'),
    path('pritam/', views.pritam, name='pritam'),
    path('vfx/', views.vfx, name='vfx')

]