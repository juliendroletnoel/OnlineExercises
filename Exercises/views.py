from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    """
    Displays the main page
    """
    return render(request, 'exercises/index.html')

def newgame(request):
    """
    Displays the options to start the game
    """

    difficulty_levels = ('beginner', 'advanced', 'beast')
    exercises_types = ('muscular', 'cardio', 'balance')
    body_parts_names = ('chest', 'shoulders', 'biceps', 'triceps')

    return render(request, 'exercises/newgame.html', {'difficulty_levels' : difficulty_levels,\
                                                      'exercises_types' : exercises_types, \
                                                      'body_parts_names' : body_parts_names})

def game(request):
    """
    Displays the main game page where the player
    can interact with the game
    """

    if request.method == 'POST':
        print ('Sent method is POST!')

    return render(request, 'exercises/game.html')


def gatter_food_exercise(request):
    """ Exercise to gather food """
    pass

def gatter_water_exercise(request):
    """ Exercise to gather water """
    pass

def build_shelter(request):
    """ Exercise to build a shelter """
    pass

def build_a_raft(request):
    """ Exercise to build a Raft """
    pass
