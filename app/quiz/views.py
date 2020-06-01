from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ExpensesForm
from quiz.models import Question


@login_required
def expenses(request):
    return render(request, 'quiz/expenses_question.html', {})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ExpensesForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/dashboard/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ExpensesForm()

    return render(request, 'name.html', {'form': form})
