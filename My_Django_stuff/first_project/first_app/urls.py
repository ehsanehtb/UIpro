from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('',views.index,name='index'),
    path('filter/',views.filter,name='filter'),
    path('movie1/',views.movie1,name='movie1'),
    path('play/',views.play,name='play'),
]
