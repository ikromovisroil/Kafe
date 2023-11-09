from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponseRedirect
from kafe.models import *
from django.urls import reverse
from django.contrib import messages
from .form import *
from kafe.models import *
from users.models import *
# Create your views here.

@login_required
def stollar(request):
    context = {
        'stol': Stol.objects.filter(author=request.user.author)
    }
    return render(request, 'afitsan/stollar.html',context)


@login_required
def buyurtma(request,pk):
    stol = Stol.objects.get(id=pk)
    if request.method == 'POST':
        form = NewZakasForm(request.POST)
        if form.is_valid():
            zakas = form.save(request)
            zakas.author = request.user.author
            zakas.stol = stol
            if zakas.soni > 0:
                zakas.save()
                messages.success(request, "Buyurtma olindi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = NewZakasForm()
    context = {
        'stol': stol,
        'form': form,
        'product': Product.objects.filter(author=request.user.author),
        'category': Category.objects.filter(author=request.user.author),
    }
    return render(request, 'afitsan/buyurtma.html', context)


@login_required
def buyurtmalar(request,pk):
    stol = Stol.objects.get(id=pk)
    context = {
        'stol': stol,
        'zakas': Zakas.objects.filter(author=request.user.author,stol=stol),
        'category': Category.objects.filter(author=request.user.author),
    }
    return render(request, 'afitsan/buyurtmalar.html',context)


@login_required
def buyurtmalar_delete(request,pk):
    zakas = Zakas.objects.get(id=pk)
    if zakas.author == request.user.author:
        zakas.delete()
        messages.info(request, "buyurtma bekor qilindi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('login'))
