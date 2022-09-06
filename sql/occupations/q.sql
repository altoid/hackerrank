\W

use hackerrank;

drop table if exists professors;
drop table if exists singers;
drop table if exists doctors;
drop table if exists actors;
drop table if exists t1;
drop table if exists t2;
drop table if exists t3;
drop table if exists t4;
drop table if exists t5;
drop table if exists t6;
drop table if exists t7;
drop table if exists t8;
drop table if exists t9;

set @d = 0;
create temporary table doctors
select name, @d := @d + 1 as rowid from occupations
where occupation = 'doctor'
order by name
;

set @a = 0;
create temporary table actors
select name, @a := @a + 1 as rowid from occupations
where occupation = 'actor'
order by name
;

create temporary table t1
select d.name doctors, a.name actors, ifnull(a.rowid, d.rowid) rowid from doctors d
left join actors a
on d.rowid = a.rowid
;

create temporary table t2
select d.name doctors, a.name actors, ifnull(a.rowid, d.rowid) rowid from doctors d
right join actors a
on d.rowid = a.rowid
;

create temporary table t3
select * from t1
union
select * from t2
;

set @s = 0;
create temporary table singers
select name, @s := @s + 1 as rowid from occupations
where occupation = 'singer'
order by name
;

create temporary table t4
select t3.doctors, t3.actors, s.name singers, ifnull(s.rowid, t3.rowid) rowid from t3
left join singers s
on s.rowid = t3.rowid
;


create temporary table t5
select t3.doctors, t3.actors, s.name singers, ifnull(s.rowid, t3.rowid) rowid from t3
right join singers s
on s.rowid = t3.rowid
;

create temporary table t6
select * from t4
union
select * from t5
;

set @p = 0;
create temporary table professors
select name, @p := @p + 1 as rowid from occupations
where occupation = 'professor'
order by name
;


create temporary table t7
select t6.doctors, t6.actors, t6.singers, p.name professors, ifnull(p.rowid, t6.rowid) rowid from t6
left join professors p
on p.rowid = t6.rowid
;

create temporary table t8
select t6.doctors, t6.actors, t6.singers, p.name professors, ifnull(p.rowid, t6.rowid) rowid from t6
right join professors p
on p.rowid = t6.rowid
;

create temporary table t9
select * from t7
union
select * from t8
;

select doctors, professors, singers, actors from t9
;
