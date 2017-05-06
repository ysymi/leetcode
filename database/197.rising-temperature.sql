select t1.Id from Weather as t1, Weather as t2 where datediff(t1.Date, t2.Date) = 1 and t1.Temperature > t2.Temperature;
