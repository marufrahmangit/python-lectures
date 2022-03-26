# from django.shortcuts import render
# from django.http import HttpResponse
from django.urls import reverse_lazy

# class_based view
from django.views.generic import (
    View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
)
from . import models

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School   # returns school_list automatically if context_object_name is not defined!

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    model = models.School
    fields = ('name','principal','location')

class SchoolUpdateView(UpdateView):
    model = models.School
    fields = ('name','principal')

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy('basic_app:school_list')





# class CBView(View):
#     def get(self,request):
#         return HttpResponse('CLASS BASED VIEWS ARE COOL!')


# function_based view
# def home(request):
#     return render(request,'home.html',{})


