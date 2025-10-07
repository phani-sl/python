select count(*) as total_countries from country;
select sum(Population) as total_population from country;
select avg(LifeExpectancy) as avg_life from country;
select min(LifeExpectancy) as min_life from country;
select max(GNP) as max_gnp from country;
select Continent, count(*) as country_count from country group by Continent;
select Continent, avg(Population) as avg_population
from country
group by Continent
having avg_population > 50000000;
select upper(Name) as country_upper from country;
select lower(Name) as country_lower from country;
select Name, length(Name) as name_length from country limit 10;
select concat(Name, ' - ', Continent) as country_info from country limit 10;
select Name, substring(Name, 1, 4) as first_four from country limit 10;
select round(LifeExpectancy, 1) as rounded_life from country limit 10;
select ceil(GNP / 1000) as ceil_gnp from country limit 10;
select Name, mod(Population, 2) as remainder from country limit 10;
select power(2, 3) as power_example;
select now() as current_datetime;
select curdate() as current_date;
select curtime() as current_time;
select year(now()) as current_year;
select month(now()) as current_month;
select day(now()) as current_day;
select format(GNP, 2) as formatted_gnp from country limit 10;
select version() as mysql_version;

select Continent, sum(Population) as total_population from country group by Continent;
select Region, avg(GNP) as avg_gnp from country group by Region;
select Continent, max(LifeExpectancy) as max_life from country group by Continent;
select CountryCode, count(Language) as total_languages
from countrylanguage
group by CountryCode;
select CountryCode, sum(Population) as total_city_population
from city
group by CountryCode;

