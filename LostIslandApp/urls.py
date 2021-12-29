from django.urls import path

from . import views

urlpatterns = [
    # exercise's appalication index page
    path('', views.index, name='index'),

    # new game page (game settings selection)
    path('newgame', views.newgame, name='newgame'),

    # playing game
    path('game', views.game, name='game'),

    # get body parts name
    path('request_available_body_parts/<str:exercisetypename>/', views.request_available_body_parts)
]