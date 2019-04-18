\W

use hackerrank_15_days;

select 
s1.submission_date, s1.hacker_id,
s2.submission_date, s2.hacker_id
from
submissions s1
inner join submissions s2
on s1.hacker_id = s2.hacker_id
and s1.submission_date <= s2.submission_date
order by s2.submission_date, s1.submission_date
;

select 
s2.submission_date, s2.hacker_id, count(*) c
from
submissions s1
inner join submissions s2
on s1.hacker_id = s2.hacker_id
and s1.submission_date <= s2.submission_date
group by s2.submission_date, s2.hacker_id
order by s2.submission_date
;

select submission_date, day_of_contest, hacker_id, c
from
(select @prev := null, @day_of_contest := 1) init
join
(
select 
@prev,
@day_of_contest,
@day_of_contest := if(submission_date != @prev, @day_of_contest + 1, @day_of_contest) day_of_contest,
@prev := submission_date,
submission_date, hacker_id, c
from
(

    select 
    s2.submission_date, s2.hacker_id, count(*) c
    from
    submissions s1
    inner join submissions s2
    on s1.hacker_id = s2.hacker_id
    and s1.submission_date <= s2.submission_date
    group by s2.submission_date, s2.hacker_id
    order by s2.submission_date
    ) y

) x
;

/*
select day_of_contest, sdate, hid, c
from
( select @prev := '', @days := 0) init
join
(
select
@days := if(s2.submission_date != @prev, 1, @days + 1) as day_of_contest,
@prev = s2.submission_date,
s2.submission_date sdate,
s1.hacker_id hid,
count(*) c

from submissions s1
inner join submissions s2
on s1.hacker_id = s2.hacker_id
and s1.submission_date <= s2.submission_date
group by s2.submission_date,
s1.hacker_id
order by s2.submission_date
) x
;
*/