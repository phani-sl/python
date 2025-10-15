
CREATE TABLE employees (
    emp_id SERIAL PRIMARY KEY,
    emp_name VARCHAR(50),
    salary NUMERIC(10,2),
    dept_id INT
);

ALTER TABLE employees
ADD COLUMN date_of_joining DATE;

ALTER TABLE employees
DROP COLUMN date_of_joining;

ALTER TABLE employees
ALTER COLUMN salary TYPE NUMERIC(12,2);

-- Create referenced table
CREATE TABLE departments (
    dept_id SERIAL PRIMARY KEY,
    dept_name VARCHAR(50)
);

ALTER TABLE employees
ADD CONSTRAINT fk_dept
FOREIGN KEY (dept_id) REFERENCES departments(dept_id);

ALTER TABLE employees
ADD CONSTRAINT unique_emp_name UNIQUE(emp_name);

ALTER TABLE employees
ADD CONSTRAINT check_salary CHECK (salary > 0);

ALTER TABLE employees
DROP CONSTRAINT fk_dept;

ALTER TABLE employees
ALTER COLUMN salary SET DEFAULT 30000;

ALTER TABLE employees
ALTER COLUMN salary DROP DEFAULT;

ALTER TABLE employees
RENAME COLUMN emp_name TO employee_name;

ALTER TABLE employees
RENAME TO staff;

DROP TABLE staff;