from django.urls import include, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^contact/', views.contact, name='contact'),
]
