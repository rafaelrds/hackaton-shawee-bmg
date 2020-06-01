from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def dash_home(request):
    if not request.user.profile.answered_quiz:
        return redirect('quiz')

    return render(request, 'dashboard/home.html', {})
