\W

use hackerrank_challenges;

select hacker_id, count(*) c
from challenges
group by hacker_id
order by count(*), hacker_id
;


select c, count(*) cc
from
(
    select count(*) c
    from challenges
    group by hacker_id
    order by count(*), hacker_id
)x
group by c
;

select max(c) maxcount
from
(
    select hacker_id, count(*) c
    from challenges
    group by hacker_id
    order by count(*), hacker_id
) y
;

select
*
from
(
    select c, count(*) cc
    from
    (
        select count(*) c
        from challenges
        group by hacker_id
--        order by count(*), hacker_id
    )x
    group by c
) a
inner join
(
    select max(c) maxcount
    from
    (
        select hacker_id, count(*) c
        from challenges
        group by hacker_id
--        order by count(*), hacker_id
    ) y
) b
where  cc < 2 or c = maxcount
;

/*
select
*
from
(
    select hacker_id, count(*) c
    from challenges ch
    group by ch.hacker_id
) a
inner join
(
    select c, count(*) cc
    from
    (
    select count(*) c
    from challenges
    group by hacker_id
    order by count(*), hacker_id
    )x
    group by c
) b
on a.c = b.c
;
*/