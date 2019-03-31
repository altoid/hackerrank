\W

use hackerrank;

-- count is odd

select truncate(lat_n, 4) median
from 
( select @rowid := 0 ) init
join
( select @rowid := @rowid + 1 as rowid,
  lat_n
  from station order by lat_n
) x
join ( select count(*) c from station ) cnt
where c - rowid + 1 = rowid
;
-- count is even

select truncate(sum(lat_n) / 2, 4) median
from 
( select @rowid := 0 ) init
join
( select @rowid := @rowid + 1 as rowid,
  lat_n
  from station order by lat_n
) x
join ( select count(*) c from station ) cnt
where abs((c - rowid + 1) - rowid) = 1

;


