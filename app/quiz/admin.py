from django.contrib import admin
from quiz import models as quiz_models


admin.site.register(quiz_models.Quiz)
admin.site.register(quiz_models.Question)
admin.site.register(quiz_models.Answer)
admin.site.register(quiz_models.AnswerScreen)
