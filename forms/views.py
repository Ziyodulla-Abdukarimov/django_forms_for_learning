from django.shortcuts import render
from .forms import BlogForm, PersonFormSet


# Create your views here.
def home_view(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        form.save()
    context = {'form': BlogForm}
    return render(request, 'home.html', context)


def edit_people(request):
    if request.method == 'POST':
        formset = PersonFormSet(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = PersonFormSet()

    return render(request, 'formset.html', {'formset': formset})
