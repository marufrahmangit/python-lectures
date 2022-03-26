from django.shortcuts import render
# from .models import User
from .forms import UserForm


# Create your views here.
def home(request):
    return render(request,'user_app/home.html')


def users(request):
    form = UserForm()

    if request.method == 'POST':

        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return home(request)
        else:
            print('ERROR FORM INVALID')
    return render(request,'user_app/users.html',{'form':form})



    # USER LIST
    # user_list = User.objects.order_by('id')
    # user_dict = {'users':user_list}
    # return render(request,'user_app/users.html',context=user_dict)