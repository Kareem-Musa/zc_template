from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StateForm, LocalityForm, UnityForm
from .models import State, Locality, Unity

def state_list(request):
    states = State.objects.all()
    context = {
        'states':states
    }
    return render(request, 'locations/state_list.html', context)

def add_state(request):
    if request.method == "POST":
        form = StateForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم اضافة ولاية بنجاح')
            return redirect('locations:states')
        else:
            messages.error(request, 'الرجاء تصحيح الأخطاء')
    else:
        form = StateForm()
    return render(request, 'locations/add_state.html', {'form':form})

def locality_list(request):
    localities = Locality.objects.all()
    context = {
        'localities':localities
    }
    return render(request, 'locations/locality_list.html', context)

def add_locality(request):
    if request.method == "POST":
        form = LocalityForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم أضافة محلية جديدة')
            return redirect('locations:locality_list')
        else:
            messages.error(request, 'الرجاء تصحيح بيانات المحلية')
    else:
        form = LocalityForm()
    return render(request, 'locations/add_locality.html', {'form':form})

def unity_list(request):
    unity_list = Unity.objects.all()
    context = {
        'unity_list':unity_list
    }
    return render(request, 'locations/unity_list.html', context)

def add_unity(request):
    if request.method == 'POST':
        form = UnityForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم أضافة وحدة أدارية بنجاح')
            return redirect('locations:unity_list')
        else:
            messages.error(request, 'الرجاء تصحيح بيانات الوحدة الأدارية')
            # return redirect(request, 'locations:add_unity')
    else:
        form = UnityForm()
    return render(request, 'locations/add_unity.html', {'form':form})
