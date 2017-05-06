select de.Name as Department, em.Name as Employee, em.Salary as Salary 
from Department as de, Employee as em
where de.Id = em.DepartmentId and 
(DepartmentId, Salary) in (select DepartmentId,max(Salary) FROM Employee GROUP BY DepartmentId);
