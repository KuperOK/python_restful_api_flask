create database depemp1;

use database depemp1;

create table department (
dep_id int AUTO_INCREMENT primary key,
dep_name varchar(30) not null
) ;

create table employee (
emp_id int AUTO_INCREMENT primary key,
emp_name varchar(30) not null,
date_of_birth date not null,
salary float not null,
dep_id  int ,
foreign key (dep_id) references department(dep_id)) on delete set null on update cascade ) ;
