\W

use hackerrank_15_days;

-- problem is badly worded.  want everyone who made a submission on a given day.

-- max counts among hackers on a given day.
select submission_date, max(c) most_submissions
from
(
select submission_date, count(*) c
from submissions
group by submission_date, hacker_id
) counts_per_hacker_per_day
group by submission_date
;

-- min hacker id for each count per day
select submission_date, c, min(hacker_id) min_hacker_id
from
(
select submission_date, count(*) c, hacker_id
from submissions
group by submission_date, hacker_id
) counts_per_hacker_per_day
group by submission_date, c
;

select
min_hacker_id_by_count_per_day.*
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
-- inner join hackers
-- on min_hacker_id_by_count_per_day.min_hacker_id = hackers.hacker_id
;
