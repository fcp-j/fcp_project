from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Genre
from games.models import Game

# Create your views here.
@login_required
def index(request):
    genres = Genre.objects.all().order_by('name')
    member = request.user.member
    member.remove_expired_rewards

    return render(request, 'genres/index.html', {'genres': genres, 'member': member})

@login_required
def show(request, name):
    genre = Genre.objects.get(name=name)
    games = Game.objects.filter(genre=genre).order_by('release_datetime')
    member = request.user.member
    member.remove_expired_rewards

    return render(request, 'genres/show.html', {'genre': genre, 'games': games, 'member': member})
