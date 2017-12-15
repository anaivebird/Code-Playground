from threading import Thread
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse
from app.snake import get_run
import app.maze
import app.snake
from app.models import Submission


def home_view(request):
    return render(request, 'index.html')



def login_view(request):
    if request.method == 'POST':
        if request.POST['tab-select'] == 'register':
            User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['pass'])
            user = authenticate(username=request.POST['user'], password=request.POST['pass'])
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            raise PermissionDenied
        else:
            login(request, user)
        return redirect(reverse('home'))
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))


def about_view(request):
    return render(request, 'about.html')

def hot_view(request):
    return render(request, 'Hotgames.html')
def ai_view(request):
    return render(request, 'ai.html')

def games_view(request):
    return render(request, 'games.html')
def beginner_view(request):
    return render(request, 'Beginner.html')
def intermediate_view(request):
    return render(request, 'Intermediate.html')
def advanced_view(request):
    return render(request, 'Advanced.html')
def link_view(request):
    return render(request, 'link.html')
def snake_view(request):
    data = dict()
    data["code"] = get_run()
    return render(request, 'snake.html', data)
def fivechess_view(request):
    return render(request, 'fivechess.html')
def maze_demo(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            raise PermissionDenied
        submission = Submission.objects.create(user=request.user, lang=request.POST['lang'], code=request.POST['code'])
        Thread(target=app.maze.gen_output, args=(submission.pk, submission.code, submission.lang)).start()
        return redirect(reverse('submission', kwargs={'pk': submission.pk}))
    return render(request, 'maze.html')


def snake_demo(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
             raise PermissionDenied
        data = dict()
        data['run'] = request.POST['run']
        return HttpResponse(app.snake.gen_output(data))
    return render(request, 'snake.html')

def submission_display(request, pk):
    return render(request, 'submission.html', context={
        'submission': Submission.objects.get(pk=pk)
    })
