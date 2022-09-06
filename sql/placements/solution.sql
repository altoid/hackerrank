use placements;

select
my_name
from
(
select students_names.name my_name, my_packages.salary my_salary, friends_names.name friend_name, friends_packages.salary friend_salary
from students students_names
inner join  friends
on students_names.id = friends.id
inner join students friends_names
on friends.friend_id = friends_names.id
inner join packages friends_packages
on friends_packages.id = friends_names.id
inner join packages my_packages
on my_packages.id = students_names.id
) wrap
where friend_salary > my_salary
order by friend_salary
;
