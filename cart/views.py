
# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from fruits_app.models import Product
from .cart import Cart


def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart.html', {'basket': cart})  # Pass as 'basket'

# def cart_summary(request):
#     cart = Cart(request) 
#     return render(request, 'cart.html', {'cart': cart})






def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))

        # Fetch the product and add it to the cart
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, qty=product_qty)

        # Return updated cart quantity as JSON response
        cart_qty = cart.__len__()
        return JsonResponse({'qty': cart_qty})

# def cart_add(request):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         product_qty = int(request.POST.get('productqty'))
#         product = get_object_or_404(Product, id = product_id)
#         cart.add(product=product, qty=product_qty)

#         cartqty = cart.__len__()
#         response = JsonResponse({'qty': cartqty})
#         return response

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        cart.delete(product=product_id)

        cartqty = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})
        return response




def cart_update(self, product_id, qty):
    """
    Update values in session data.
    """
    product_id = str(product_id)
    if product_id in self.cart:
        self.cart[product_id]['qty'] = qty
        self.save()

# def cart_update(request):
#     cart = Cart(request)
#     if request.POST.get('action') == 'post':
#         product_id = int(request.POST.get('productid'))
#         product_qty = int(request.POST.get('productqty'))
#         cart.update(product=product_id, qty=product_qty)

#         cartqty = cart.__len__()
#         carttotal = cart.get_total_price()
#         response = JsonResponse({'qty': cartqty, 'subtotal': carttotal})  # Removed `self`
#         return response
