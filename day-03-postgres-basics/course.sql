-- Day 03: my own learning tracks
-- Run from repo root on the Mac:
--   docker exec -i fastapi-postgres psql -U postgres -d mydatabase < day-03-postgres-basics/course.sql

DROP TABLE IF EXISTS course;

CREATE TABLE course (
    id             SERIAL PRIMARY KEY,
    name           VARCHAR NOT NULL,
    instructor     VARCHAR NOT NULL,
    duration_days  INTEGER NOT NULL
);

INSERT INTO course (name, instructor, duration_days)
VALUES ('10 Days of FastAPI', 'STUDY MART (Abu Noman Bashar)', 10),
       ('90 Days of DevOps', 'TrainWithShubham', 90);

-- Add a column later; DEFAULT fills the old rows so NOT NULL doesn't break
ALTER TABLE course ADD COLUMN website TEXT NOT NULL DEFAULT 'N/A';

UPDATE course
SET website = 'https://github.com/Fahim017803/10-days-of-fastapi'
WHERE name = '10 Days of FastAPI';

SELECT * FROM course;