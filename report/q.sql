\W

use hackerrank;

select if (g.grade < 8, null, s.name) `name`, g.grade, s.marks
from 
students s
inner join grades g
on s.marks between g.min_mark and g.max_mark
order by grade desc, name, marks
;

