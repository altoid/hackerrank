\W

use hackerrank;

select start_date, min(end_date)
from
(
select start_date, end_date
from
(
select start_date
from projects
where start_date not in (select end_date from projects)
) start_dates
join
(
select end_date
from projects
where end_date not in (select start_date from projects)
) end_dates
where end_date > start_date
) x
group by start_date
order by datediff(min(end_date), start_date) desc, start_date
;

