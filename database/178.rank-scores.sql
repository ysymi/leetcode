select Score, (select count(*) from (select distinct Score as tmp_s from Scores) as tmp where tmp_s > Score) as Rank 
from Scores
order by Score desc

