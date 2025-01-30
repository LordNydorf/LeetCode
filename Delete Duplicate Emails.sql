DELETE FROM Person
WHERE id NOT IN (SELECT min_id FROM
(SELECT min(Id) AS min_id FROM Person GROUP BY Email) AS a)
