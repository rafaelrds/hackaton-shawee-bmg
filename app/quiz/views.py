from django.shortcuts import render
from quiz.models import Question


def test_view(request):
    q = Question.objects.last()

    return render(request, 'index.html', {'q': q})

