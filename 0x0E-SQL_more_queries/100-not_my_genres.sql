--Lists all genres not linked to the show Dexter, from the database hbtn_0d_tvshows
SELECT tv_genres.name 
FROM hbtn_0d_tvshows.tv_genres 
WHERE tv_genres.id NOT IN (
  SELECT tv_shows_genres.genre_id 
  FROM hbtn_0d_tvshows.tv_shows_genres 
  JOIN hbtn_0d_tvshows.tv_shows ON tv_shows.id = tv_shows_genres.tv_show_id 
  WHERE tv_shows.title = 'Dexter'
) 
ORDER BY tv_genres.name ASC;

