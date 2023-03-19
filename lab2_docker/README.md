## Purpose

Sample project for LAB_2.

## Blog post

- 2021.12.13: [Hands-on with PostgreSQL Authorization (Part 1): Roles and Grants](https://www.tangramvision.com/blog/hands-on-with-postgresql-authorization-part-1-roles-and-grants)

## Usage

This project uses Docker to run the PostgreSQL database, to avoid installing
a bunch of packages on your machine and potentially running into different
platform and environment issues.

If you don't have Docker, please visit https://docs.docker.com/get-docker/.

To run the database with the example schema:

```
docker-compose up 
```

To open a psql prompt in that container, run the following in another terminal start **_psql.bat** or **_psql.sh** depending on your system 

To run SQL statements located in .sql files in psql use:

```
\i /repo/sample_queries.sql
```
