CREATE TABLE IF NOT EXISTS jobs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_type TEXT not NULL,
    job_status TEXT not NULL,
    job_date TEXT,
    job_compagny_name TEXT,
    job_name TEXT not NULL,
    job_location TEXT,
    job_description TEXT
);
