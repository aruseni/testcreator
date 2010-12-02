from tests.models import Test, Question, Answer
from django.contrib import admin

admin.site.register(Test)

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
