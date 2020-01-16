from django.shortcuts import render, redirect
from django.urls import reverse

from .words import kor, eng


def get_quiz(request):
    # localhost:8000/word?index=0&correct=0
    if request.method == 'GET':
        index = int(request.GET.get('index', 0))
        correct = int(request.GET.get('correct', 0))

        action = ""
        if index == 4:
            action += reverse('result')

        context = {
            "index": index,
            "quiz": eng[index],
            "action": action,
            "correct": correct
        }
        return render(request, 'word/index.html', context)

    if request.method == 'POST':
        index = int(request.POST.get('index'))
        before_correct = int(request.POST.get('correct'))
        answer = request.POST.get('answer')

        correct = before_correct

        if answer == kor[index]:
            correct += 1

        next_url = 'quiz' if int(index) < 4 else 'result'

        return redirect(
            reverse(next_url) +
            "?index={index}&correct={correct}".format(index=index+1, correct=correct)
        )


def get_result(request):
    if request.method == 'POST':
        correct = int(request.POST.get('correct'))
        index = int(request.POST.get('index'))
        answer = request.POST.get('answer')

        result = correct
        if answer == kor[index]:
            result += 1

        context = {
            "result": result
        }
    return render(request, 'word/result.html', context)
