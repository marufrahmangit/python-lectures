from django.shortcuts import render

# Create your views here.
def home(request):
    context_dict = {'text':'hello world','number':100}  # template filter example, check home.html
    return render(request,'app/home.html',context_dict)

def other(request):
    return render(request,'app/other.html',{})

def relative_url(request):
    return render(request,'app/relative_url_templates.html',{})
