CREATE ROLE airflow WITH LOGIN PASSWORD 'airflow';

CREATE TABLE pollution_data (
    data_id INT PRIMARY KEY,
    pollution_value FLOAT,
    station_name VARCHAR(255),
    province_name VARCHAR(255),
    gegr_lat FLOAT,
    gegr_lon FLOAT
);