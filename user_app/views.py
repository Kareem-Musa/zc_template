from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout as do_logout
from django.contrib import messages
from .forms import UserLoginForm, RegisterForm

def dashboard(request):
    return render(request, 'user_app/dashboard.html')

def user_login(request):
    # if request.method == "POST":
    #     form = UserLoginForm(data=request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(username=username, password=password)
    #         if user is not None:
    #             login(request, user)
    #             return redirect('user_app:dashboard')
    #         else:
    #             return redirect('user_app:login')
    # else:
    #     form = UserLoginForm()
    # return render(request, 'user_app/login.html', {'form':form})
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'تم الدخول بنجاح')
                return redirect('user_app:dashboard')
            else :
                messages.error(request, "خطأ اسم المستخدم / كلمة المرور")
                return redirect('user_app:login')
    else:
        form = UserLoginForm()
    return render(request, 'user_app/login.html', {'form':form})

def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم التسجيل بنجاح')
            return redirect('user_app:login')
        else:
            messages.error('الرجاء تصحيح الحقول')
            return redirect('user_app:register')
    else:
        form = RegisterForm()
    return render(request, 'user_app/register.html', {'form':form})

def logout(request):
    do_logout(request)
    return redirect('user_app:login')
