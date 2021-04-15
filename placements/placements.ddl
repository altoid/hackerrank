use placements;

create table if not exists
students
(
	id int not null auto_increment primary key,
	name varchar(16) not null
) engine=innodb;


create table if not exists
friends
(
	id int not null auto_increment primary key,
	friend_id int not null,
	foreign key (friend_id) references students(id) on delete cascade
) engine=innodb;


create table if not exists
packages
(
	id int not null auto_increment primary key,
	salary float not null
) engine=innodb;

insert into students
values
(1, 'ashley'),
(2, 'samantha'),
(3, 'julia'),
(4, 'scarlet')
;

insert into friends
values
(1, 2),
(2, 3),
(3, 4),
(4, 1)
;


insert into packages
values
(1, 15.20),
(2, 10.06),
(3, 11.55),
(4, 12.12)
;
