select * from sakila.actor;
select * from sakila.address;
select * from sakila.category;
select * from sakila.city;
select * from sakila.country;

select actor_id from sakila.actor;
select address from sakila.address;
select inventory_id from sakila.inventory;
select rental_id, rental_date from sakila.rental;
select store_id, address_id from sakila.store;

select * from sakila.actor where actor_id = 1;
select * from sakila.actor where first_name = 'ED';

select first_name from sakila.actor where first_name = 'ED';

select * from sakila.city where city_id = 1;
select * from sakila.city where city_id > 10;
select * from sakila.city where city_id < 23;

select * from sakila.city where country_id >= 2;
select * from sakila.city where country_id = 2;
select * from sakila.city where country_id <= 2;

select * from sakila.country where country = 'Algeria' and country_id = 2;
select * from sakila.country where country = 'Algeria' and country_id = 10;

select * from sakila.country where country = 'Algeria' or country_id = 2;
select * from sakila.country where country = 'Algeria' or country_id = 10;

select * from sakila.actor where actor_id != 10;

select * from sakila.actor where first_name like '%b';
select * from sakila.actor where first_name like '%a';

select * from sakila.actor where first_name like 'a%';

select * from sakila.actor where first_name like '%an%';

select * from sakila.actor where last_name like '_h%';

select distinct first_name from sakila.actor;
