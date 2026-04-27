CREATE DATABASE if not exists hr_system;
USE hr_system;
create table if not exists departments ( dept_id int primary key auto_increment, dept_name varchar(50) not null);
insert into departments (dept_name) values ('IT'), ('HR'), ('Sales');
select dept_name from departments where dept_name = 'IT';