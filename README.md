# Python Developer - Take Home Exercise

```
LANGUAGES:                  Python
MUST USE FRAMEWORKS:        Flask, TikTok-Api
TESTS (UNIT, INTEGRATION):  nice to have, but not mandatory
```

## Overview

This exercise is about implementing the best possible solution to our problem: _**collecting data about tiktok users**_.

We're evaluating your ability to take a set of requirements and spike a holistic solution that is beautiful, intuitive and easy to debug/test/extend.

Ideally, your solution would have some way to run locally and test the results so we can fully analyze your efforts.

---

### Exercise: 

The goal of this exercise is to design a basic REST API that allows developers to collect data about tiktok users


#### User Story: As a developer I want to

* Add tiktok user to the database via a`POST` request. The endpoint should accept a JSON payload that includes the tiktok username, pulls all user data from tiktok via [TikTok-Api](https://github.com/davidteather/TikTok-Api) and stores it in a database
  * **Payload example**:
  ```json
    {"tiktok_username": "realmadrid"}
  ```

* Fetch a single tiktok user via `GET` request. The endpoint should accept either a tiktok username or a tiktok user id
  * **Examples**: Let's assume 435787539865 is the tiktok id of [realmadrid](https://www.tiktok.com/@realmadrid). The developer has the option to fetch realmadrid data from your api using either one of these paths: `/tiktok_users/realmadrid` OR `/tiktok_users/435787539865`

### A few quick notes

* Other than the user id, there is no requirement on which fields should be stored in the database
* You have total freedom on how you want to design your databases schemas. Please do whatever makes the most sense to you given the time allocated. Ideally this exercise would use MYSQL, SQLite or Postgres, but any SQL database is OK.
* If you'd like to use an ORM to make this easier, thats fine with us!
* [Flask](https://github.com/pallets/flask) and  [TikTok-Api](https://github.com/davidteather/TikTok-Api) are the only packages that are required for this exercise. Feel free to install other pip packages if necessary

---

## Submitting your exercise

- Once you are done, push your code to a github
- Include a readme file in your repo that covers the following topics:
  - How much time it took you to finish the exercise (number of hours)
  - You database design
  - Steps to run the flask app
  - Issues/challenges you faced when you are solving this exercise
  - Possible ways to improve the api
