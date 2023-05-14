INSERT INTO employees (employee_id, last_name, first_name, status) VALUES (default, 'New', 'Employee', 'active');

UPDATE employees SET status = 'inactive' WHERE employee_id = 2;

DELETE FROM employees WHERE employee_id = 3;

