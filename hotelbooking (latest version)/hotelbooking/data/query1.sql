select * from booking_booking;
select * from booking_rooms;
select distinct(rt_id_id) from booking_rooms;
insert into booking_booking values ('a','b','aa@123.com','123','2017-12-13','5');
insert into booking_booking values ('a1','b1','aa@123.com','123','2017/12/13','5');
insert into booking_booking values ('a2','b1','aa@123.com','123','12/21/2013','5');
select * from booking_room_types;
select * from booking_cust_info where fname = 'qqqq';
delete from booking_cust_info where fname = 'qqqq';
select rt_id_id, floor from booking_rooms group by rt_id_id ;
select * from booking_booking_has;
delete from booking_booking_has;
select b_id,b_daysno from booking_booking where bsdate >= '2018-04-7';
update booking_room_types set bld ='ST' where rt_id like'rt%';
update booking_room_types set bld ='BR' where rt_id in ('rt008','rt009','rt010','rt011','rt012');
update booking_room_types set bld ='GC' where rt_id in ('rt013','rt014','rt015','rt016');

select * from booking_room_types where rt_id in ('rt001','rt002');



select distinct(bh.r_id_id)
	from booking_booking_has as bh
	inner join 
	(
    select e.id from 
	  (SELECT id, DATE_ADD(bsdate,INTERVAL b_daysno DAY) AS Endday from booking_booking) as e
	     where e.Endday >= '2017-07-15' and e.Endday <= '2017-08-17'
	
        union
	
    select s.id from booking_booking as s 
	  where s.bsdate >= '2017-07-15' and s.bsdate <= '2017-08-17'
      ) as booked on booked.id = bh.b_id_id ;

select distinct(avail.rt_id_id) 
	from booking_rooms as avail
    left join 
		(
		select distinct(bh.r_id_id)
			from booking_booking_has as bh
			inner join 
			(
			select e.b_id from 
			  (SELECT b_id, DATE_ADD(bsdate,INTERVAL b_daysno DAY) AS Endday from booking_booking) as e
				 where e.Endday >= '2017-07-15' and e.Endday <= '2017-09-17'
			
				union
			
			select s.b_id from booking_booking as s 
			  where s.bsdate >= '2017-07-15' and s.bsdate <= '2017-09-17'
			  ) as booked on booked.b_id = bh.b_id
		) as brms on avail.r_id = brms.r_id_id where brms.r_id_id is null ;



-- final version
select *, count(*) as avail_temp from booking_room_types as rt   
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
				 where e.Endday >= '2017-07-15' and e.Endday <= '2017-09-17'
			
				union
			
			select s.id from booking_booking as s 
			  where s.bsdate >= '2017-07-15' and s.bsdate <= '2017-09-17'
			  ) as booked on booked.id = bh.b_id_id
		) as brms on avail.r_id = brms.r_id_id where brms.r_id_id is null  
    ) as avail_rt on avail_rt.rt_id_id = rt.rt_id 
    where b_price>=8000 and b_price<=20000 and maxno>=4 and bld='ST' group by rt.rt_id order by b_price; /**/
 
 
 
 -- with group
select distinct(avail.rt_id_id), count(*) as avail_no
	from booking_rooms as avail
    left join 
		(
		select distinct(bh.r_id_id)
			from booking_booking_has as bh
			inner join 
			(
			select e.id from 
			  (SELECT id, DATE_ADD(bsdate,INTERVAL b_daysno DAY) AS Endday from booking_booking) as e
				 where e.Endday >= '2017-07-15' and e.Endday <= '2017-09-17'
			
				union
			
			select s.id from booking_booking as s 
			  where s.bsdate >= '2017-07-15' and s.bsdate <= '2017-09-17'
			  ) as booked on booked.id = bh.b_id_id
		) as brms on avail.r_id = brms.r_id_id where brms.r_id_id is null group by avail.rt_id_id;


-- without group
select *
	from booking_rooms as avail
    left join 
		(
		select distinct(bh.r_id_id)
			from booking_booking_has as bh
			inner join 
			(
			select e.id from 
			  (SELECT id, DATE_ADD(bsdate,INTERVAL b_daysno DAY) AS Endday from booking_booking) as e
				 where e.Endday >= '2017-07-15' and e.Endday <= '2017-09-17'
			
				union
			
			select s.id from booking_booking as s 
			  where s.bsdate >= '2017-07-15' and s.bsdate <= '2017-09-17'
			  ) as booked on booked.id = bh.b_id_id
		) as brms on avail.r_id = brms.r_id_id where brms.r_id_id is null;
        
        
select r_id from  
	(
    select r_id, rt_id_id
	from booking_rooms as avail
    left join 
		(
		select distinct(bh.r_id_id)
			from booking_booking_has as bh
			inner join 
			(
			select e.id from 
			  (SELECT id, DATE_ADD(bsdate,INTERVAL b_daysno DAY) AS Endday from booking_booking) as e
				 where e.Endday >= '2017-07-15' and e.Endday <= '2017-09-17'
			
				union
			
			select s.id from booking_booking as s 
			  where s.bsdate >= '2017-07-15' and s.bsdate <= '2017-09-17'
			  ) as booked on booked.id = bh.b_id_id
		) as brms on avail.r_id = brms.r_id_id where brms.r_id_id is null  
    ) as avail_rt  where rt_id_id='rt001' order by r_id limit 3;