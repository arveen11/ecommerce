from django import forms
from django.template import RequestContext
from forms import RegistrationForm
#from registration.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from catalog.models import Product
from checkout.models import Order, OrderItem


@login_required
def my_account(request, template_name="registration/my_account.html"):
    """ page displaying customer account information, past order list and account options """
    page_title = 'My Account'
    orders = Order.objects.filter(user=request.user)
    name = request.user.username
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def order_details(request, order_id, template_name="registration/order_details.html"):
    """ displays the details of a past customer order; order details can only be loaded by the same 
    user to whom the order instance belongs.
    
    """
    order = get_object_or_404(Order, id=order_id, user=request.user)
    page_title = 'Order Details for Order #' + order_id
    order_items = OrderItem.objects.filter(order=order)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))

@login_required
def order_info(request, template_name="registration/order_info.html"):
    """ page containing a form that allows a customer to edit their billing and shipping information that
    will be displayed in the order form next time they are logged in and go to check out """
    if request.method == 'POST':
        postdata = request.POST.copy()
        form = UserProfileForm(postdata)
        if form.is_valid():
            profile.set(request)
            url = urlresolvers.reverse('my_account')
            return HttpResponseRedirect(url)
    else:
        user_profile = profile.retrieve(request)
        form = UserProfileForm(instance=user_profile)
    page_title = 'Edit Order Information'
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))        


def home(request):
    p = Product.objects.all()
    return render_to_response('home.html', {'title': 'Home', 'p': p}, context_instance=RequestContext(request))

def about(request):
    p = Product.objects.all()
    return render_to_response('about.html', {'title': 'About Us', 'p': p}, context_instance=RequestContext(request))    


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def register(request):
    title = "Registration"
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = RegistrationForm()
    return render_to_response("registration/registration_form.html", locals())

    """
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save();
            new_user = authenticate(username=request.POST['username'], password=request.POST['password1'])
            login(request, new_user)
            return HttpResponseRedirect('/accounts/profile')
    else:
        form = RegistrationForm()

    return render_to_response('registration/registration.html', {'form' : form}, context_instance=RequestContext(request))


    """
