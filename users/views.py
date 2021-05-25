from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm, CouncilForm, UpdateCouncilForm
from .models import Council

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        c_form = CouncilForm(request.POST)
        if form.is_valid() and c_form.is_valid():
            user = form.save()
            c_form = c_form.save(commit=False)
            c_form.user = user
            c_form.save()
            #username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegistrationForm()
        c_form = CouncilForm()
    return render(request, 'users/register.html', {'form':form, 'c_form':c_form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES, 
                                    instance=request.user.profile)
        c_form = CouncilForm(request.POST)
        if u_form.is_valid() and p_form.is_valid() and c_form.is_valid():
            user = u_form.save()
            u_form.save()
            p_form.save()
            c_form = c_form.save(commit=False)
            c_form.user = user
            c_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)  
        c_form = CouncilForm()      
    context = {
        'u_form': u_form,
        'p_form' : p_form,
        'c_form' : c_form,
        'councils': Council.objects.all()
    }
    return render(request, 'users/profile.html', context)