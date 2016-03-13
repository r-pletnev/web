from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Answer, Question

def test(req, *args, **kwargs):
    return HttpResponse("OK")

def question(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'question.html', {'question' : question})

def question_index(request):
    question_list = Question.objects.all()
    paginator = Paginator(question_list, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'questions': questions})

def popular_questions(request):
    question_list = Question.objects.order_by('-rating')
    paginator = Paginator(question_list, 10)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'questions': questions})





