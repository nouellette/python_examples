SELECT * FROM employees;

SELECT name, department FROM employees;

SELECT * FROM employees WHERE department = 'Sales';

SELECT * FROM employees ORDER BY age ASC;

SELECT AVG(salary) AS average_salary FROM employees WHERE department = 'Sales';

SELECT COUNT(*) AS number_of_employees FROM employees WHERE department = 'IT';

UPDATE employees SET salary = salary * 1.10 WHERE department = 'IT';

DELETE FROM employees WHERE age < 22;

INSERT INTO employees (name, age, department, salary) VALUES ('John Doe', 30, 'Marketing', 50000);

SELECT employees.name, departments.department_name
FROM employees
JOIN departments
ON employees.department = departments.department_id;