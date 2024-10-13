from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from kafe.models import *
from .models import *
from users.models import *
from django.db.models import Sum
from .forms import *
from django.http import JsonResponse
from django.template.loader import render_to_string

@login_required
def tables(request):
    tables = Table.objects.filter(author=request.user.author)
    
    for table in tables:
        table.order_count = table.order_set.filter(author__author=request.user.author, deliver=False).count()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Prepare JSON response for AJAX
        table_data = [{
            'id': table.id,
            'name': table.name,
            'order_count': table.order_count,
        } for table in tables]
        return JsonResponse({'tables': table_data})
    
    context = {
        'table': tables,
    }
    return render(request, 'xodim/tables.html', context)


@login_required
def order(request, table_pk, category_pk=None):
    table = get_object_or_404(Table, id=table_pk)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.author = request.user
            order.table = table
            order.summa_all = order.product.summa * order.number
            order.save()
            messages.info(request, "Buyurtma muvaffaqiyatli qo'shildi!")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
        else:
            messages.error(request, "Yaroqsiz maʼlumot!")
    else:
        form = OrderForm()
    products = Product.objects.filter(author=request.user.author, status=True)
    if category_pk:
        products = products.filter(category=category_pk)
    context = {
        'form': form,
        'table': table,
        'product': products,
        'category': Category.objects.filter(author=request.user.author),
    }
    return render(request, 'xodim/order.html', context)


@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, id=pk)
    if order.author.author == request.user.author:
        order.delete()
        messages.info(request, "O'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))


@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, id=pk)
    if request.method == 'POST' and order.author.author == request.user.author:
        order.number = int(request.POST.get('number'))
        order.summa_all = order.product.summa * order.number
        order.save()
        messages.info(request, "Buyurtma muvaffaqiyatli yangilandi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return redirect('login')

    
@login_required
def orders(request,pk):
    table = get_object_or_404(Table, id=pk)
    context = {
        'table': table,
        'order': Order.objects.filter(author__author=request.user.author,table=table,deliver=False)
    }
    return render(request, 'xodim/orders.html',context)


@login_required
def cook(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':  # AJAX so'rovini tekshirish
        orders = Order.objects.filter(author__author=request.user.author, deliver=False).order_by('-status')
        html = render_to_string('xodim/order_list.html', {'order': orders})
        return JsonResponse({'html': html})
    context = {
        'order': Order.objects.filter(author__author=request.user.author, deliver=False).order_by('-status')
    }
    return render(request, 'xodim/cook.html', context)


@login_required
def order_status(request, pk):
    order = get_object_or_404(Order, id=pk)
    if order.author.author == request.user.author:
        if order.status:
            order.status = False
        else:
            order.status = True
        order.save()
        messages.info(request, "Saqlandi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))


@login_required
def report(request, pk):
    table = get_object_or_404(Table, id=pk)
    order_list = Order.objects.filter(author__author=request.user.author, table=table, deliver=False)
    jami_sum = order_list.aggregate(total_sum=Sum('summa_all'))
    jami_sum_value = jami_sum['total_sum'] if jami_sum['total_sum'] is not None else 0  # Agar jami yo'q bo'lsa, 0
    context = {
        'table': table,
        'order': order_list,
        'jami_sum': jami_sum_value
    }
    return render(request, 'xodim/report.html', context)


@login_required
def report_delete(request, pk):
    table = get_object_or_404(Table, id=pk)
    if table.author == request.user.author:
        order_list = Order.objects.filter(author__author=request.user.author, table=table, deliver=False)
        for order in order_list:
            order.deliver = True  # Buyurtma yetkazib berilgan deb belgilanyapti
            order.save()  # Har bir buyurtmani alohida saqlash kerak
        messages.info(request, "O'chirildi!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/fallback-url/'))
    else:
        return redirect(reverse('login'))