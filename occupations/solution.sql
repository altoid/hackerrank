\W

use hackerrank;

set @d := 0, @p := 0, @a := 0, @s := 0;

select min(doctor), min(professor), min(singer), min(actor)
from
(
    select
    case occupation
    when 'Doctor'    then @d := @d + 1
    when 'Professor' then @p := @p + 1
    when 'Singer'    then @s := @s + 1
    when 'Actor'     then @a := @a + 1
    end rownum,
    occupation,
    case occupation when 'Doctor' then name end doctor,
    case occupation when 'Professor' then name end professor,
    case occupation when 'Singer' then name end singer,
    case occupation when 'Actor' then name end actor
    from occupations
    order by name
) x
group by rownum
;

