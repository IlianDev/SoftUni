SELECT last_name FROM employees
WHERE salary = 900 AND first_name = 'John';

SELECT last_name FROM employees
WHERE NOT salary = 900;

SELECT last_name FROM employees
WHERE salary = 900 OR salary = 1100;

SELECT last_name, salary FROM employees
WHERE NOT (salary = 900 OR salary = 1100);

SELECT last_name, salary FROM employees
WHERE salary >= 900 AND salary <= 2100;

SELECT last_name, salary FROM employees
WHERE salary BETWEEN 900 AND 2100;

SELECT first_name, last_name
FROM employees
WHERE salary IN (2100, 1100, 900, 880);
