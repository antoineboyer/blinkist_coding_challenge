-- The number of users newly created in the last two weeks within the DACH region. 
SELECT COUNT(*) AS nb_users
FROM {{source('blinkist','user_fact')}}
WHERE country_code IN ('DE', 'AT', 'CH') AND 
        created_at >= current_date - INTERVAL '2 weeks'