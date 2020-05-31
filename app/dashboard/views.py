from django.shortcuts import render


def dash_home(request):
    return render(request, 'dashboard/home.html', {})
