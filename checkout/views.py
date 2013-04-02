from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.http import HttpResponseRedirect
from forms import CheckoutForm
from models import Order, OrderItem
import checkout
from cart import cart
from django.contrib.auth.decorators import login_required

@login_required
def show_checkout(request, template_name='checkout/checkout.html'):
    """if cart.is_empty(request):
        cart_url = urlresolvers.reverse('show_cart')
    return HttpResponseRedirect(cart_url)"""

    if request.method == 'POST':
        postdata = request.POST.copy()
        form = CheckoutForm(postdata)
        if form.is_valid():
            response = checkout.process(request)
            order_number = response.get('order_number',0)
            error_message = response.get('message','')
            if order_number:
                request.session['order_number'] = order_number
                receipt_url = urlresolvers.reverse('checkout_receipt')
                return HttpResponseRedirect(receipt_url)
        else:
            error_message = u'Correct the errors below'
    else:
        form = CheckoutForm()
    page_title = 'Checkout'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

def receipt(request, template_name='checkout/receipt.html'):
    order_number = request.session.get('order_number','')
    if order_number:
        order = Order.objects.filter(id=order_number)[0]
        order_items = OrderItem.objects.filter(order=order)
        del request.session['order_number']
    else:
        cart_url = urlresolvers.reverse('show_cart')
        return HttpResponseRedirect(cart_url)
    return render_to_response(template_name,locals(), context_instance=RequestContext(request))



        
    




