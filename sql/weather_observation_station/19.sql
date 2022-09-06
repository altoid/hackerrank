\W

use hackerrank;

select truncate(sqrt( (d - c) * (d - c) + (a - b) * (a - b)), 4) distance
from
(
		select max(lat_n) a, min(lat_n) b, max(long_w) c, min(long_w) d
        from station
) extremes
;
