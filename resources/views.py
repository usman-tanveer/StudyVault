from django.shortcuts import render


def home(request):
    return render(request, 'resources/home.html')


def subjects(request):
    return render(request, 'resources/subjects.html')


def data_science(request):
    return render(request, 'resources/data_science.html')


def quantitative_reasoning(request):
    return render(request, 'resources/quantitative_reasoning.html')


def ict(request):
    return render(request, 'resources/ict.html')


def fundamental_mathematics(request):
    return render(request, 'resources/fundamental_mathematics.html')


def functional_english(request):
    return render(request, 'resources/functional_english.html')


def global_challenges(request):
    return render(request, 'resources/global_challenges.html')