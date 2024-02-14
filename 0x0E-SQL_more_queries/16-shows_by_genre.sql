-- Lists all shows and all genres linked to that show, from the database hbtn_0d_tvshows
SELECT DISTINCT tv_shows.title, tv_genres.name 
FROM hbtn_0d_tvshows.tv_shows 
LEFT JOIN hbtn_0d_tvshows.tv_shows_genres ON tv_shows.id = tv_shows_genres.tv_show_id 
LEFT JOIN hbtn_0d_tvshows.tv_genres ON tv_genres.id = tv_shows_genres.genre_id 
ORDER BY tv_shows.title ASC, tv_genres.name ASC;

