CREATE ROLE "hotel-user" LOGIN PASSWORD 'password';

CREATE DATABASE hotel ENCODING 'UTF-8' LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8' TEMPLATE template0 OWNER "hotel-user";