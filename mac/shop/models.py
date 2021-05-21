from django.db import models

# Create your models here.
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=300)
    price=models.IntegerField(default=0)
    category=models.CharField(max_length=50,default='')
    subcategory=models.CharField(max_length=50,default='')
    image=models.ImageField(upload_to='shop/images',default='')

    pub_date=models.DateField()
    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    phone=models.IntegerField(default=0)
    email=models.CharField(max_length=50)
    message=models.CharField(max_length=500)


    def __str__(self):
        return self.email
