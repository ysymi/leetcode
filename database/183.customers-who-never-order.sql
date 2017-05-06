select c.Name as Customers from Customers as c left join Orders as o on c.id = o.CustomerId where o.id is null;
