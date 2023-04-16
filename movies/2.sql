/* birth year of Emma Stone */

SELECT birth
  FROM people
 WHERE id = (SELECT id
               FROM people
              WHERE name LIKE 'Emma Stone');