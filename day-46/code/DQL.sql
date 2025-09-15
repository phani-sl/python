select * from sakila.actor;
select * from sakila.address;
select * from sakila.city;
select * from sakila.film;
select * from sakila.language;

select actor_id, last_name from sakila.actor;
select address_id, district from sakila.address;
select rental_id from sakila.rental;
select store_id from sakila.store;

select * from sakila.actor where  actor_id = 1;
select * from sakila.store where store_id = 2;
select * from sakila.city where country_id > 30;

select * from sakila.actor where actor_id = 1 and last_name ='gUINESS';
select * from sakila.city where city = Adana and country_id = 97;

select first_name, last_name from SAKILA.actor where actor_id = 1 OR last_name ='mostel';
select language_id from sakila.language where last_update = 2006-02-15 OR name = 'German';

