\connect labs;
SET ROLE "labs-user";

-- клієнти, які проживають у заданому номері,
SELECT c.* FROM visits v
JOIN visit_clients vc ON vc.visit_id = v.visit_id
JOIN clients c ON c.client_id = vc.client_id
JOIN rooms r ON r.room_id = v.room_id
WHERE v.end_date IS NULL
  AND v.start_date >= CURRENT_DATE
  AND r.room_number = '102a';

-- клієнти, які прибули із заданого міста,
SELECT * from clients WHERE city = 'New York';

-- хто із службовців прибирав номер вказаного клієнта у заданий день
SELECT e.* FROM employees e
JOIN cleaning_schedule s ON s.employee_id = e.employee_id
WHERE s.schedule_date = current_date + INTERVAL '1 day'
  AND floor_number IN (
    SELECT r.floor_number FROM visit_clients vc
    JOIN visits v ON v.visit_id = vc.visit_id
    JOIN rooms r ON r.room_id = v.room_id
    WHERE vc.client_id = 1
  );

-- чи є в готелі вільні місця та вільні номери і, якщо є, то скільки.
SELECT COUNT(1) FROM rooms r
WHERE NOT EXISTS (
    SELECT 1 FROM visits v
    WHERE r.room_id = v.room_id
      AND v.end_date IS NULL
);

--прийняти на роботу або звільнити службовця готелю.
INSERT INTO employees (last_name, first_name) VALUES ('Employee', 'Test');
UPDATE employees SET status = 'inactive' WHERE employee_id = CURRVAL(pg_get_serial_sequence('employees', 'employee_id'));

-- змінити розклад роботи службовця.
INSERT INTO cleaning_schedule (employee_id, floor_number, schedule_date)
VALUES (CURRVAL(pg_get_serial_sequence('employees', 'employee_id')), 3, current_date + INTERVAL '3 day');

UPDATE cleaning_schedule set floor_number = 2
    WHERE employee_id = CURRVAL(pg_get_serial_sequence('employees', 'employee_id')) AND floor_number = 3 AND schedule_date = current_date + INTERVAL '3 day';

-- поселити чи виселити клієнта.
INSERT INTO clients (last_name, first_name, passport, city) VALUES ('Client', 'Test', 'RAND' || CURRVAL(pg_get_serial_sequence('clients', 'client_id')), 'New York');

INSERT INTO visits (room_id, start_date, end_date)
VALUES (4, current_date - INTERVAL '6 day', NULL);

INSERT INTO visit_clients (visit_id, client_id)
VALUES (CURRVAL(pg_get_serial_sequence('visits', 'visit_id')), CURRVAL(pg_get_serial_sequence('clients', 'client_id')));

UPDATE visits SET end_date = current_date - INTERVAL '4 day'
WHERE visit_id = CURRVAL(pg_get_serial_sequence('visits', 'visit_id'));