\W

use hackerrank_15_days;

select 
s1.submission_date, s1.hacker_id,
s2.submission_date, s2.hacker_id
from
( select distinct submission_date, hacker_id from submissions ) s1
inner join
( select distinct submission_date, hacker_id from submissions ) s2
on s1.hacker_id = s2.hacker_id
and s1.submission_date >= s2.submission_date
order by s1.submission_date, s2.submission_date
;


select submission_date, day_of_contest
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
    s1.submission_date, s1.hacker_id, count(*) c
    from
    ( select distinct submission_date, hacker_id from submissions ) s1
    inner join
    ( select distinct submission_date, hacker_id from submissions ) s2
    on s1.hacker_id = s2.hacker_id
    and s1.submission_date >= s2.submission_date
    group by s1.submission_date, s1.hacker_id
) y
) x
where day_of_contest = c
;

select submission_date, count(*)
from
(
    select submission_date, day_of_contest
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
        s1.submission_date, s1.hacker_id, count(*) c
        from
        ( select distinct submission_date, hacker_id from submissions ) s1
        inner join
        ( select distinct submission_date, hacker_id from submissions ) s2
        on s1.hacker_id = s2.hacker_id
        and s1.submission_date >= s2.submission_date
        group by s1.submission_date, s1.hacker_id
    ) y
    ) x
    where day_of_contest = c
) z
group by submission_date
;
