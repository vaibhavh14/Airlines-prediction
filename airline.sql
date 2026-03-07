SELECT * FROM flights.flight;

select distinct(source_city)from flight
union
select distinct(destination_city)from flight;


SELECT * 
FROM flight
WHERE source_city = 'Bangalore'
AND destination_city = 'Delhi';

select airline, count(*) from flight
group by airline;

select source_city, count(*) from (select source_city from flight
                              union all
							select destination_city from flight)t
group by t.source_city
order by count(*) desc;

select date_