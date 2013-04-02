from django.shortcuts import render_to_response, get_object_or_404, redirect
from catalog.models import Category, Product
from django.template import RequestContext
from django.core import urlresolvers
from cart import cart
from forms import ProductAddToCartForm


def index(request, template_name="catalog/index.html"):
    title = "Index"
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def show_category(request, category_slug, template_name="catalog/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    title = c.name

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def show_product(request, product_slug, template_name="catalog/product.html"):
    p = get_object_or_404(Product, slug=product_slug)
    categories = p.categories.filter(is_active=True)
    title = p.name
    if request.method == "POST":
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        if form.is_valid():
            cart.add_to_cart(request)
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return redirect(url)
    else:
        form = ProductAddToCartForm(request=request, label_suffix=":")

    form.fields['product_slug'].widget.attrs['value'] = product_slug
    request.session.set_test_cookie()
    return render_to_response("catalog/product.html", locals(), context_instance=RequestContext(request))
