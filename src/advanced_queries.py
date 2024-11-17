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