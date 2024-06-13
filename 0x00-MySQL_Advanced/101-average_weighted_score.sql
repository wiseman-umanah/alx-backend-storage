-- SQL script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the overall score for a student.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    SELECT 
        C.user_id, 
        U.name, 
        CAST(SUM(C.score * P.weight) / SUM(P.weight) AS DECIMAL(10, 4)) AS average_score 
    FROM 
        corrections AS C
    JOIN 
        users AS U ON C.user_id = U.id
    JOIN 
        projects AS P ON C.project_id = P.id
    WHERE 
        C.user_id = U.id
    GROUP BY 
        C.user_id, U.name;
END
$$

DELIMITER ;
