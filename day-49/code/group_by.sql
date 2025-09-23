select * from world.city;
select * from world.country;
select * from world.countrylanguage;

select Continent, count(*) as TotalCountries from Country group by Continent;

select Continent, avg(Population) as AvgPopulation from Country group by Continent;
select Continent, sum(Population) as SumPopulation from Country group by Continent;
select Continent, min(Population) as MinPopulation from Country group by Continent;
select Continent, max(Population) as MaxPopulation from Country group by Continent;

select Continent, count(*) as TotalCountries from Country group by Continent having COUNT(*) > 20;
select Region, avg(LifeExpectancy) as AvgLife from Country group by Region order by AvgLife desc limit 1;
select Region, avg(LifeExpectancy) as AvgLife from Country group by Region order by AvgLife asc limit 1;
select Region, count(*) as BigCountries from Country where Population > 50000000 group by Region;

select CountryCode, count(*) as TotalCities from City group by CountryCode;
select CountryCode, count(*) as CityCount from City group by CountryCode order by CityCount desc limit 5;
select CountryCode, count(*) as CityCount from City group by CountryCode order by CityCount asc limit 5;
select CountryCode, avg(Population) as AvgCityPop from City group by CountryCode;
select CountryCode, min(Population) as MinCityPop from City group by CountryCode;
select CountryCode, max(Population) as MaxCityPop from City group by CountryCode;
select CountryCode, sum(Population) as SumCityPop from City group by CountryCode;

select CountryCode, name, Population from City where Population > 5000000;