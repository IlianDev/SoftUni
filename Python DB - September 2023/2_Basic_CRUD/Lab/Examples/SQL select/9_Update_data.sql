-- Update
UPDATE employees
SET last_name = 'Brown'
WHERE id = 1;

-- Multible updates
UPDATE employees
SET salary = salary * 1.10,
job_title = 'Senior ' || job_title
WHERE department_id = 3;