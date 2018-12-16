from django.shortcuts import render
from mystore.models import Product, M_Khach_hang
from cart.forms import CardAddProductForm
from mystore import forms
from django.shortcuts import redirect
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    username=''
    if request.session.has_key('username'):
        username = request.session['username']
    pro_list = Product.objects.all()
    paginator = Paginator(pro_list, 4)
    page_number = request.GET.get("page")

    try:
        contacts = paginator.page(page_number)
    except PageNotAnInteger:
        # Nếu page_number không thuộc kiểu integer, trả về page đầu tiên
        contacts = paginator.page(1)
    except EmptyPage:
        # Nếu page không có item nào, trả về page cuối cùng
        contacts = paginator.page(paginator.num_pages)
    print(contacts)

    return render(request, "mystore/index.html", {"products":contacts,'username':username})

def product_detail(request, id=None):
    product = Product.objects.get(pk=id)
    cart_product_form = CardAddProductForm()
    return render(request, 'mystore/product_detail.html', context= {'product': product, 'cart_product_form': cart_product_form})

def dang_nhap(request):
    err = ''
    hasher = PBKDF2PasswordHasher()
    if request.method=="POST":
        _ten = request.POST.get('ten_dang_nhap')
        _mat_khau = hasher.encode(request.POST.get('mat_khau'),'123')
        kh = M_Khach_hang.objects.filter(ten_dang_nhap=_ten, mat_khau=_mat_khau)
        if kh.count()>0:
            request.session['username'] = kh[0].ho_ten
            err = 'Da luu khach hang vao session'
            return redirect('mystore:index')
        else:
            err = 'Dang nhap không thành công'
    return render(request, 'mystore/dang_nhap.html', {'err':err})

def dang_xuat(request):
    if request.session.has_key("username"):
        del request.session['username']
    return redirect('mystore:index')

def dang_ky(request):
    registered = False
    if request.method == "POST":
        form_user = forms.FormDangKy(request.POST, M_Khach_hang)
        #####################################################
        hasher = PBKDF2PasswordHasher()
        # Them validation cho form
        if form_user.is_valid() and form_user.cleaned_data['mat_khau'] == form_user.cleaned_data['confirm']:
            request.POST._mutable = True
            post = form_user.save(commit=False)
            post.ho_ten = form_user.cleaned_data['ho_ten']
            post.ten_dang_nhap = form_user.cleaned_data['ten_dang_nhap']
            ###########################################################
            post.mat_khau = hasher.encode(form_user.cleaned_data['mat_khau'],'123')
            post.email = form_user.cleaned_data['email']
            post.phone = form_user.cleaned_data['phone']
            post.dia_chi = form_user.cleaned_data['dia_chi']
            post.save()
            print('Da ghi user vao CSDL')
            registered = True
        elif form_user.cleaned_data['mat_khau'] != form_user.cleaned_data['confirm']:
            form_user.add_err('confirm','The password not match')
            print('Password and password confirm not match')
    else:
        form_user = forms.FormDangKy()

    return render(request, "mystore/registration.html", {'user_form':form_user, 'registered': registered})


def contact(request):
    registered = False
    if request.method == "POST":
        form_contact = forms.FormContact(data = request.POST)
        if form_contact.is_valid():
            register = form_contact.save()
            register.save()
            registered = True
        else:
            print(form_contact.errors)
    else:
        form_contact = forms.FormContact()
    return render(request, "mystore/contact.html",{'contact_form':form_contact,'registered': registered})