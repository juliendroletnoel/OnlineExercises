from django.http.response import HttpResponseBadRequest
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json

from ExercisesGenerator.ExerciseGenerator import ExerciseGenerator
# Create your views here.

exercise_generator = ExerciseGenerator()

def index(request):
    """
    Displays the main page
    """
    return render(request, 'lostislandapp/index.html')

def newgame(request):
    """
    Displays the options to start the game
    """

    available_exercises_types = exercise_generator.get_available_exercise_types()
    return render(request, 'lostislandapp/newgame.html', {'exercises_types' : available_exercises_types})

def request_available_body_parts(request, exercisetypename):
    """
        Returns available body parts based on given exercise name
        Returns a BadRequest error if given exercise_type_name is unknown by exercise_generator
    """

    try:
        available_body_parts = exercise_generator.get_available_body_part_name(exercisetypename)
    except ValueError as e:
        return HttpResponseBadRequest(e)

    formatted_response = json.dumps(tuple(available_body_parts))
    return HttpResponse(formatted_response)

def game(request):
    """
    Displays the main game page where the player
    can interact with the game
    """

    if request.method == 'POST':
        print ('Sent method is POST!')

    return render(request, 'lostislandapp/game.html')


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
