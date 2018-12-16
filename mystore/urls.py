from django.contrib import admin
from django.urls import path
from mystore import views
from django.conf.urls import url

app_name = "mystore"

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^product_detail/(\d+)/$', views.product_detail, name='product_detail'),
    url(r'^dang_nhap/$', views.dang_nhap, name="dang_nhap"),
    url(r'^dang_xuat/$', views.dang_xuat, name="dang_xuat"),
    url(r'^dang_ky/$', views.dang_ky, name="dang_ky"),
    url(r'^contact/$', views.contact, name="contact"),
]