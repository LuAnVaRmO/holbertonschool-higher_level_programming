-- Count by genre --
-- MySQL server --
SELECT g.name AS genre, COUNT(g.name) AS number_of_shows FROM tv_shows s INNER JOIN tv_show_genres sg ON s.id = sg.show_id INNER JOIN tv_genres g ON g.id = sg.genre_id GROUP BY g.name ORDER BY number_of_shows DESC;
