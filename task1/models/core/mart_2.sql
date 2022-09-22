-- All users being active at least once in any form (web or app) 
-- in the last 2 weeks who became Blinkist users in 2021.
WITH users_2021 AS 
(
  SELECT user_id
  FROM {{source('blinkist','user_fact')}}
  WHERE extract(year from created_at) = '2021'
)
SELECT dwa.user_id
FROM {{source('blinkist','daily_web_activity')}} dwa
JOIN users_2021 USING(user_id)
WHERE web_activity_date >= current_date - INTERVAL '2 weeks'

UNION -- removes duplicate records

SELECT dda.user_id
FROM {{source('blinkist','daily_app_activity')}} dda
JOIN users_2021 USING(user_id)
WHERE app_activity_date >= current_date - INTERVAL '2 weeks'