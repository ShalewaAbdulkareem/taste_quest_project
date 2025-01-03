from fruits_app.models import Product
from django.conf import settings
from decimal import Decimal

class Cart():
    """
    A base Cart Class, providing some default behaviors that
    can be inherited or overridden, as necessary.
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if settings.CART_SESSION_ID not in request.session:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def add(self, product, qty):
        """
         and update the user's cart session data.
        """
        product_id = product.id
        if product_id not in self.cart:
        # Add product to cart
            self.cart[product_id] = {'price': str(product.price), 'qty': int(qty)}
        else:
        # Update quantity if product exists
            self.cart[product_id]['qty'] += qty

        self.save()


    # def add(self, product, qty):
    #     """
    #     Add and update the user's cart session data.
    #     """
    #     product_id = str(product.id)
    #     if product_id not in self.cart:
    #         self.cart[product_id]['qty'] = qty
    #     else:
    #         self.cart[product_id] = {'price': str(product.price), 'qty': qty}

        
    #     self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database and return products
        """
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    def __len__(self):
        """
        Get the cart data and count the qty items
        """
        return sum(item['qty'] for item in self.cart.values())






    def get_total_price(self):
        """
        Calculate total price including shipping.
        """
        subtotal = sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
        delivery_fee = Decimal(45.00) if subtotal > 0 else Decimal(0.00)  # Match with HTML
        total = subtotal + delivery_fee
        return total


    # def get_total_price(self):
    #     suntotal = sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())
    #     if subtotal == 0:
    #         shipping = Decimal(0.00)
    #     else:
    #         shipping = Decimal(0.00)

    #         total = subtotal + Decimal(shipping)

    #         return total


    def get_subtotal_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    
    def delete(self, product):
        """
        Delete items from session data
        """
        product_id = str(product)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def update(self, product, qty):
        """
        Update values in session data
        """
        product_id = str(product)
        if product_id in self.cart:
            self.cart[product_id]['qty'] = qty
            self.save()


    def clear(self):
        # Remove cart from session data
        del self.session[settings.CART_SESSION_ID]
        self.save()


    def save(self):
        """
        Mark the session as modified to ensure it saves changes.
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True
