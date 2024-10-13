from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from users.models import *
from .forms import *
# Create your views here.

@login_required
def profil(request):
    if request.method == 'POST':
        form = Userprofilform(request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = Userprofilform(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'kafe/profil.html',context)


@login_required
def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(request)
            category.author = request.user
            category.save()
            messages.info(request, "Maxsulot turi qo'shildi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
        else:
            messages.success(request, "Yaroqsiz maʼlumot!")
    else:
        form = CategoryForm()
    context = {
        'form': form,
        'category': Category.objects.filter(author=request.user)
    }
    return render(request, 'kafe/category.html',context)


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, id=pk)
    if category.author == request.user:
        category.delete()
        messages.info(request, "O'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))


@login_required
def product(request,pk=None):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            messages.info(request, "Maxsulot qo'shildi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
        else:
            messages.info(request, "Yaroqsiz maʼlumot!")
    else:
        form = ProductForm()
    context = {
        'form': form,
        'category': Category.objects.filter(author=request.user),
        'product': Product.objects.filter(author=request.user)
    }
    if pk:
        context['product'] = context['product'].filter(category=pk)
        
    return render(request, 'kafe/product.html', context)


@login_required
def product_status(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product.author == request.user:
        if product.status:
            product.status = False
        else:
            product.status = True
        product.save()
        messages.info(request, "Saqlandi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, id=pk)
    if product.author == request.user:
        product.delete()
        messages.info(request, "O'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))
    
    
@login_required
def employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            user = form.save(request)
            user.author = request.user
            user.save()
            messages.info(request, "Xodim qo'shildi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
        else:
            messages.success(request, "Yaroqsiz maʼlumot!")
    else:
        form = EmployeeForm()
    context = {
        'form': form,
        'rol': Rol.objects.all(),
        'employees': User.objects.filter(author=request.user),
    }
    return render(request, 'kafe/employee.html',context)


@login_required
def employee_delete(request, pk):
    user = get_object_or_404(User, id=pk)
    if user.author == request.user:
        user.delete()
        messages.info(request, "O'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))
    
    
@login_required
def table(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            table = form.save(request)
            table.author = request.user
            table.save()
            messages.info(request, "Stol,Kabina qo'shildi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
        else:
            messages.success(request, "Yaroqsiz maʼlumot!")
    else:
        form = TableForm()
    context = {
        'form': form,
        'table': Table.objects.filter(author=request.user)
    }
    return render(request, 'kafe/table.html',context)


@login_required
def table_delete(request, pk):
    table = get_object_or_404(Table, id=pk)
    if table.author == request.user:
        table.delete()
        messages.info(request, "O'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))
   
    
@login_required
def contact(request):
    if request.method == 'POST':
        form = Usercomment(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.author = request.user
            contact.save()
            messages.info(request, "Xabar yuborildi")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request, "Yaroqsiz maʼlumot.")
    else:
        form = Usercomment()
    context = {
        'form': form,
    }
    return render(request, 'kafe/contact.html', context)