docker-compose exec --env PGPASSWORD=password --interactive --tty postgres_db psql --username="labs-user" --dbname="labs" %*
