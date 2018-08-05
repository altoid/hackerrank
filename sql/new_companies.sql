use hackerrank;

select
c.*,
t1.lmcounts,
t2.smcounts,
t3.mcounts,
t4.ecounts
from
company c
inner join
(
select company_code, count(*) lmcounts from
(
select distinct
company_code, lead_manager_code
 from lead_manager
) lmcounts
group by company_code
) t1 on t1.company_code = c.company_code
inner join
(
select company_code, count(*) smcounts from
(
select distinct
company_code, senior_manager_code
 from senior_manager
) smcounts
group by company_code
) t2 on t1.company_code = t2.company_code
inner join
(
select company_code, count(*) mcounts from
(
select distinct
company_code, manager_code
 from manager
) mcounts
group by company_code
) t3 on t2.company_code = t3.company_code
inner join
(
select company_code, count(*) ecounts from
(
select distinct
company_code, employee_code
 from employee
) ecounts
group by company_code
) t4 on t3.company_code = t4.company_code

order by c.company_code
;

