from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from afitsan.models import *
# Create your views here.

@login_required
def zakas(request):
    context = {
        'soni': Zakas.objects.filter(author=request.user.author,buyurtma=False),
        'zakas': Zakas.objects.filter(author=request.user.author)[::-1]
    }
    return render(request, 'oshpaz/zakas.html',context)


def tayor(request,pk):
    zakas = Zakas.objects.get(id=pk)
    if zakas.author == request.user.author:
        if zakas.buyurtma == False :
            zakas.buyurtma = True
        else:
            zakas.buyurtma = False
        zakas.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(reverse('login'))