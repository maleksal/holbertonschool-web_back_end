-- lists all students with filters
DROP VIEW IF EXISTS need_meeting;
CREATE VIEW need_meeting AS
SELECT name FROM students
    WHERE score < 80
    AND last_meeting is NULL OR last_meeting < DATE_SUB(NOW(), INTERVAL 1 MONTH);