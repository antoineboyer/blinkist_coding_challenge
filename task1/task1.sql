-- to translate into DBT
CREATE SCHEMA blinkist;

CREATE TABLE blinkist.user_fact(
  user_id VARCHAR(50) PRIMARY KEY, -- user_id should be unique
  created_at TIMESTAMP WITHOUT TIME ZONE, -- Always store time in UTC
  country_code VARCHAR(2) -- https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
);

CREATE TABLE blinkist.daily_web_activity(
  user_id VARCHAR(50),
  web_activity_date DATE, -- Renaming `date` to `web_activity_date` as date is a sql keyword
  n_sessions INT 
);

CREATE TABLE blinkist.daily_app_activity(
  user_id VARCHAR(50),
  app_activity_date DATE, -- Renaming `date` to `app_activity_date` as date is a sql keyword
  units_bib_audio INT,
  units_shortcuts INT
);

 -- for now in plain SQL
 -- The number of users newly created in the last two weeks within the DACH region. 
SELECT COUNT(*)
FROM blinkist.user_fact 
WHERE country_code IN ('DE', 'AT', 'CH') AND 
        created_at >= current_date - INTERVAL '2 weeks'

-- All users being active at least once in any form (web or app) 
-- in the last 2 weeks who became Blinkist users in 2021.
WITH users_2021 AS 
(
  SELECT user_id
  FROM blinkist.user_fact 
  WHERE extract(year from created_at) = '2021'
)
SELECT dwa.user_id
FROM blinkist.daily_web_activity dwa
JOIN users_2021 USING(user_id)
WHERE web_activity_date >= current_date - INTERVAL '2 weeks'

UNION -- removes duplicate records

SELECT dda.user_id
FROM blinkist.daily_app_activity dda
JOIN users_2021 USING(user_id)
WHERE app_activity_date >= current_date - INTERVAL '2 weeks'
;