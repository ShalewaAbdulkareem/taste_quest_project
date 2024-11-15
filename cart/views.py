from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from fruits_app.models import Product
from .cart import Cart

def cart_summary(request):
    cart = Cart(request) #Assuming Cart is a class that manages cart functionality

    #Get the cart items, their quantity, and total price
    cart_items = cart.get_items() # Replace with appropriate methods to get cart items
    total_price = cart.get_total_price() # Replace with appropriate method to calculate total 

    context = {
        'cart': cart_items,
        total_price: total_price
    }
    return render(request,'cart.html', context) 

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id = product_id)
        cart.add(product=product, qty=product_qty)

        cartqty = cart.__len__()
        response = JsonResponse({'qty': cartqty})
         
        return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        cart.update(product=product_id, qty=product_qty)

        cartqty =cart.__len__()
        carttotal = cart.get_total_price()
        response = self.JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response