from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecord

# Create your views here.
def home(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list}
    return render(request,'AppTwo/home.html',context=date_dict)











# def home(request):
#     # return HttpResponse("<em>My Second App</em>")
#     my_dictionary = {'template_tag': 'Now I am coming from AppTwo/home.html.py'}
#     return render(request,'AppTwo/home.html',context=my_dictionary)

# def help(request):
#     my_dict = {'help_var': 'Help Page'}
#     return render(request,'AppTwo/help.html',context=my_dict)
