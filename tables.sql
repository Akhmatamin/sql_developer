CREATE TABLE persons (
    person_id      VARCHAR(50) PRIMARY KEY,
    name           VARCHAR(255)
);

CREATE TABLE titles (
    id                INT PRIMARY KEY,
    show_id           VARCHAR(50),
    title             VARCHAR(500),
    type              VARCHAR(20),
    description       TEXT,
    release_year      INT,
    date_added        DATE,
    age_certification VARCHAR(20),
    runtime           INT,
    seasons           INT,
    imdb_id           VARCHAR(50),
    imdb_score        DECIMAL(3,1),
    imdb_votes        INT,
    tmdb_popularity   DECIMAL(10,4),
    tmdb_score        DECIMAL(3,1)
);


CREATE TABLE genres (
    genre_id   INT PRIMARY KEY,
    name       VARCHAR(150)
);


CREATE TABLE title_genres (
    id        INT PRIMARY KEY,
    title_id  INT REFERENCES titles(id),
    genre_id  INT REFERENCES genres(genre_id)
);

CREATE TABLE countries (
    country_id  INT PRIMARY KEY,
    name        VARCHAR(150)
);


CREATE TABLE title_countries (
    id         INT PRIMARY KEY,
    title_id   INT REFERENCES titles(id),
    country_id INT REFERENCES countries(country_id)
);


CREATE TABLE credits (
    credit_id     INT PRIMARY KEY,
    title_id      INT REFERENCES titles(id),
    person_id     VARCHAR(50) REFERENCES persons(person_id),
    role          VARCHAR(50),
    character_name VARCHAR(500)
);
