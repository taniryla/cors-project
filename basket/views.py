from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from store.models import Product
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Basket


@login_required(login_url="/accounts/login")
def basket_summary(request):
    basket = Basket(request)
    return render(request, 'store/basket/summary.html', {'basket': basket})


def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)

        basketqty = basket.__len__()
        response = JsonResponse({'qty': basketqty})
        return response
