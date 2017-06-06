design of booking app:

For project

     __init__ changes:
          import pymysql
          #import cx_Oracle
          pymysql.install_as_MySQLdb()

     urls.py changes:
          url(r'^', include('booking.urls'))  # booking is your app_name
     
     setting.py changes:
          add below items to INSTALLED_APPS:
               'booking' -- app name
          DATABASES = 
               'ENGINE': 'django.db.backends.mysql',
               'NAME': 'hotel_booking_db',
               'USER':'root',  #'root'
               'PASSWORD':'1234', #'1234'
          
For APP
     Add templates Dir:
          for each html:
               add tag  {% load staticfiles %} below <head>
               tag all pic/js/css with "{% static 'some/dir/file' %}" or '{% static 'some/dir/file' %}'

     creat usrl.py and urls contain:
         url(r'^availibility/$', views.availibility),
         url(r'^contact/$', views.contact),
         url(r'^hotel/$', views.hotel),
         url(r'^index/$', views.index),
         url(r'^price/$', views.price),
         url(r'^projects/$', views.projects),
         url(r'^services/$', views.services),
         url(r'^sidebar_right/$', views.sidebar_right),

     models contains：
     
     hotel_booking_db
          #booking
               b_id(PK),bname,email,phone,bsdate,b_daysno

          #cust_info
               c_id(PK),fname,lname,add,email,country,gender,title,phone,gender

          #rooms
               r_id(PK),rt_id(FK),floor

          #room_type
               rt_id(PK),room_type,maxno,b_price,area,bed_no,quantity,boat,parking,library,cinema,plift,image

          #booking_has
               b_id(PK),r_id(FK),c_id(FK)

               
               
               

     views contain:
          availability

For MySql
     Installation: https://jerrynest.io/windows-mysql-installer/
     Import data: https://dev.mysql.com/doc/workbench/en/wb-admin-export-import-table.html
     