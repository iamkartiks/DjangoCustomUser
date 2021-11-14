from django.db.models.manager import Manager
from django.shortcuts import redirect, render
from users.forms import AddressEditForm, CustomUserChangeForm, CustomUserCreationForm, EmailEditForm, UsernameEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.models import *


def logIn(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request,email=email, password=password)

        if user is not None:
            login(request,user)
            return redirect('userdetails/%d'%request.user.id)
    return render(request,'djangotask/login.html')

def signUp(request):
    
    form = CustomUserCreationForm()

    if request.method=='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'form':form}
    return render(request,'djangotask/register.html',context)


@login_required(login_url='login')
def userDetails(request,pk):
    user = CustomUser.objects.get(id=pk)
    context = {'user':user}
    return render(request, 'djangotask/userdetails.html',context)


@login_required(login_url='login')
def addressSettings(request):
	user = request.user
	form = AddressEditForm(instance=user)

	if request.method == 'POST':
		form = AddressEditForm(request.POST,instance=user)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'djangotask/edit_field.html', context)

@login_required(login_url='login')
def emailSettings(request):
	user = request.user
	form = EmailEditForm(instance=user)

	if request.method == 'POST':
		form = EmailEditForm(request.POST,instance=user)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'djangotask/edit_field.html', context)

@login_required(login_url='login')
def usernameSettings(request):
	user = request.user
	form = UsernameEditForm(instance=user)

	if request.method == 'POST':
		form = UsernameEditForm(request.POST,instance=user)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'djangotask/edit_field.html', context)

@login_required(login_url='login')
def deleteEmail(request,pk):
    user = CustomUser.objects.get(id=pk)
    if request.method=='POST':
        user.email = None
        return redirect('/userdetails/%d'%request.user.id)
    return render(request,'djangotask/delete_field.html')


@login_required(login_url='login')
def deleteAddress(request,pk):
    user = CustomUser.objects.get(id=pk)
    if request.method=='POST':
        user.address = None
        return redirect('/userdetails/%d'%request.user.id)
    return render(request,'djangotask/delete_field.html')


@login_required(login_url='login')
def deleteUsername(request,pk):
    user = CustomUser.objects.get(id=pk)
    if request.method=='POST':
        user.username = None
        user.save()
        return redirect('/userdetails/%d'%request.user.id)
    return render(request,'djangotask/delete_field.html')


@login_required(login_url='login')
def deleteUser(request,pk):
    user = CustomUser.objects.get(id=pk)
    u = CustomUser.objects.filter(email=user)
    if request.method=='POST':
        u.delete()
        return redirect('/')
    return render(request,'djangotask/deleteuser.html')


def logOut(request):
    logout(request)
    return redirect('login')