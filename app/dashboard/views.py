from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def dash_home(request):
    profile = getattr(request.user, 'profile', None)
    if profile and not profile.answered_quiz:
        return redirect('quiz')
    else:
        return redirect('register')

    return render(request, 'dashboard/home.html', {})
