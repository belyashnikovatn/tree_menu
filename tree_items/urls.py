from django.urls import path
from . import views

urlpatterns = [
    path('', views.generic_view, {'template_name': 'home'}, name='home'),
    path('about/', views.generic_view,
         {'template_name': 'about'}, name='about'),
    path('contact/', views.generic_view,
         {'template_name': 'contact'}, name='contact'),
    path('team/', views.generic_view, {'template_name': 'team'}, name='team'),
    path('history/', views.generic_view,
         {'template_name': 'history'}, name='history'),
    path('partners/', views.generic_view,
         {'template_name': 'partners'}, name='partners'),
    path('mock/', views.generic_view,
         {'template_name': 'mock'},  name='mock'),
]
