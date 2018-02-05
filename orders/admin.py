from django.contrib import admin
from .models import Order, OrderDetail
from django.core.urlresolvers import reverse

def order_detail(obj):
    return '<a href="{}">View</a>'.format(
        reverse('orders:admin_order_detail', args=[obj.id]))
order_detail.allow_tags = True

class OrderDetailInLine(admin.TabularInline):
    model = OrderDetail
    raw_id_fields = ['product']
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'address', 'city', 'paid', 'created', 'updated', order_detail]
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderDetailInLine]

admin.site.register(Order, OrderAdmin)
