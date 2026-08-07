SELECT
    c.competition_name,
    c.competition_type,
    c.gender,
    cat.category_name
FROM competitions c
JOIN categories cat
    ON c.category_id = cat.category_id;

SELECT
    cat.category_name,
    COUNT(c.competition_id) AS competition_count
FROM categories cat
LEFT JOIN competitions c
    ON cat.category_id = c.category_id
GROUP BY cat.category_id, cat.category_name
ORDER BY competition_count DESC;    

SELECT *
FROM competitions
WHERE LOWER(competition_type) = 'doubles';


SELECT *
FROM competitions
WHERE parent_id IS NULL;


SELECT
    parent.competition_name AS parent_competition,
    child.competition_name AS sub_competition
FROM competitions child
JOIN competitions parent
    ON child.parent_id = parent.competition_id;


SELECT
    v.venue_name,
    v.city_name,
    v.country_name,
    v.timezone,
    c.complex_name
FROM venues v
JOIN complexes c
    ON v.complex_id = c.complex_id;


SELECT
    c.name,
    c.country,
    r.rank_position,
    r.points
FROM competitor_rankings r
JOIN competitors c
    ON r.competitor_id = c.competitor_id
WHERE r.rank_position <= 5
ORDER BY r.rank_position;


SELECT
    c.name,
    r.rank_position,
    r.movement,
    r.points
FROM competitor_rankings r
JOIN competitors c
    ON r.competitor_id = c.competitor_id
WHERE r.movement = 0;