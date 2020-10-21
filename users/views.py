# Users view

# Django
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Exceptions
from django.db.utils import IntegrityError

# Form
from users.forms import LoginForm, RegisterForm

# Roles
from rolepermissions.roles import assign_role
from rolepermissions.checkers import has_role

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data

            if not user_exist(form_data['username']):
                return render(request, 'users/login_view.html', {'error': "User doesn't exist", 'form': form})
            else:
                user = authenticate(request, username=form_data['username'], password=form_data['password'])

            if user:
                login(request, user)
                return redirect('items')
            else:
                return render(request, 'users/login_view.html', {'error': 'Invalid email or password', 'form': form})

    else:
        form = LoginForm()

    if request.method == 'GET':
        if request.user.is_authenticated:
           return redirect('items')

    return render(request, 'users/login_view.html', {'form': form})


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data

            if form_data['password'] != form_data['password_confirm']:
                return render(request, 'users/register_view.html', {'error': 'Password confirmation does not match', 'form': form})

            try:
                user = User.objects.create_user(
                    username = form_data['username'],
                    password = form_data['password']
                )
            except IntegrityError:
                # If user already exists
                return render(request, 'users/register_view.html', {'error': 'User already exist', 'form': form})

            if form_data['is_seller']:
                assign_role(user, 'seller')
            else:
                assign_role(user, 'buyer')

            user.email = form_data['email']
            user.first_name = form_data['first_name']
            user.last_name = form_data['last_name']
            user.save()

            return redirect('login')
    else:
        form = RegisterForm()

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('items')

    return render(request, 'users/register_view.html', {'form': form})


@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return redirect('login')


def user_exist(username):
    return User.objects.filter(username=username).exists()