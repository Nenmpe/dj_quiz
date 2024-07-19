from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('api/get-quiz/', get_questions, name='get_quiz'),
    path('quiz/', quiz, name='quiz'),
]
