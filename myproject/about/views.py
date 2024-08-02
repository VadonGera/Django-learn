from django.shortcuts import render

context = 'user@main'


def about(request):
    """About view"""
    return render(
        request,
        'about/about.html',
        context={'user': context},
    )
