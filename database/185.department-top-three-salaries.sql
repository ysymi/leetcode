-- 这个组里比某个员工的salary多的人，不超过3个，说明这个员工salary排名前3

select de.Name as Department, em.Name as Employee, em.Salary as Salary
 from Department as de, Employee as em
 where (select count(distinct(Salary)) from Employee where DepartmentId = em.DepartmentId and Salary > em.Salary) < 3
        and em.DepartmentId = de.Id
         order by em.Salary desc ;
