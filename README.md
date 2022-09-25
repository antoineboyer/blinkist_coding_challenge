# Blinkist Coding Challenge

### Task 1

You can interact with the Blinkist product via the web and the app. Given the following tables:

| user_fact    | type      | description                         |
|--------------|-----------|-------------------------------------|
| user_id      | varchar   | id of the user                      |
| created_at   | timestamp | time the user was created           |
| country_code | varchar   | country of the user in code alpha-2 |


---

| daily_web_activity | type    | description                      |
|--------------------|---------|----------------------------------|
| user_id            | varchar | id of the user                   |
| date               | date    | date the user was active         |
| n_sessions         | int     | number of session a user started |

---

| daily_app_activity | type    | description                                 |
|--------------------|---------|---------------------------------------------|
| user_id            | varchar | id of the user                              |
| date               | date    | date the user was active                    |
| units_bib_audio    | int     | number of audio units consumed by a user    |
| units_shortcuts    | int     | number of shortcut units consumed by a user |


Please write in dbt (preferred) or plain sql queries that return:
1. The number of users newly created in the last two weeks within the DACH region. 
2. All users being active at least once in any form (web or app) in the last 2 weeks who became Blinkist users in 2021.

Assume we use Redshift as DB.

### Answers of Task 1

I reproduced a minimalist DBT project. I included some [documentations](./task1/models/core/scr_blinkist.yml) and some [tests](./task1/models/core/mart.yml). The SQL queries are under [models/core](./task1/models/core/).

### Task 2

To retrieve the latest exchange rates we query the [opendexchangerates api](https://docs.openexchangerates.org/docs/latest-json).  

The result looks like this:

```
{
    disclaimer: "https://openexchangerates.org/terms/",
    license: "https://openexchangerates.org/license/",
    timestamp: 1449877801,
    base: "USD",
    rates: {
        AED: 3.672538,
        AFN: 66.809999,
        ALL: 125.716501,
        AMD: 484.902502,
        ANG: 1.788575,
        AOA: 135.295998,
        ARS: 9.750101,
        AUD: 1.390866,
        ...
    }
}
```

Please create a lambda function using the [serverless framework](https://www.serverless.com/framework/docs/providers/aws/guide/functions) that queries the latest exchange rates for base EUR and saves the result as json to a bucket on S3.

To share your results please use a repository on Github or Gitlab and send us the link. We are looking forward to your solution. :)

### Answers of Task 2
Following, the commands to create and deploy the lambda function:
```
sls plugin install -n serverless-python-requirements
sls deploy
```