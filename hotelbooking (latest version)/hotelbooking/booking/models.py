from __future__ import unicode_literals
from django.db import models
#from django import forms
#from django.utils.translation import ugettext_lazy as _
#from datetime import datetime
# Create your models here.

class Room_types(models.Model):
    # rt_id,room_type, maxno, b_price, area, bed_no
    rt_id = models.CharField(max_length=10, primary_key=True) # verbose_name="rt_id" # 
    room_type = models.CharField( max_length=50)  #"rt_id",
    maxno = models.CharField(max_length=10) #
    b_price = models.CharField(max_length=10)
    area = models.CharField(max_length=10)
    bed_no = models.CharField(max_length=10)
    quantity = models.CharField(max_length=10)
    boat = models.CharField(max_length=10)
    parking = models.CharField(max_length=10)
    library = models.CharField(max_length=10)
    cinema = models.CharField(max_length=10)
    plift = models.CharField(max_length=10)
    #models.BooleanField(max_length=1, choices=((0, 'FALSE'),(1, 'TRUE'),))
    image = models.CharField( max_length=100)
    bld = models.CharField(max_length=10)


class Booking(models.Model):
     #b_id = models.CharField(max_length=20) # , primary_key=True
     b_name = models.CharField( max_length=50)
     email = models.EmailField()
     phone = models.CharField(max_length=50)
     bsdate = models.DateField()
     # optional method
     #  birthday = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y')), input_formats=('%m/%d/%Y',))
     b_daysno = models.IntegerField()

#==============================================================================
class Rooms(models.Model):
      r_id = models.CharField(max_length=10, primary_key=True) # 
      rt_id = models.ForeignKey('Room_types',on_delete=models.CASCADE) ##
      floor = models.CharField(max_length=10)
      #maxno = models.CharField(max_length=10)
      #b_price = models.CharField(max_length=10)
      
#==============================================================================

class Cust_info(models.Model):
     #c_id =models.CharField(max_length=20) # ,primary_key=True
     fname = models.CharField(max_length=50, default='')
     lname = models.CharField(max_length=50,default='')
     add= models.CharField(max_length=500,default='')
     email =models.CharField(max_length=100)
     country =models.CharField(max_length=100,default='')
     gender = models.CharField(max_length=10)
     title =models.CharField(max_length=50,default='')
     phone =models.CharField(max_length=100)
     


#==============================================================================
class Booking_has(models.Model):
     b_id= models.ForeignKey('Booking',on_delete=models.CASCADE)
     r_id= models.ForeignKey('Rooms',on_delete=models.CASCADE)
     c_id= models.ForeignKey('Cust_info',on_delete=models.CASCADE)
     class Meta:         
          unique_together=(('b_id','r_id','c_id'),)
#==============================================================================
     
     
          
