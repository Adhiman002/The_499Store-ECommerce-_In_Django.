from django.db import models
# Create your models here.
class Product(models.Model):
    Product_Name=models.CharField(max_length=50,default='')
    Catagory=models.CharField(max_length=50,default='')
    Subcatagory=models.CharField(max_length=50,default='')
    Price=models.IntegerField()
    Description=models.CharField(max_length=1050,default='')
    Publish_date=models.DateField()
    Product_img=models.ImageField(upload_to='shop/images' ,default='')

    def __str__(self):
        return self.Product_Name
    
class ContactUs(models.Model):
    First_name=models.CharField(max_length=15 ,default='')
    Last_name=models.CharField(max_length=15 ,default='')
    Email=models.EmailField(max_length=100 ,default='')
    Phone=models.CharField(max_length=12 ,default='')
    Msg=models.TextField(max_length=300 ,default='')

    def __str__(self):
        return self.First_name +' '+ self.Last_name

class PlaceOrder(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    Name=models.CharField(max_length=15 ,default='')
    Phone=models.CharField(max_length=15 ,default='')
    Email=models.EmailField(max_length=100 ,default='')
    Address=models.CharField(max_length=100 ,default='')
    City=models.CharField(max_length=12 ,default='')
    State=models.CharField(max_length=300 ,default='')
    ZipCode=models.CharField(max_length=300 ,default='')

    def __str__(self):
        return self.Name
class SlideData(models.Model):
    slide_id=models.AutoField(primary_key=True)
    shoe_name_first=models.CharField(max_length=30,default='')
    shoe_name_second=models.CharField(max_length=30,default='')
    shoe_name_third=models.CharField(max_length=30,default='')
    slide_image=models.ImageField(upload_to='shop/MainSlideImage', default='')
    shoe_company_name=models.CharField(max_length=50,default='')
    shoe_name=models.CharField(max_length=100,default='')
    details=models.CharField(max_length=200,default='')
    price=models.IntegerField(max_length=10,default='')

    def __str__(self):
        return self.shoe_name