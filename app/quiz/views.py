from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ExpensesForm
from quiz.models import Quiz, Question, Answer


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

  
@login_required
def main_quiz(request):
    last_quiz = Quiz.objects.last()

    request.session['quiz_id'] = last_quiz.pk

    return render(request, 'quiz/welcome.html', {'be_clean': True, 'quiz': last_quiz})

@login_required
def quiz_question(request, quiz_id, question_position):
    quiz = Quiz.objects.get(pk=quiz_id)

    question = Question.objects.get(quiz=quiz, position=question_position)

    return render(request, 'quiz/question.html', {'be_clean': True, 'question': question})


@login_required
def quiz_answer(request, ans_id):
    answer = Answer.objects.get(pk=ans_id)
    context = {
        'be_clean': True,
        'answer': answer,
        'question': answer.question,
        'quiz': answer.question.quiz,
    }

    if answer.is_correct:
        request.session['correct_count'] = request.session.get('correct_count', 0) + 1

    return render(request, 'quiz/answer.html', context)


@login_required
def quiz_finish(request):
    correct_count = request.session.get('correct_count')
    quiz_id = request.session.get('quiz_id')

    quiz = Quiz.objects.get(pk=quiz_id)

    profile = request.user.profile
    profile.answered_quiz = True
    profile.save()

    context = {'be_clean': True, 'points': correct_count / quiz.questions.count()}
    return render(request, 'quiz/finish.html', context)
