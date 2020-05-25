from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey! {username}. Your profile is successfully created!')
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    username = request.user.username
    designation = request.user.profile.designation
    team = request.user.supervisor.all()
    team_member_no = len(team)
    supervisor = request.user.member.all().first().supervisor
    context = {
        'username': username,
        'designation': designation,
        'supervisor': supervisor,
        'team': team,
        'team_member_no': team_member_no,
    }
    return render(request, 'users/profile.html', context)