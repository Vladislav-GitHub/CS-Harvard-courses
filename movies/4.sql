/* number of movies with an IMDb rating of 10.0 */

SELECT COUNT(movies.id)
  FROM movies
       JOIN ratings
       ON movies.id = ratings.movie_id
          AND ratings.rating = 10;