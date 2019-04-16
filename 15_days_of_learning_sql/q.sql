\W

use hackerrank_15_days;

/*
want the count of the number of hackers who have submitted each day since the beginning.

*/


select
b.submission_date,
b.k,
a.hacker_id,
a.name
from
(
    select
    min_hacker_id_by_count_per_day.submission_date,
    hackers.hacker_id,
    hackers.name
    from
    (
    
        select submission_date, max(c) most_submissions
        from
        (
        select submission_date, count(*) c
        from submissions
        group by submission_date, hacker_id
        ) counts_per_hacker_per_day
        group by submission_date
    
    ) max_counts_per_day
    inner join
    (
        select submission_date, c, min(hacker_id) min_hacker_id
        from
        (
        select submission_date, count(*) c, hacker_id
        from submissions
        group by submission_date, hacker_id
        ) counts_per_hacker_per_day
        group by submission_date, c
    
    ) min_hacker_id_by_count_per_day
    
    on
    max_counts_per_day.submission_date = min_hacker_id_by_count_per_day.submission_date
    and
    max_counts_per_day.most_submissions = min_hacker_id_by_count_per_day.c
    
    inner join hackers
    on hackers.hacker_id = min_hacker_id_by_count_per_day.min_hacker_id
) a
inner join
(
    select submission_date, count(*) k
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
) b
on a.submission_date = b.submission_date
;
