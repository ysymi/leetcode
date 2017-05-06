select distinct l1.Num as ConsecutiveNums
from Logs as l1 join Logs as l2 on l1.Id + 1 = l2.Id
                join Logs as l3 on l3.Id - 1 = l2.Id 
where l1.Num = l2.num and l2.Num = l3.Num;
