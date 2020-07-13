-- LIsts number of records with same score --
-- MySQL server --
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
