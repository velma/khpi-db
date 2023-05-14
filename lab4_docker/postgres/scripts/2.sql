create extension pgmemcache;

SELECT memcache_add('employees::' || employee_id, (
    SELECT to_json(foo)
    FROM (
         SELECT employee_id, last_name, first_name, status) AS FOO)::text
) FROM employees;

