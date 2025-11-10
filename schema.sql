/*
 A raw sql schema of the students table for postgres
 */
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    enrollment_date DATE NOT NULL
);

/*
 (C) add student
 */
INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ("Thomas", "Selwyn", "thomas@selwyn.tech", "2020-09-01")

/*
 (R) get all students
 */
SELECT * FROM students;
/* get single student */
SELECT * FROM students WHERE email = 'thomas@selwyn.tech';

/*
 (U) update student email
 */
UPDATE students SET email = 'john.doe2@example.com' WHERE student_id = 1;

/*
 (D) delete student
 */
DELETE FROM students WHERE student_id = 1;
