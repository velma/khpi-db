DROP DATABASE IF EXISTS labs;

CREATE ROLE "labs-user" LOGIN PASSWORD 'password';

CREATE DATABASE labs ENCODING 'UTF-8' LC_COLLATE 'en_US.UTF-8' LC_CTYPE 'en_US.UTF-8' TEMPLATE template0 OWNER "labs-user";

\connect labs;
SET ROLE "labs-user";

CREATE TABLE employees (
    employee_id INTEGER GENERATED ALWAYS AS IDENTITY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    status VARCHAR(8) NOT NULL DEFAULT 'active' CONSTRAINT employee_status_ck CHECK (status IN ('active', 'inactive')),
    CONSTRAINT employees_pk PRIMARY KEY (employee_id)
);

CREATE TABLE clients (
    client_id INTEGER GENERATED ALWAYS AS IDENTITY,
    last_name VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    passport VARCHAR(15) NOT NULL,
    city VARCHAR(30) NOT NULL,
    CONSTRAINT clients_pk PRIMARY KEY (client_id),
    CONSTRAINT passport_uk UNIQUE(passport)
);

CREATE TABLE rooms (
    room_id INTEGER GENERATED ALWAYS AS IDENTITY,
    room_number VARCHAR(4) NOT NULL,
    floor_number INTEGER NOT NULL,
    phone VARCHAR(12),
    CONSTRAINT rooms_pk PRIMARY KEY (room_id),
    CONSTRAINT room_number_uk UNIQUE (room_number)
);

CREATE TABLE visits (
    visit_id INTEGER GENERATED ALWAYS AS IDENTITY,
    room_id INTEGER NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    CONSTRAINT visits_pk PRIMARY KEY (visit_id),
    CONSTRAINT rooms_fk FOREIGN KEY (room_id) REFERENCES rooms (room_id)
);

CREATE TABLE visit_clients (
    visit_id INTEGER NOT NULL REFERENCES visits(visit_id),
    client_id INTEGER NOT NULL REFERENCES clients(client_id),
    CONSTRAINT visit_clients_pk PRIMARY KEY (visit_id, client_id),
    CONSTRAINT visit_clients_visit_fk FOREIGN KEY (visit_id) REFERENCES visits (visit_id),
    CONSTRAINT visit_clients_client_fk FOREIGN KEY (client_id) REFERENCES clients (client_id)
);

CREATE TABLE cleaning_schedule (
    employee_id INTEGER NOT NULL REFERENCES employees(employee_id),
    floor_number INTEGER NOT NULL,
    schedule_date DATE NOT NULL,
    CONSTRAINT cleaning_schedule_pk PRIMARY KEY (employee_id, floor_number, schedule_date),
    CONSTRAINT employees_fk FOREIGN KEY (employee_id) REFERENCES employees (employee_id)
);