from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart
from django.core.mail import EmailMessage

# Create your views here.
def order_create(request):
    cart = Cart(request)
    form = OrderCreateForm()
    if request.method == 'POST':
        print("I'm here")
        form = OrderCreateForm(request.POST)
        email = request.POST.get('email','')
        print(email)
        if form.is_valid():
            order = form.save()
            data =  'Diamond Shop xin cảm ơn quý khách đã mua sản phẩm <br>'+\
                    'Xác nhận thông tin đơn hàng của quý khách như bên dưới'+\
                    '<table><tbody><tr><td valign="top"> <h2>Chi tiết đơn hàng</h2>' 
            for item in cart:
                data += '<ul> <li>'+ str(item['quantity']) + 'sản phẩm x '+\
                        item['product'].name + ' = <span>' + str(item['total_fee']) + '</span>'+\
                        '</li> </ul>'
            data += '<ul>Tổng: '+ str(cart.get_total_fee()) + ' vnđ</ul></td></tr></tbody></table>'
            data += '<br> chúng tôi sẽ liên hệ với quý khách trong thời gian gần nhất'
            for item in cart:
                OrderItem.objects.create(order = order,product = item['product'],price = item['fee'], quantity = item['quantity'])
                #clear the cart
                cart.clear()
                msg = EmailMessage('Diamond Shop - xác nhận đơn hàng',data,"PLC",[email],)
                msg.content_subtype = "html"
                msg.send()
                return render(request, 'orders/created.html', context = {'order' : order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html',context={'form':form})