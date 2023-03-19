\connect labs;
SET ROLE "labs-user";

INSERT INTO employees (last_name, first_name)
VALUES ('Bloggs', 'Joe'), ('Schmoe', 'Joe');

INSERT INTO clients (last_name, first_name, passport, city)
VALUES ('Doe', 'John', 'SM11111', 'New York'), ('Doe', 'Jane', 'SM22222', 'New York'), ('Unknown', 'Name', 'SM3333', 'Paris');

INSERT INTO rooms (room_number, floor_number, phone)
VALUES ('101', 1, '+38011111111'), ('102a', 1, '+38011111112'), ('102b', 1, '+38011111113'),
       ('201', 2, '+38011111114'), ('301', 3, '+38011111115'), ('302', 3, '+38011111116');

INSERT INTO visits (room_id, start_date, end_date)
VALUES (1, current_date - INTERVAL '10 day', current_date - INTERVAL '7 day'),
	   (1, current_date - INTERVAL '5 day', current_date - INTERVAL '2 day'),
	   (1, current_date, NULL), (2, current_date, NULL);

INSERT INTO visit_clients (visit_id, client_id)
VALUES (1, 3), (2, 3), (3, 3), (4, 1), (4, 2);

INSERT INTO cleaning_schedule (employee_id, floor_number, schedule_date)
VALUES (1, 1, current_date + INTERVAL '1 day'), (1, 2, current_date + INTERVAL '1 day'), (2, 3, current_date + INTERVAL '1 day'),
       (1, 1, current_date + INTERVAL '2 day'), (2, 2, current_date + INTERVAL '2 day'), (2, 3, current_date + INTERVAL '2 day');
