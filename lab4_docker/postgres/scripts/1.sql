-- Ця реалізація демонстрирує, як використовувати команди memcache та to_json
-- для додавання нових кортежей, оновлення та видалення данних з кешу та перетворення даних у формат JSON.

CREATE OR REPLACE FUNCTION employees_to_cache() RETURNS TRIGGER AS
$$
BEGIN
    IF TG_OP = 'INSERT' THEN
        PERFORM memcache_add('employees::' || NEW.employee_id, to_json(NEW)::text);
    ELSIF TG_OP = 'UPDATE' THEN
        PERFORM memcache_set('employees::' || NEW.employee_id, to_json(NEW)::text);
    ELSIF TG_OP = 'DELETE' THEN
     PERFORM memcache_delete('employees::' || OLD.employee_id);
    END IF;
    RETURN NULL;
END;
$$
LANGUAGE plpgsql;

-- DROP TRIGGER employees_trigger ON employees;

CREATE CONSTRAINT TRIGGER employees_trigger AFTER INSERT OR UPDATE OR DELETE ON employees DEFERRABLE INITIALLY DEFERRED
    FOR EACH ROW
    EXECUTE PROCEDURE employees_to_cache();

