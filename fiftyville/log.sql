-- Keep a log of any SQL queries you execute as you solve the mystery.

SELECT *
  FROM crime_scene_reports
 WHERE year = 2021
   AND month = 7
   AND day = 28
   AND Street = 'Humphrey Street'
  -- time = 10:15am at the bakery, 3 witnesses

SELECT name
FROM people
WHERE phone_number IN (
    SELECT caller
    FROM phone_calls
    WHERE year = 2021
    AND month = 7
    AND day = 28
    AND duration < 60);
-- This will get the name of all the people who made a call on the day that was less than a minute
-- a notable hint pointed out by one our witnesses
-- output is Kenny, Sofia, Benista, Taylor, Diana, Kelsey, Bruce, Carina

SELECT *
FROM interviews
WHERE year = 2021 -- by the ATM on Leggett Street and saw the thief there withdrawing some money
  AND month = 7 -- and planning to take the earliest flight out of Fiftyville tomorrow (29.07.21).
  AND day = 28; -- The thief then asked the person on the other end of the phone to purchase the flight ticket.
-- whispering into a phone for about half an hour

SELECT *
FROM airports
WHERE city LIKE 'Fiftyville'; -- abbreviation: CSF, id: 8

SELECT *
FROM flights
WHERE year = 2021
  AND month = 7
  AND day = 29
  AND origin_airport_id = '8'; -- earliest flight is at 8 hour 8:20, destination_airport_id = 4, origin_airport id = 8, flight id = 36

SELECT DISTINCT name
           FROM people
           JOIN bank_accounts ON people.id = bank_accounts.person_id
           JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number
           WHERE day = 28
           AND month = 7
           AND year = 2021
           AND transaction_type = 'withdraw'
           AND atm_location = 'Leggett Street';
-- Suspects: Luca, Kenny, Taylor, Bruce, Brooke, Iman, Benista, Diana

-- After filtering who withdrew money, who left the bakery at a specific time and who was on the earliest plane out of fiftyville
-- the next day we narrowed it down to suspect Kenny, Benista, Taylor, Diana and Bruce

SELECT city
FROM airports
WHERE id = (
SELECT destination_airport_id
FROM flights
WHERE year = 2021 AND month= 7 AND day = 29
ORDER BY hour, minute
LIMIT 1); -- New York City

SELECT name
FROM people
     JOIN phone_calls
     ON people.phone_number = phone_calls.receiver
        WHERE year = 2021
        AND month = 7
        AND day = 28
        AND duration < 60
        AND caller = (
        SELECT phone_number
        FROM people
        WHERE name = 'Bruce');

SELECT name
FROM people
     JOIN passengers
       ON people.passport_number = passengers.passport_number
          JOIN flights
          ON passengers.flight_id = flights.id
             WHERE origin_airport_id = 8
               AND destination_airport_id = 4
               AND year = 2021
               AND month = 7
               AND hour = 8
               AND minute = 20;
               -- Doris, Sofia, Bruce, Edward, Kelsey, Taylor, Kenny, Luca
               -- Suspects: Kenny, Taylor, Bruce
-- Kenny: amount = 20, id = 395717, phone_number: (826) 555-1652, passport_number: 9878712108, license_plate: 30G67EN, person_id: 395717, account_number: 28296815
-- Taylor: amount = 60, id = 449774, phone_number: (286) 555-6063, passport_number: 1988161715, license_plate: 1106N58, person_id: 449774, account_number: 76054385
-- Bruce: amount = 50, id = 686048, phone_number: (367) 555-5533, passport_number: 5773159633, license_plate: 94KL13X, person_id: 686048, account_number: 49610011