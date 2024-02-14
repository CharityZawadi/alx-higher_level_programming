--Lists all Comedy shows in the database hbtn_0d_tvshows
SELECT DISTINCT tv_shows.title 
FROM hbtn_0d_tvshows.tv_shows 
JOIN hbtn_0d_tvshows.tv_shows_genres ON tv_shows.id = tv_shows_genres.tv_show_id 
JOIN hbtn_0d_tvshows.tv_genres ON tv_genres.id = tv_shows_genres.genre_id 
WHERE tv_genres.name = 'Comedy' 
ORDER BY tv_shows.title ASC;

