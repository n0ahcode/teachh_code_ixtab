from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('contribution/',views.contribution,name='contribution'),
    path('event/<int:id>/',views.event,name='event'),
    path('add',views.add,name='add')
]
