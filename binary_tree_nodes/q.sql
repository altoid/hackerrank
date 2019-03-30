\W

use hackerrank;

select n, t from
(
select n, 'Inner' t from bst as x
where exists (select p from bst where x.n = p) and p is not null
union
select n, 'Root' t from bst where p is null
union
select n, 'Leaf' t from bst as x
where not exists (select p from bst where x.n = p)
) z
order by n
;
