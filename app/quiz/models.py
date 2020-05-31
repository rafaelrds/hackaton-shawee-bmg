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


class Answer(models.Model):
    position = models.IntegerField()
    text = models.TextField()
    is_correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    def __str__(self):
        return f'Answer {self.position}'


class AnswerScreen(models.Model):
    text = models.TextField()
    answer = models.OneToOneField(
        Answer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'AnswerScreen for Answer {self.position}'
