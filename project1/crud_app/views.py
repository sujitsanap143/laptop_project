from django.shortcuts import render, redirect

from django.shortcuts import HttpResponse

from .forms import LaptopForm
from .models import Laptops

from django.contrib.auth.decorators import login_required


@login_required(login_url='signin_url')
def laptop_create_view(request):
    form = LaptopForm()
    if request.method == 'POST':
        form = LaptopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('show_url')

    template_name = 'crud_app/laptop_form.html'
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='signin_url')
def laptop_retrive_view(request):
    objs = Laptops.objects.all()
    template_name = 'crud_app/laptop_list.html'
    context = {'data': objs}
    return render(request, template_name, context)


def laptop_update_view(request, pk):
    obj = Laptops.objects.get(id=pk)
    form = LaptopForm(instance=obj)

    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')

    template_name = 'crud_app/laptop_form.html'
    context = {'form': form}
    return render(request, template_name, context)


def laptop_delete_view(request, pk):
    obj = Laptops.objects.get(id=pk)
    if request.method == 'POST':
        obj.delete()
        return redirect('show_url')
    # obj.delete()
    template_name = 'crud_app/laptop_delete_confirmation.html'
    context = {'obj':obj}
    return render(request, template_name, context)