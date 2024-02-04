from django.contrib import admin
from .models import Product,ContactUs,PlaceOrder,SlideData
# Register your models here.
admin.site.register(Product)
admin.site.register(ContactUs)
admin.site.register(PlaceOrder)
admin.site.register(SlideData)