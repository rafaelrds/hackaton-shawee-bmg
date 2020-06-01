from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def dash_home(request):
    profile = getattr(request.user, 'profile', None)
    if not profile:
        return render(request, 'dashboard/landing.html', {})
    if profile and not profile.answered_quiz:
        return redirect('quiz')

    return render(request, 'dashboard/home.html', {})
