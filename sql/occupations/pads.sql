use hackerrank;

select concat(name, '(', substring(name, 1, 1), ')') t
from occupations
order by name
;

select concat('There are a total of ', count(*), ' ', lower(occupation), 's.') t
from occupations
group by occupation
order by count(*), occupation
;
