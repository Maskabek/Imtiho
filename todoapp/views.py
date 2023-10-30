from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404

from .forms import LoginForm, RegistrationForm, TodoForm
from .models import Todo


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form = LoginForm()
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def home_view(request):
    user = request.user
    if user == 'AnonymousUser':
        return redirect('register')
    else:
        todos = Todo.objects.filter(owner=request.user)
        return render(request, 'home.html', {'todos': todos})


def add_todo(request):
    user = request.user
    if user.is_anonymous:
        return redirect('register')

    if request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = user
            todo.save()
            return redirect('home')
    else:
        form = TodoForm()

    return render(request, 'todo/add.html', context={'form': form})


def edit_todo(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if todo.owner != request.user:
        return redirect('home')

    if request.method == 'POST':
        if 'delete' in request.POST:
            todo.delete()
            return redirect('home')
        else:
            form = TodoForm(data=request.POST, instance=todo)
            if form.is_valid():
                form.save()
                return redirect('home')
    else:
        form = TodoForm(instance=todo)

    return render(request, 'todo/edit.html', {'form': form, 'todo': todo})
