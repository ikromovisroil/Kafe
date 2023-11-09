from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from kafe.models import *
from afitsan.models import *
# Create your views here.

@login_required
def kabina(request):
    context = {
        'stol': Stol.objects.filter(author=request.user.author)
    }
    return render(request, 'kassa/kabina.html',context)


@login_required
def shot(request,pk):
    stol = Stol.objects.get(id=pk)
    zakas = Zakas.objects.filter(author=request.user.author, stol=stol),
    jami_sum = 0
    for i in zakas:
        for x in i:
            jami_sum += x.sum()
    context = {
        'stol': stol,
        'jami_sum': jami_sum,
        'zakas': Zakas.objects.filter(author=request.user.author,stol=stol),
    }
    return render(request, 'kassa/shot.html',context)


@login_required
def tozalash(request,pk):
    stol = Stol.objects.get(id=pk)
    if stol.author == request.user.author:
        zakas = Zakas.objects.filter(author=request.user.author, stol=stol),
        for i in zakas:
            i.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('login'))


