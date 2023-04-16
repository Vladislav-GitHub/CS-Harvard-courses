/* names of all people who starred in a movie released in 2004, ordered by birth year */

SELECT DISTINCT name
           FROM people
                JOIN stars
                ON stars.person_id=people.id
                   JOIN movies
                   ON stars.movie_id=movies.id
                      JOIN ratings
                      ON ratings.movie_id=movies.id
                         WHERE year = 2004
                         ORDER BY birth; 