from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .check_password import check_passwords_isalnum, check_passwords_size
from .math import send_math, check_math
from listings.models import Game


def register(request):
    if request.method == "POST":
        # get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # check passwords
        if check_passwords_size(password):
            if check_passwords_isalnum(password):
                if password == password2:
                    if User.objects.filter(username=username).exists():
                        messages.error(request, 'That username is taken')
                        return redirect('register')
                    else:
                        if User.objects.filter(email=email).exists():
                            messages.error(request, 'That email is used')
                            return redirect('register')
                        else:
                            user = User.objects.create_user(
                                username=username,
                                first_name=first_name,
                                last_name=last_name,
                                email=email,
                                password=password
                            )

                            user.save()
                            messages.success(request, 'You are now registered and can log in')
                            return redirect('login')
                else:
                    messages.error(request, 'Passwords do not match')
                    return redirect('register')
            else:
                messages.error(request, 'Password should have number and character')
                return redirect('register')
        else:
            messages.error(request, 'passwords length should be 8')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        check_box = request.POST['check_box']
        math = request.POST['math']

        if check_math(math, check_box):
            user = auth.authenticate(
                username=username,
                password=password
            )

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'You are log in')
                return redirect('dashboard')
            else:
                messages.error(request, 'Username or password not match')
                return redirect('login')
        else:
            messages.error(request, 'Wrong math')
            return redirect('login')

    else:
        math = {
            "math": send_math()
        }
        return render(request, 'accounts/login.html', math)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out.')
        return redirect('index')


def dashboard(request):
    games = Game.objects.order_by('-list_date')[:3]

    context = {
        'games': games
    }
    return render(request, 'accounts/dashboard.html', context)
