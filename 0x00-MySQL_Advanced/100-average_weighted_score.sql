-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the overall score for a student.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
    SELECT 
        C.user_id, 
        U.name, 
        SUM(C.score * P.weight) / SUM(P.weight) AS average_score 
    FROM 
        corrections AS C
    JOIN 
        users AS U ON C.user_id = U.id
    JOIN 
        projects AS P ON C.project_id = P.id
    WHERE 
        C.user_id = user_id
    GROUP BY 
        C.user_id, U.name;
END
$$

DELIMITER ;
