\W

use hackerrank_15_days;

select
s2.submission_date,
s1.hacker_id,
count(*)

from submissions s1
inner join submissions s2
on s1.hacker_id = s2.hacker_id
and s1.submission_date <= s2.submission_date
group by s2.submission_date,
s1.hacker_id
;
