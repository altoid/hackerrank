\W

use hackerrank;

select truncate(abs(c - a) + abs(d - b), 4) as manhattan
from
(
select min(lat_n) a, min(long_w) b, max(lat_n) c, max(long_w) d
from station
) extremes
;
