from django.contrib import admin

from main.models import *


# Register your models here.

class AnswerAdmin(admin.StackedInline):
    # This is used if a single foreign key has multiple object, i.e. one question has one answer with multiple choices which is shown as answers for single question
    model = Answer


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerAdmin]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Category)
