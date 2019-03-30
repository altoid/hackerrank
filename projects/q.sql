\W

use hackerrank;

select *
from
(
select 
start_dates.d sd, min(end_dates.d) ed,
datediff(min(end_dates.d), start_dates.d) ddiff
from
(
select start_date d from projects
where start_date not in (select end_date from projects)
) start_dates
inner join
(
select end_date d from projects
where end_date not in (select start_date from projects)
)
end_dates
on end_dates.d > start_dates.d
group by start_dates.d
) ans
order by ddiff, sd
;
