from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=264,unique=True)
    fee = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to = "images/")
    
    def __str__(self):
        return str(self.name)

class M_Khach_hang(models.Model):
    ho_ten = models.CharField(max_length=264,blank=False)
    ten_dang_nhap = models.CharField(max_length=50,blank=False)
    mat_khau = models.CharField(max_length=100,blank=False)
    phone = models.CharField(max_length=264,blank=False)
    email = models.EmailField(max_length=264,blank=False)
    dia_chi = models.TextField(max_length=264,blank=False)

    def __str__(self):
        return str(self.ho_ten)

    class Meta:
        db_table=u'Khachhang'

class Contact(models.Model):
    ho_ten = models.CharField(max_length = 264, blank = False)
    phone = models.CharField(max_length = 20)
    email = models.EmailField(blank = False)
    noi_dung = models.TextField()

    def __str__(self):
        return self.ho_ten
        
    class Meta:
        db_table=u'Contact'