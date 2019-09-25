\W

use hackerrank;

create temporary table doctor1 as
select rowid, name
from
(select @rowid := 0) init
inner join
(
select @rowid := @rowid + 1 rowid, name
from occupations
where occupation = 'doctor'
order by name
) doctor
;

create temporary table doctor2 as
select rowid, name
from
(select @rowid := 0) init
inner join
(
select @rowid := @rowid + 1 rowid, name
from occupations
where occupation = 'doctor'
order by name
) doctor
;

create temporary table professor1 as
select rowid, name
from
(select @rowid := 0) init
inner join
(
select @rowid := @rowid + 1 rowid, name
from occupations
where occupation = 'professor'
order by name
) professor
;

create temporary table professor2 as
select rowid, name
from
(select @rowid := 0) init
inner join
(
select @rowid := @rowid + 1 rowid, name
from occupations
where occupation = 'professor'
order by name
) professor
;

create temporary table singer1 as
select rowid, name
from
(select @rowid := 0) init
inner join
(
select @rowid := @rowid + 1 rowid, name
from occupations
where occupation = 'singer'
order by name
) singer
;

create temporary table singer2 as
select rowid, name
from
(select @rowid := 0) init
inner join
(
select @rowid := @rowid + 1 rowid, name
from occupations
where occupation = 'singer'
order by name
) singer
;

create temporary table actor1 as
select rowid, name
from
(select @rowid := 0) init
inner join
(
select @rowid := @rowid + 1 rowid, name
from occupations
where occupation = 'actor'
order by name
) actor
;

create temporary table actor2 as
select rowid, name
from
(select @rowid := 0) init
inner join
(
select @rowid := @rowid + 1 rowid, name
from occupations
where occupation = 'actor'
order by name
) actor
;

create temporary table part1 as
select ifnull(d1_rowid, p1_rowid) rowid, d_name, p_name
from
(
select d1.rowid d1_rowid, d1.name d_name, p1.rowid p1_rowid, p1.name p_name
from doctor1 d1
left join professor1 p1 on p1.rowid = d1.rowid

union

select d2.rowid d2_rowid, d2.name d_name, p2.rowid p2_rowid, p2.name p_name
from doctor2 d2
right join professor2 p2 on p2.rowid = d2.rowid
) x
;

create temporary table part2 as
select ifnull(s1_rowid, a1_rowid) rowid, s_name, a_name
from
(
select s1.rowid s1_rowid, s1.name s_name, a1.rowid a1_rowid, a1.name a_name
from singer1 s1
left join actor1 a1 on a1.rowid = s1.rowid

union

select s2.rowid s2_rowid, s2.name s_name, a2.rowid a2_rowid, a2.name a_name
from singer2 s2
right join actor2 a2 on a2.rowid = s2.rowid
) x
;

create temporary table part3 as
select * from part1
;

create temporary table part4 as
select * from part2
;

select d_name, p_name, s_name, a_name
from part1
left join part2
on part1.rowid = part2.rowid

union

select d_name, p_name, s_name, a_name
from part3
right join part4
on part3.rowid = part4.rowid

;
