from django.db import models


class Quiz(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Question(models.Model):
    position = models.IntegerField()
    text = models.TextField()
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')

    def __str__(self):
        return f'Question {self.position}'


class AnswerScreen(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return f'AnswerScreen for Answer {self.name}'


class Answer(models.Model):
    position = models.IntegerField()
    text = models.TextField()
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    screen = models.ForeignKey(
        AnswerScreen,
        on_delete=models.CASCADE,
        related_name='answer'
    )

    def __str__(self):
        return f'{self.text}'

