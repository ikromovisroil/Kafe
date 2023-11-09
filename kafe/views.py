from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .forms import *
from users.models import *
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
        'category': Category.objects.filter(author=request.user),
        'user': User.objects.get(username=request.user)
    }
    return render(request, 'kafe/profil.html',context)


@login_required
def category(request):
    if request.method == 'POST':
        form = NewCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(request)
            category.author = request.user
            category.save()
            messages.success(request, "Maxsulot turi qo'shildi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = NewCategoryForm()
    context = {
        'form': form,
        'categor': Category.objects.filter(author=request.user)[::-1],
        'category': Category.objects.filter(author=request.user),
        'user': User.objects.get(username=request.user)
    }
    return render(request, 'kafe/category.html',context)


@login_required
def category_delete(request,pk):
    category = Category.objects.get(id=pk)
    if category.author == request.user:
        category.delete()
        messages.info(request, "Maxsulot turi o'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('login'))


@login_required
def product_new(request):
    if request.method == 'POST':
        form = NewProductForm(request.POST,request.FILES)
        if form.is_valid():
            product = form.save(request)
            product.author = request.user
            product.save()
            messages.success(request, "Maxsulot qo'shildi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(request, "Yaroqsiz malumot!")
    else:
        form = NewProductForm()
    context = {
        'form': form,
        'category': Category.objects.filter(author=request.user),
        'product': Product.objects.filter(author=request.user),
        'user': User.objects.get(username=request.user)
    }
    return render(request, 'kafe/product_new.html',context)


@login_required
def product(request,pk):
    category = Category.objects.get(id=pk)
    context = {
        'category': Category.objects.filter(author=request.user),
        'product': Product.objects.filter(category=category,author=request.user),
        'user': User.objects.get(username=request.user)
    }
    return render(request,'kafe/product.html',context)


@login_required
def product_delete(request,pk):
    product = Product.objects.get(id=pk)
    if product.author == request.user:
        product.delete()
        messages.info(request, "Maxsulot o'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('login'))


@login_required
def product_detail(request,pk):
    product = Product.objects.get(id=pk)
    if product.author == request.user:
        form = ProductForm(request.POST, files=request.FILES, instance=product)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, "Maxsulot Taxrilandi!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            form = ProductForm(instance=product)
    else:
        return redirect(reverse('login'))
    context = {
        'form': form,
        'category': Category.objects.filter(author=request.user),
        'user': User.objects.get(username=request.user)
    }
    return render(request, 'kafe/product_detail.html', context)


@login_required
def stol(request):
    if request.method == 'POST':
        form = NewStolForm(request.POST)
        if form.is_valid():
            stol = form.save(request)
            stol.author = request.user
            stol.save()
            messages.success(request, "Stol qo'shildi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = NewStolForm()
    context = {
        'form': form,
        'stol': Stol.objects.filter(author=request.user)[::-1],
        'category': Category.objects.filter(author=request.user),
        'user': User.objects.get(username=request.user)
    }
    return render(request, 'kafe/stol.html',context)


@login_required
def stol_delete(request,pk):
    stol = Stol.objects.get(id=pk)
    if stol.author == request.user:
        stol.delete()
        messages.info(request, "Stol o'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('login'))


def xodim_register(request):
    if request.method == 'POST':
        form = UserXodimform(request.POST)
        if form.is_valid():
            password = request.POST['password1']
            xodim = form.save(commit=False)
            xodim.author = request.user
            xodim.parol = password
            print(xodim)
            xodim.save()
            messages.info(request, "Xodim Qo'shildi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(request, "Muvaffaqiyatsiz ro'yxatdan o'tkazish. Yaroqsiz maʼlumot.")
    else:
        form = UserXodimform()
    context = {
        'form': form,
        'rol': Rol.objects.all(),
        'user': User.objects.filter(author=request.user,),
        'category': Category.objects.filter(author=request.user),
    }
    return render(request, 'kafe/xodim_register.html', context)


@login_required
def xodim_delete(request, pk):
    xodin = User.objects.get(id=pk)
    if xodin.author == request.user:
        xodin.delete()
        messages.info(request, "Xodim o'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('login'))


@login_required
def yordam(request):
    return render(request,'kafe/yordam.html')