from django.contrib import admin
from django.urls import path
from mystore import views
from django.conf.urls import url

app_name = "mystore"

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^product_detail/(\d+)/$', views.product_detail, name='product_detail'),
]