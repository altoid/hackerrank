\W

use hackerrank_15_days;

-- problem is badly worded.  want everyone who made a submission on a given day.

select count(*), submission_date from submissions
group by submission_date
order by submission_date
;

select submission_date, count(*), name 
from submissions s
inner join hackers h on h.hacker_id = s.hacker_id 
group by submission_date, h.hacker_id
order by submission_date, count(*) desc, name
;


