select t.*
from
(
select min(city) w, length(city) l from station group by length(city)
) t
inner join (
select min(length(city)) l from station
union
select max(length(city)) l from station
) m
on t.l = m.l
;


