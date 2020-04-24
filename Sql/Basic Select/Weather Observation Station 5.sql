select city, length(city) as length from station order by length asc,city asc limit 1;
select city, length(city) as length from station order by length desc, city asc limit 1;