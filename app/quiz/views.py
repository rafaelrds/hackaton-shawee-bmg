from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from quiz.models import Question


@login_required
def expenses(request):
    return render(request, 'quiz/expenses_question.html', {})

