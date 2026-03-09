
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, UpdateUserForm, ChangePasswordForm, UserInfoForm
from django.contrib.auth.models import User
from .models import Profile



def update_info(request):
    if request.user.is_authenticated:
        current_user = Profile.objects.get(user__id=request.user.id)
        form = UserInfoForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
           
            messages.success(request, ("Your Info Has Been Updated!"))
            return redirect('home')
        return render(request, 'users/update_info.html', {'form':form})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')




def update_password(request):
    if request.user.is_authenticated:    
        current_user = request.user
        # Did they fill out the form
        if request.method == 'POST':
            form = ChangePasswordForm(current_user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, ("Your Password Has Been Updated!"))                 
                login(request, current_user)
                return redirect('update_user')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)


            # Do stuff with the form
        else:
                form = ChangePasswordForm(current_user)
                return render(request, 'users/update_password.html', {'form':form})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')        
             

    return render(request, 'users/update_password.html', {})



def update_user(request):
    if request.user.is_authenticated:
        current_user = User.objects.get(id=request.user.id)
        user_form = UpdateUserForm(request.POST or None, instance=current_user)
        if user_form.is_valid():
            user_form.save()
            login(request, current_user)
            messages.success(request, ("Your Account Has Been Updated!"))
            return redirect('home')
        return render(request, 'users/update_user.html', {'user_form':user_form})
    else:
        messages.success(request, ("You Must Be Logged In To View This Page..."))
        return redirect('home')
    


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, Please Try Again"))
            return redirect('login')

    else:
        return render(request, 'users/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logout...Thanks for stopping by..."))
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have registered Successfully!! Welecom!"))
            return redirect('home')
        else:
            messages.success(request, ("Whoops! There was a problem Registring, please try again "))
            return redirect('register')

    else:   
        return render(request, 'users/register.html', {'form':form}) 
