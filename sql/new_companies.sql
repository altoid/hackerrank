use hackerrank;

select
distinct
c.*,
lm.lead_manager_code,
sm.senior_manager_code,
m.manager_code,
e.employee_code
from company c
inner join lead_manager lm on lm.company_code = c.company_code
inner join senior_manager sm on sm.company_code = lm.company_code
inner join manager m on m.company_code = sm.company_code
inner join employee e on e.company_code = m.company_code
;

select
distinct
c.*,
lm.lead_manager_code
from company c
inner join lead_manager lm on lm.company_code = c.company_code
;

select
distinct
c.*,
sm.senior_manager_code
from company c
inner join senior_manager sm on sm.company_code = c.company_code
;

select
distinct
c.*,
m.manager_code
from company c
inner join manager m on m.company_code = c.company_code
;

select
distinct
c.*,
e.employee_code
from company c
inner join employee e on e.company_code = c.company_code
;

select company_code, count(*) c, 'lmcounts' type from
(
select distinct
company_code, lead_manager_code
 from lead_manager
) lmcounts
group by company_code

union all

select company_code, count(*) c, 'smcounts' type from
(
select distinct
company_code, senior_manager_code
 from senior_manager
) smcounts
group by company_code

union all

select company_code, count(*) c, 'mcounts' type from
(
select distinct
company_code, manager_code
 from manager
) mcounts
group by company_code

union all

select company_code, count(*) c, 'ecounts' from
(
select distinct
company_code, employee_code
 from employee
) ecounts
group by company_code
;

