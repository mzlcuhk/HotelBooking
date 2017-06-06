from django.shortcuts import render,loader
from booking import models
from django.http import HttpRequest, HttpResponse
from datetime import datetime
from datetime import timedelta
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

#from booking.forms import CustomersForm

# Create your views here.

def table(request):
     rt_ls = ['rt001','rt002','rt003','rt004','rt005','rt006','rt007','rt008','rt009','rt010','rt011','rt012','rt013','rt014','rt015','rt016']
     book_dic = {}
     book_ls = []
     booking_res = []
     if request.method == 'POST':
          for rt in rt_ls:
               if rt in request.POST:
                    book_dic[rt]=request.POST[rt]
                    book_ls.append(rt)
          booking_sum = models.Room_types.objects.raw('select * from booking_room_types where rt_id in %s',params=[book_ls])          
          
          if 'inday' in request.POST:
               inday = request.POST['inday']
               if inday is None or inday == '':
                    inday = '2013-01-01'
          else:
               inday = '2013-01-01'
          
          if 'outday' in request.POST:
               outday = request.POST['outday']
               if outday is None or outday == '':
                    outday = '2013-01-02'
          else:
               outday = '2013-01-02'
          
          if 'total' in request.POST:
               total = request.POST['total']
               if total is None or outday == '':
                    total = 0
          else:
               total = 0
          
   

          email1 = request.POST['email']    
          fname1 = request.POST['fname']
          lname1 = request.POST['lname']
          phone1 = request.POST['phone']
          cardn1 = request.POST['cardn']
          cardnm1 = request.POST['cardnm']
          eday =request.POST['eday']
          cvv =request.POST['cvv']
          #cls = models.Cust_info.objects.raw('insert into booking_cust_info values ()')
          cust = models.Cust_info(fname=fname1, lname=lname1, phone=phone1,email= email1)
          cust.save()
          date_format ="%Y-%m-%d"
          a = datetime.strptime(inday,date_format)
          b = datetime.strptime(outday,date_format)
          delta = b-a
          no_day =  delta.days
          book = models.Booking(b_name=fname1+' '+lname1, bsdate=inday, phone=phone1, email= email1, b_daysno=no_day)
          book.save()
          for rt in book_ls: 
               b_rms = models.Rooms.objects.raw(
                              '''select r_id from 
                                        (select r_id, rt_id_id
                                         from booking_rooms as avail
                                         left join
                                              (
                                                    select distinct(bh.r_id_id)
                                                    from booking_booking_has as bh
                                                         inner join
                                                       	(
                                                  			select e.id from
                                                  			  (SELECT id, DATE_ADD(bsdate,INTERVAL b_daysno DAY) AS Endday from booking_booking) as e
                                                  				 where e.Endday >= \'{0}\' and e.Endday <= \'{1}\'
                                                  				union
                                                  			  select s.id from booking_booking as s 
                                                  			  where s.bsdate >= \'{0}\' and s.bsdate <= \'{1}\'
                              			            ) as booked on booked.id = bh.b_id_id
                                            ) as brms on avail.r_id = brms.r_id_id where brms.r_id_id is null
                                        ) as roomls where rt_id_id = \'{2}\' order by r_id limit {3}'''.format(inday,outday,rt,book_dic[rt])) #order by r_id limit {3}
               for rm in b_rms:
                    book_has = models.Booking_has(
                              b_id=models.Booking.objects.get(id = book.id), 
                              r_id=models.Rooms.objects.get(r_id = rm.r_id), 
                              c_id=models.Cust_info.objects.get(id = cust.id))
                    book_has.save()
                    booking_res.append(rm)
     return render(request,'table.html',locals())

def search(request):
     totalbill = 0
     if request.method == 'POST':
          if 'bid' in request.POST:
               bid=request.POST['bid']   ##b_id_id, r_id, room_type, b_price, fname, lname, bsdate, b_daysno
          booking_sum = models.Booking_has.objects.filter(b_id_id = bid)
          booking_day = models.Booking.objects.filter(id = bid)
          cid = booking_sum[0].c_id_id
          fname = models.Cust_info.objects.filter(id = cid)[0].fname
          lname = models.Cust_info.objects.filter(id = cid)[0].lname
          df =  "%Y-%m-%d"
          inday = booking_day[0].bsdate
          days1 = int(booking_day[0].b_daysno)
          outday = inday + timedelta(days = days1)
          for rm in booking_sum:
               rts = models.Rooms.objects.filter(r_id = rm.r_id_id)
               prices = models.Room_types.objects.filter(rt_id = rts[0].rt_id_id)
               totalbill += int(prices[0].b_price) * days1
          #outday = outday.strftime(df)
     return render(request,'table1.html',locals())
    
def availability(request):
     if request.method == 'POST':
          #price = request.POST.get('price',0)
          if 'inday' in request.POST:
               inday = request.POST['inday']
               if inday is None or inday == '':
                    inday = '2013-01-01'
          else:
               inday = '2013-01-01'
          
          if 'outday' in request.POST:
               outday = request.POST['outday']
               if outday is None or outday == '':
                    outday = '2013-01-02'
          else:
               outday = '2013-01-02'
          
          
          if 'price_lower' in request.POST:
               price_lower = request.POST['price_lower'].replace(u'\xa0', u' ')
               if price_lower is None or price_lower == '':
                    price_lower = 5000 
          else:
               price_lower = 5000 
                    
          if 'price_upper' in request.POST:
               price_upper = request.POST['price_upper'].replace(u'\xa0', u' ')
               if price_upper is None or price_upper == '':
                    price_upper = 50000
          else:
               price_upper = 50000 
          
          if 'location' in request.POST:
               location = request.POST['location'].replace(u'\xa0', u' ')
               if 'ky' in location:
                    location = 'ST'
               elif 'sort' in location:
                    location = 'BR'
               elif 'stle' in location:
                    location = 'GC'
               elif location is None or location == '':
                    location = ''
          else:
               location = ''
          
          if 'adults' in request.POST:  
               adults = request.POST['adults'].replace(u'\xa0', u' ')
               if adults is None or adults == '':
                    adults = 1
          else:
               adults = 1
          

          if location == '':
               rt_list_d = models.Room_types.objects.raw(
                         '''select *, count(*) as ano from booking_room_types as rt   
                         	inner join
                         	(
                             select avail.rt_id_id
                         	from booking_rooms as avail
                             left join 
                         		(
                         		select distinct(bh.r_id_id)
                         			from booking_booking_has as bh
                         			inner join 
                         			(
                         			select e.id from 
                         			  (SELECT id, DATE_ADD(bsdate,INTERVAL b_daysno DAY) AS Endday from booking_booking) as e
                         				 where e.Endday >= \'{0}\' and e.Endday <= \'{1}\'
                         			
                         				union
                         			
                         			select s.id from booking_booking as s 
                         			  where s.bsdate >= \'{0}\' and s.bsdate <= \'{1}\'
                         			  ) as booked on booked.id = bh.b_id_id
                         		) as brms on avail.r_id = brms.r_id_id where brms.r_id_id is null  
                             ) as avail_rt on avail_rt.rt_id_id = rt.rt_id 
    where b_price>={2} and b_price<={3} and maxno>={4} group by rt.rt_id order by b_price'''.format(inday,outday,price_lower,price_upper,adults))
          else:
               rt_list_d = models.Room_types.objects.raw(
                        ''' select *, count(*) as ano from booking_room_types as rt   
                                   	inner join
                                   	(
                                       select avail.rt_id_id
                                   	from booking_rooms as avail
                                       left join 
                                   		(
                                   		select distinct(bh.r_id_id)
                                   			from booking_booking_has as bh
                                   			inner join 
                                   			(
                                   			select e.id from 
                                   			  (SELECT id, DATE_ADD(bsdate,INTERVAL b_daysno DAY) AS Endday from booking_booking) as e
                                   				 where e.Endday >= \'{0}\' and e.Endday <= \'{1}\'
                                   			
                                   				union
                                   			
                                   			select s.id from booking_booking as s 
                                   			  where s.bsdate >= \'{0}\' and s.bsdate <= \'{1}\'
                                   			  ) as booked on booked.id = bh.b_id_id
                                   		) as brms on avail.r_id = brms.r_id_id where brms.r_id_id is null  
                                       ) as avail_rt on avail_rt.rt_id_id = rt.rt_id 
                         where b_price>={2} and b_price<={3} and maxno>={4} and rt.bld= \'{5}\' group by rt.rt_id order by b_price '''.format(inday, 
                                        outday,price_lower,price_upper,adults,location))
     return render(request,'availability.html',locals())

def payment(request):
     rt_ls = ['rt001','rt002','rt003','rt004','rt005','rt006','rt007','rt008','rt009','rt010','rt011','rt012','rt013','rt014','rt015','rt016']
     date_format ="%Y-%m-%d"
     book_ls = {}
     booking = []
     total = 0
     if request.method == 'POST':
          
          if 'inday' in request.POST:
               inday = request.POST['inday']
               if inday is None or inday == '':
                    inday = '2013-01-01'
          else:
               inday = '2013-01-01'
          
          if 'outday' in request.POST:
               outday = request.POST['outday']
               if outday is None or outday == '':
                    outday = '2013-01-02'
          else:
               outday = '2013-01-02'
          
          for rt in rt_ls:
               if rt in request.POST:
                    book_ls[rt] = request.POST[rt].replace(u'\xa0', u' ')
                    if '0' in book_ls[rt]:
                         pass
                    elif '0' not in book_ls[rt]:
                         booking.append(rt)
          if not booking: 
               return render(request, 'index.html',locals())
          else:
               booking_sum = models.Room_types.objects.raw('select * from booking_room_types where rt_id in %s',params=[booking])
               
     a = datetime.strptime(inday,date_format)
     b = datetime.strptime(outday,date_format)
     delta = b-a
     no_day =  delta.days
     for rm in booking_sum:
          total +=  int(rm.b_price) * int(book_ls[rm.rt_id]) * delta.days
     return render(request, 'payment.html',locals())

def payment_s(request):
     if request.method == 'POST':
          email = request.POST['email']
          fname = request.POST['fname']
          lname = request.POST['lname']
          phone = request.POST['phone']
          cardn = request.POST['cardn']
          cardnm = request.POST['cardnm']
          eday =request.POST['eday']
          cvv =request.POST['cvv']
          test = models.Cust_info.objects.raw('select * from booking_cust_info')
     return render(request, 'payment_s.html',locals())

def contact(request):
    return render(request, 'contact.html',locals())

def hotel(request):
    return render(request, 'hotel.html',locals())

def index(request):
    return render(request, 'index.html',locals())

def price(request):
    return render(request, 'price.html',locals())

def projects(request):
    return render(request, 'projects.html',locals())

def services(request):
    return render(request, 'services.html',locals())

def sidebar_right(request):
    return render(request, 'sidebar_right.html',locals())

def index_jp(request):
    return render(request, 'index_jp.html',locals())
def index_fr(request):
    return render(request, 'index_fr.html',locals())
def index_cn(request):
    return render(request, 'index_cn.html',locals())
def index_ar(request):
    return render(request, 'index_ar.html',locals())