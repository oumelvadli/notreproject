from django.urls import path
from . import views

urlpatterns={
    path('e',views.index,name='index'),
}