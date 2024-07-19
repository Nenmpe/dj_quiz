from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import *
import random

# Create your views here.


def index(request):
    context = {
        'categories': Category.objects.all(),
    }

    if request.GET.get('category'):
        return redirect(f"/quiz/?category={request.GET.get('category')}")

    return render(request, 'home.html', context)


def quiz(request):
    context = {'category': request.GET.get('category')}
    return render(request, 'quiz.html', context)


def get_questions(request):
    try:
        questions = Question.objects.all()

        if request.GET.get('category'):
            questions = questions.filter(category__category_name__icontains=request.GET.get('category'))

        questions = list(questions)

        data = []
        random.shuffle(questions)

        for q in questions:
            data.append({
                'uid': q.uid,
                'category': q.category.category_name,
                'question': q.question,
                'marks': q.marks,
                'answers': q.get_answers()
            })

        context = {
            'status': True,
            'data': data,
        }

        return JsonResponse(context)

    except Exception as e:
        print(e)
        return HttpResponse("Error")