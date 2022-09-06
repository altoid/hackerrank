\W

use hackerrank;

select x, y
from
(
select
f1.x , f1.y
from functions f1
inner join functions f2
on
f1.x = f2.y and f1.y = f2.x
where f1.x < f1.y
union
select
x, y
from functions
where x = y
group by x
having count(*) > 1
) a
order by x, y
;

/*
for a pair with equal values to be symmetric
there has to be two pairs with that value.

this is symmetric

(20, 20)
(20, 20)

this is not:

(21, 21)

this is too

(21, 21)
(21, 21)
(21, 21)

*/