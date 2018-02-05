from django.shortcuts import render, get_object_or_404, redirect
from .models import OrderDetail
from .forms import AddOrderForm
from cart.cart import Cart
from django.contrib.admin.views.decorators import staff_member_required
from .models import Order

def add_order(request):
    if request.user.is_authenticated():
        cart = Cart(request)
        if request.method == 'POST':
            form = AddOrderForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in cart:
                    OrderDetail.objects.create(order=order,
                                               product=item['product'],
                                               price=item['price'],
                                               quantity=item['quantity'])
                # clear the cart
                cart.clear()
                return render(request, 'orders/order/added.html', {'order': order})
        else:
            form = AddOrderForm()
        return render(request, 'orders/order/add.html', {'cart': cart, 'form': form})
    else:
        return redirect('store:login')


@staff_member_required #check both is_active and is_staff fields of the user made request to the page are True
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'admin/orders/order/detail.html', {'order': order})
