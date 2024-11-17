from db import connect_to_database
        
connection = connect_to_database();


def user_performance(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        query = """WITH user_skills AS (
    SELECT user_id, COUNT(skill_id) AS skill_count
    FROM user_skill
    GROUP BY user_id
),
user_posts AS (
    SELECT user_id, COUNT(*) AS post_count
    FROM post
    GROUP BY user_id
),
user_stats AS (
    SELECT 
        u.user_id,
        u.name,
        u.location_country,
        COALESCE(us.skill_count, 0) AS skill_count,
        COALESCE(up.post_count, 0) AS post_count
    FROM user u
    LEFT JOIN user_skills us ON u.user_id = us.user_id
    LEFT JOIN user_posts up ON u.user_id = up.user_id
)
SELECT 
    us.user_id,
    us.name,
    us.location_country,
    us.skill_count,
    us.post_count,
    RANK() OVER (ORDER BY us.skill_count DESC, us.post_count DESC) AS overall_rank,
    RANK() OVER (PARTITION BY us.location_country ORDER BY us.skill_count DESC, us.post_count DESC) AS country_rank,
    CASE 
        WHEN us.skill_count > (SELECT AVG(skill_count) FROM user_stats)
        AND us.post_count > (SELECT AVG(post_count) FROM user_stats)
        THEN 'High Performer'
        ELSE 'Average Performer'
    END AS performance_category
FROM user_stats us
WHERE us.user_id IN (
    SELECT DISTINCT user_id 
    FROM experience 
    WHERE institution_id IN (
        SELECT institution_id 
        FROM institution 
        WHERE industry = 'Technology'
    )
)
ORDER BY overall_rank, country_rank;"""
        cursor.execute(query)
        results = cursor.fetchall()
        
        if results:
            return {"status": "success", "user_performance": results}
        else:
            return {"status": "error", "message": "No user performance data found"}
    except Exception as error:
        return {"status": "error", "message": str(error)};
    finally:
        cursor.close()
        

def analyze_institution_growth(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        query = """WITH institution_growth AS (
    SELECT
        i.institution_id,
        i.name,
        e.start,
        COUNT(*) OVER (PARTITION BY i.institution_id ORDER BY e.start) AS employee_count
    FROM institution i
    JOIN experience e ON i.institution_id = e.institution_id
    )
    SELECT
        name,
        start,
        employee_count,
        LAG(employee_count) OVER (PARTITION BY institution_id ORDER BY start) AS previous_count,
        employee_count - LAG(employee_count) OVER (PARTITION BY institution_id ORDER BY start) AS growth
    FROM institution_growth
    ORDER BY name, start;"""
        cursor.execute(query)
        results = cursor.fetchall()
        
        if results:
            return {"status": "success", "institution_growth": results}
        else:
            return {"status": "error", "message": "No institution growth data found"}
    except Exception as error:
        return {"status": "error", "message": str(error)}
    finally:
        cursor.close()

def getJobRecommendation(connection):
    try:
        cursor = connection.cursor(dictionary=True)
        query = """SELECT 
    j.job_id,
    j.job_title,
    j.description,
    j.type,
    i.name AS institution_name,
    CONCAT(i.location_city, ', ', i.location_state, ', ', i.location_country) AS institution_location,
    COUNT(DISTINCT s.skill_id) AS matching_skills
FROM 
    job j
JOIN institution i ON j.institution_id = i.institution_id
JOIN user_skill us ON us.user_id = 3
JOIN skill s ON s.skill_id = us.skill_id
WHERE 
    LOWER(j.description) LIKE CONCAT('%', LOWER(s.skill_name), '%')
GROUP BY 
    j.job_id, j.job_title, j.description, j.type, i.name, 
    i.location_city, i.location_state, i.location_country
ORDER BY 
    matching_skills DESC, j.job_id
LIMIT 10;"""
        cursor.execute(query)
        results = cursor.fetchall()
        
        if results:
            return {"status": "success", "job_recommendation": results}
        else:
            return {"status": "error", "message": "No job recommendation data found"}
    except Exception as error:
        return {"status": "error", "message": str(error)}
    finally:
        cursor.close()
    