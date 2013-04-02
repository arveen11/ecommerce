from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.defaults import *
from ecommerce import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    url(r'^checkout/', include('checkout.urls')),

    #url(r'^$', include('catalog.urls')),
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^ecommerce/', include('ecommerce.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)


urlpatterns += patterns('accounts.views',
        (r'^register/$', 'register'),
        (r'^$', 'home'),
        (r'^about/$', 'about'),
        (r'^logout/$', 'logout'),
        (r'^accounts/profile/$', 'my_account',
        {'template_name': 'registration/my_account.html'}, 'my_account'),


)
"""urlpatterns += patterns('accounts.views',
        (r'^register/$', 'register',
        {'template_name': 'registration/registration.html'},
        'register'),

        (r'^my_account/$', 'my_account',
        {'template_name': 'registration/my_account.html'}, 'my_account'),

        (r'^order_details/(?P<order_id>[-\w]+)/$', 'order_details',
        {'template_name': 'registration/order_details.html'}, 'order_details'),

        (r'^order_info//$', 'order_info',
        {'template_name': 'registration/order_info.html'}, 'order_info'),
)
    """


urlpatterns += patterns('',
        (r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'registration/login.html'}, 'login'),

        (r'^password_change/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'registration/password_change.html'}, 'password_change'),

)

urlpatterns += patterns('contact.views',
                       url(r'^contact$', 'contact'),
)

urlpatterns += patterns('catalog.views',
    #(r'^$', 'index', { 'template_name':'catalog/index.html'}, 'catalog_home'),
    (r'^category/(?P<category_slug>[-\w]+)/$','show_category', {'template_name':'catalog/category.html'},'catalog_category'),
    (r'^product/(?P<product_slug>[-\w]+)/$','show_product', {'template_name':'catalog/product.html'},'catalog_product'),
)

urlpatterns += patterns('cart.views',
    (r'^cart$', 'show_cart', { 'template_name': 'cart/cart.html' }, 'show_cart'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
