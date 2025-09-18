select * from sakila.actor;

select * from sakila.actor where NOT last_name = 'MARY';
select * from sakila.actor where NOT actor_id > 20;
select * from sakila.actor where NOT actor_id <= 25;

select * from sakila.actor where first_name regexp '[AB]';
select * from sakila.actor where last_name regexp '[ABE]';
select * from sakila.actor where actor_id regexp '[1]';
select * from sakila.actor where actor_id regexp '[10]';

select * from sakila.actor order by actor_id asc ;
select * from sakila.actor order by actor_id desc ;
select * from sakila.actor  order by first_name  asc, actor_id asc;
select * from sakila.actor where first_name = 'NICK'  order by first_name  asc, actor_id desc; 

select * from sakila.actor limit 10;
select * from sakila.actor order by first_name asc limit 25;
select * from sakila.actor order by first_name desc limit 25;
select * from sakila.actor order by actor_id asc limit 11, 10;
select * from sakila.actor order by actor_id desc limit 11, 10;