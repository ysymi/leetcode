-- this solution can select a single value or A null, can not used for select multi columns and rows
select (select distinct Salary from Employee order by Salary desc limit 1 offset 1) as SecondHighestSalary



-- this is one of my wrong solution
-- (select Salary as SecondHighestSalary from Employee order by Salary desc limit 1 offset 1)  union  (select NULL as SecondHighestSalary)
