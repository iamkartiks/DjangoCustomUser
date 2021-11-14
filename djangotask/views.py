from django.shortcuts import render
from users.forms import CustomUserCreationForm
# Create your views here.
def logIn(request):
    return render(request,'djangotask/login.html')

def signUp(request):
    
    form = CustomUserCreationForm()

    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    return render(request,'djangotask/register.html',context)

def userDetails(request):
    pass