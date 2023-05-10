from django.urls import path
from . import views

urlpatterns={
    path('g',views.index,name='index'),
}