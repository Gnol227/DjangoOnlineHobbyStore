from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views #trung vs views

urlpatterns = [
    url (r'^$', views.product_view, name='product_view'),

    url (r'^register/$', views.register, name="register"),

    url (r'^login/$', auth_views.login, {'template_name': 'store/login.html'}, name='login'),

    url (r'^logout/$', auth_views.logout, {'next_page':'/'}, name='logout'),

    url (r'^(?P<category_slug>[-\w]+)/$', views.product_view, name='product_view_by_category'),

    url (r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]
