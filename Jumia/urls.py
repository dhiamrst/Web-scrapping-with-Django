from . import views
from django.urls import path

urlpatterns = [
    path('', views.page1, name='page1'),
]