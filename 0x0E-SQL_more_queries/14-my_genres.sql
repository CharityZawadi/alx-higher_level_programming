--Lists all genres of the show Dexter in the hbtn_0d_tvshows databas
SELECT DISTINCT tv_genres.name 
FROM hbtn_0d_tvshows.tv_genres 
JOIN hbtn_0d_tvshows.tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id 
JOIN hbtn_0d_tvshows.tv_shows ON tv_shows_genres.tv_show_id = tv_shows.id 
WHERE tv_shows.title = 'Dexter' 
ORDER BY tv_genres.name ASC;

