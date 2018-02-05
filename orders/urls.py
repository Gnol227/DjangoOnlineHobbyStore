from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^add/$', views.add_order, name='add_order'),

    url (r'^admin/order/(?P<order_id>\d+)/$', views.admin_order_detail, name='admin_order_detail'),
]
