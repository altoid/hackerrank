\W

use hackerrank;

/*
select distinct
a.submission_date da, '#', b.submission_date db
from submissions a, submissions b
where a.submission_date <= b.submission_date
;

select *
from hackers h
inner join submissions s on h.hacker_id = s.hacker_id
order by name, submission_date
;
*/

/*
-- how many days are there between the start date and a given date?
select *
from
(
    select db submission_date, count(*) day_of_contest
    from
    (
        select distinct
        a.submission_date da, '#', b.submission_date db
        from submissions a, submissions b
        where a.submission_date <= b.submission_date
    ) t
    group by db
) days_since_beginning
;

select *
from
(
    select db, hb, count(*) days_submitted 
    -- number of days since beginning of contest that hacker has submitted something
    from
    (
        select distinct
        a.submission_date da, a.hacker_id ha, '#', b.submission_date db, b.hacker_id hb
        from submissions a, submissions b
        where a.submission_date <= b.submission_date
        and a.hacker_id = b.hacker_id
        order by db, hb
    ) t
    group by db, hb
) days_submitted_counts
;
*/

select submission_date, count(*)
from
(
    select
    days_since_beginning.submission_date,
    days_submitted_counts.hacker_id,
    days_submitted_counts.days_submitted
    from
    (
        -- for each date in the contest, count the number of days from the
    	-- beginning of the contest to that date (inclusive)
        select db submission_date, count(*) day_of_contest
        from
        (
            select distinct
            a.submission_date da, '#', b.submission_date db
            from submissions a, submissions b
            where a.submission_date <= b.submission_date
        ) t
        group by db
    ) days_since_beginning
    inner join
    (
        -- number of days since beginning of contest that hacker has submitted something
        select db submission_date, hb hacker_id, count(*) days_submitted 
        from
        (
            select distinct
            a.submission_date da, a.hacker_id ha, '#', b.submission_date db, b.hacker_id hb
            from submissions a, submissions b
            where a.submission_date <= b.submission_date
            and a.hacker_id = b.hacker_id
            order by db, hb
        ) t
        group by db, hb
    ) days_submitted_counts
    on days_since_beginning.submission_date = days_submitted_counts.submission_date
    and day_of_contest = days_submitted
) who_has_submitted_every_day
group by submission_date
;

/*
-- submissions per hacker per day
select *
from
(
    select submission_date, hacker_id, count(*) nsubmissions
    from submissions
    group by submission_date, hacker_id
) submissions_per_day
;

-- max number of submissions by any hacker that day.
select
*
from
(
    select submission_date, max(nsubmissions) max_submissions
    from
    (
        select submission_date, hacker_id, count(*) nsubmissions
        from submissions
        group by submission_date, hacker_id
    ) submissions_per_hacker_per_day
    group by submission_date
) max_per_day
;
*/

-- min name of all those who submitted max # of summissions for each date
select 
submission_date, min(name) name
from
(
    select 
    submissions_per_day.submission_date,
    submissions_per_day.hacker_id,
    max_per_day.max_submissions,
    hackers.name
    from
    (
        select submission_date, hacker_id, count(*) nsubmissions
        from submissions
        group by submission_date, hacker_id
    ) submissions_per_day
    inner join
    (
        select submission_date, max(nsubmissions) max_submissions
        from
        (
            select submission_date, hacker_id, count(*) nsubmissions
            from submissions
            group by submission_date, hacker_id
        ) submissions_per_hacker_per_day
        group by submission_date
    ) max_per_day
    on submissions_per_day.submission_date = max_per_day.submission_date
    and submissions_per_day.nsubmissions = max_per_day.max_submissions
    inner join hackers
    on submissions_per_day.hacker_id = hackers.hacker_id
) hackers_who_submitted_max_per_day
group by submission_date
;


/****************************************************/

select 
daily_submit_count.submission_date,
daily_submit_count.submit_count,
hackers.hacker_id,
who_submitted_max.name
from
(
    select submission_date, count(*) submit_count
    from
    (
        select
        days_since_beginning.submission_date,
        days_submitted_counts.hacker_id,
        days_submitted_counts.days_submitted
        from
        (
            -- for each date in the contest, count the number of days from the
        	-- beginning of the contest to that date (inclusive)
            select db submission_date, count(*) day_of_contest
            from
            (
                select distinct
                a.submission_date da, '#', b.submission_date db
                from submissions a, submissions b
                where a.submission_date <= b.submission_date
            ) t
            group by db
        ) days_since_beginning
        inner join
        (
            -- number of days since beginning of contest that hacker has submitted something
            select db submission_date, hb hacker_id, count(*) days_submitted 
            from
            (
                select distinct
                a.submission_date da, a.hacker_id ha, '#', b.submission_date db, b.hacker_id hb
                from submissions a, submissions b
                where a.submission_date <= b.submission_date
                and a.hacker_id = b.hacker_id
                order by db, hb
            ) t
            group by db, hb
        ) days_submitted_counts
        on days_since_beginning.submission_date = days_submitted_counts.submission_date
        and day_of_contest = days_submitted
    ) who_has_submitted_every_day
    group by submission_date
) daily_submit_count
inner join
(
    select 
    submission_date, min(name) name
    from
    (
        select 
        submissions_per_day.submission_date,
        submissions_per_day.hacker_id,
        max_per_day.max_submissions,
        hackers.name
        from
        (
            select submission_date, hacker_id, count(*) nsubmissions
            from submissions
            group by submission_date, hacker_id
        ) submissions_per_day
        inner join
        (
            select submission_date, max(nsubmissions) max_submissions
            from
            (
                select submission_date, hacker_id, count(*) nsubmissions
                from submissions
                group by submission_date, hacker_id
            ) submissions_per_hacker_per_day
            group by submission_date
        ) max_per_day
        on submissions_per_day.submission_date = max_per_day.submission_date
        and submissions_per_day.nsubmissions = max_per_day.max_submissions
        inner join hackers
        on submissions_per_day.hacker_id = hackers.hacker_id
    ) hackers_who_submitted_max_per_day
    group by submission_date
) who_submitted_max
on who_submitted_max.submission_date = daily_submit_count.submission_date
inner join hackers on who_submitted_max.name = hackers.name
order by daily_submit_count. submission_date
;

-- beware, maybe nobody submitted anything on some day.  still need to print
-- info for that day.
