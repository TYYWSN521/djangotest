from django.db import models

# Create your models here.
class guapai(models.Model):
    id=models.IntegerField(max_length=10,primary_key=True)
    total_price=models.TextField(null=True)
    house_type=models.TextField(null=True)
    area=models.TextField(null=True)
    unit_price=models.TextField(null=True)
    direction=models.TextField(null=True)
    floor=models.TextField(null=True)
    decoration=models.TextField(null=True)
    address_area=models.TextField(null=True)
    address_name=models.TextField(null=True)
    adress_subway=models.TextField(null=True)
    complete_year=models.TextField(null=True)
    category=models.TextField(null=True)
    getdate=models.TextField(null=True)
    getaddress=models.TextField(null=True)

class lianjiainf(models.Model):
    area=models.TextField(null=True)
    address=models.TextField(null=True)
    name=models.TextField(null=True)
    price=models.TextField(null=True)
    unit_price=models.TextField(null=True)
    acreage=models.TextField(null=True)
    room_type=models.TextField(null=True)
    all_floor=models.TextField(null=True)
    floor=models.TextField(null=True)
    shore=models.TextField(null=True)
    house_type=models.TextField(null=True)
    fitment=models.TextField(null=True)
    time=models.TextField(null=True)
    id=models.IntegerField(max_length=11,primary_key=True)
