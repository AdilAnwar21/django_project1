from django.shortcuts import redirect, render
from django.contrib import messages
from .froms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
# urlpatterns = [
#     path('')
# ]


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f"Account Created for {username}!")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})



@login_required
def profile(request):
    return render(request,'users/profile.html')  #return a html page
