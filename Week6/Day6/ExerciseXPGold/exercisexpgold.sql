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


select first_name, last_name, birth_date from students order by last_name asc limit 4;
select first_name, last_name, birth_date from students where birth_date = (select max(birth_date) from students);
select first_name, last_name, birth_date from students limit 3 offset 2;