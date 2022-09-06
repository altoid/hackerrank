use hackerrank_top_competitors;

drop table if exists hackers;
drop table if exists difficulty;
drop table if exists challenges;
drop table if exists submissions;

create table hackers
(
hacker_id int not null primary key,
name varchar(22) not null
) engine=innodb;

create table difficulty
(
difficulty_level int not null primary key,
score int not null
) engine=innodb;

create table challenges
(
challenge_id int not null primary key,
hacker_id int not null,
difficulty_level int not null
) engine=innodb;

create table submissions
(
submission_id int not null primary key,
hacker_id int not null,
challenge_id int not null,
score int not null
) engine=innodb;


