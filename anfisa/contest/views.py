from django.shortcuts import render

from .forms import ContestForm


def proposal(request):
    context = {'form': ContestForm()}
    if request.GET:
        form = ContestForm(request.GET)
        if form.is_valid():
            context['form'] = form

    return render(request, 'contest/form.html', context)