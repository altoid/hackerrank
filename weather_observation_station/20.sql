\W

use hackerrank;

select truncate(sum(median) / count(*), 4) median
from
(
select truncate(lat_n, 4) median
from 
( select @rowid := 0 ) init
join
( select @rowid := @rowid + 1 as rowid,
  lat_n
  from station order by lat_n
) x
join ( select count(*) c from station ) cnt
where abs((c - rowid + 1) - rowid) <= 1
) y
;

/*
if the count is even, then we have take the mean of the sum of 2 values.
in this case the mininum difference in row ids is 1.

if the count is odd, then we just have one value.  we can still take the mean of the sum of 1 value.
in this case the minimum difference in row ids is 0.
*/
