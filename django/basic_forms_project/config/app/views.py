from django.shortcuts import render
from . import forms

# Create your views here.
def home(request):
    return render(request,'app/home.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do something
            print('VALIDATION SUCCESS')
            print('Name: ' + form.cleaned_data['name'])
            print('Email: ' + form.cleaned_data['email'])
            print('Text: ' + form.cleaned_data['text'])

    return render(request,'app/form_page.html',{'form':form})