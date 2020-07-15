-- List all citites of california --
-- MySQL server --
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = "California");
