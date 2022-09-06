use ollivander;

select 
w.id,
wp.age,
w.coins_needed,
w.power
from
(
    select
    wp.age,
    min(w.coins_needed) coins_needed,
    w.power
    from wands w
    inner join wands_property wp
    on wp.code = w.code
    where is_evil = 0
    group by wp.age, w.power
) min_coins_per_power_age
inner join wands_property wp on wp.age = min_coins_per_power_age.age
inner join wands w on w.code = wp.code and w.coins_needed = min_coins_per_power_age.coins_needed
order by w.power desc, wp.age desc
;
