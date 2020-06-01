from django.shortcuts import render


def dash_home(request):
    return render(request, 'dashboard/home.html', {})


def dash_home_poor(request):
    return render(request, 'dashboard/home2.html', {})
