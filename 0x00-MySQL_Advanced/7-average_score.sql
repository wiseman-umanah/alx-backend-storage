-- Write a SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student.
DELIMITER $

CREATE PROCEDURE ComputeAverageScoreForUser(IN p_user_id INT)
BEGIN
    SELECT u.id AS id, u.name AS name, AVG(c.score) AS average_score
    FROM 
        corrections c
    JOIN 
        users u ON c.user_id = u.id
    WHERE
        c.user_id = p_user_id
    GROUP BY 
        u.id, u.name;
END
$

DELIMITER ;
