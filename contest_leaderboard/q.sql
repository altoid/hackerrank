\W

use hackerrank;

select h.hacker_id, `name`, total
from hackers h
inner join
(
select hacker_id, sum(max_score) total from
(
select hacker_id, challenge_id, max(score) max_score from submissions
group by hacker_id, challenge_id
order by hacker_id, challenge_id
) max_scores_by_challenge
group by hacker_id
) th
on h.hacker_id = th.hacker_id
where total > 0
order by total desc, hacker_id
;
