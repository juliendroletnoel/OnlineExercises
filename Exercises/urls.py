from django.urls import path

from . import views

urlpatterns = [
    # exercise's appalication index page
    path('', views.index, name='index'),

    # new game page (game settings selection)
    path('newgame', views.newgame, name='newgame'),

    # playing game
    path('game', views.game, name='game')
]