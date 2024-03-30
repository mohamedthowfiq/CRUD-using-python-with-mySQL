create database studentDB;
use studentDB;
create table users(
ID integer auto_increment primary key,
Name varchar(50),
Age integer,
City varchar(50)
);
select * from users;
insert into users(Name,Age,City) values('Ram',24,'Tenkasi');
insert into users(Name,Age,City) values('ravi',25,'tirunelveli');
insert into users(Name,Age,City) values('thowfiq',23,'tenkasi');
insert into users(Name,Age,City) values('sangara',23,'srivilliputhur');
