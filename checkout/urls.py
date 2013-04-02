from django.conf.urls.defaults import *
from ecommerce import settings

urlpatterns = patterns('checkout.views',
(r'^$', 'show_checkout', {'template_name': 'checkout/checkout.html'}, 'checkout'),
(r'^receipt/$', 'receipt', {'template_name': 'checkout/receipt.html'},'checkout_receipt'),
)

