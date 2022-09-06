\W

use hackerrank_top_competitors;

-- show submissions and the possible score for each challenge

select h.hacker_id, h.name
from
hackers h
inner join
(
    select s.hacker_id, count(*) c
    from submissions s
    inner join challenges c on c.challenge_id = s.challenge_id
    inner join difficulty d on c.difficulty_level = d.difficulty_level
    where s.score = d.score
    group by s.hacker_id
    having count(*) > 1
) result
on h.hacker_id = result.hacker_id
order by result.c desc, h.hacker_id
;
