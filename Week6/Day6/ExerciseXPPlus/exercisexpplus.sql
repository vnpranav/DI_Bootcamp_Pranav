-- Database: bootcamp

-- DROP DATABASE IF EXISTS bootcamp;

-- CREATE DATABASE bootcamp
--     WITH
--     OWNER = postgres
--     ENCODING = 'UTF8'
--     LC_COLLATE = 'English_United States.1252'
--     LC_CTYPE = 'English_United States.1252'
--     LOCALE_PROVIDER = 'libc'
--     TABLESPACE = pg_default
--     CONNECTION LIMIT = -1
--     IS_TEMPLATE = False;

-- create table students(
-- student_id serial primary key,
-- last_name varchar(50) not null,
-- first_name varchar(50) not null,
-- birth_date date)

-- insert into students(last_name, first_name, birth_date) values ('Marc', 'Benichou', '1998-11-02'), ('Yoan', 'Cohen', '2010-12-03'), ('Lea', 'Benichou', '1987-07-27'), ('Amelia','Dux', '1996-04-07'),
-- ('David', 'Grez', '2003-06-14'), ('Omer', 'Simpson', '1980-10-03')


select * from students;
select first_name, last_name from students;
select first_name, last_name from students where student_id = 2;
select first_name, last_name from students where first_name = 'Marc' and last_name = 'Benichou';
select first_name, last_name from students where first_name = 'Marc' or last_name = 'Benichou';
select first_name, last_name from students where first_name like '%a%';
select first_name, last_name from students where first_name like 'A%';
select first_name, last_name from students where first_name like '%a';
select first_name, last_name from students where first_name like '%a_';
select first_name, last_name from students where student_id in (1,3);
select first_name, last_name from students where birth_date >= '2001-01-01';