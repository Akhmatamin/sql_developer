from faker import Faker
import random
from datetime import timedelta

fake = Faker()
Faker.seed(1)

NUM_TITLES = 1500
NUM_PERSONS = 1500
NUM_CREDITS = 1500
NUM_LINKS = 1500   

GENRES = [
    "Drama", "Comedy", "Action", "Thriller", "Horror", "Romance", "Sci-Fi",
    "Fantasy", "Crime", "Adventure", "Animation", "Family", "Biography",
    "Documentary", "Mystery", "War", "History", "Western", "Musical",
    "Sport", "Short", "Reality", "Talk Show", "Film-Noir"
]


COUNTRIES = [fake.country() for _ in range(150)]

sql = []



sql.append("-- GENRES")
for i, g in enumerate(GENRES, start=1):
    sql.append(f"INSERT INTO genres (genre_id, name) VALUES ({i}, '{g}');")


sql.append("\n-- COUNTRIES")
for i, c in enumerate(COUNTRIES, start=1):
    name = c.replace("'", "''")
    sql.append(f"INSERT INTO countries (country_id, name) VALUES ({i}, '{name}');")


sql.append("\n-- PERSONS")
for i in range(NUM_PERSONS):
    pid = f"P{i+1}"
    name = fake.name().replace("'", "''")
    sql.append(f"INSERT INTO persons (person_id, name) VALUES ('{pid}', '{name}');")



sql.append("\n-- TITLES")
for i in range(NUM_TITLES):
    tid = i + 1
    show_id = f"SH{tid}"
    title = fake.sentence(nb_words=4).replace("'", "''")
    description = fake.text(max_nb_chars=120).replace("'", "''")
    type_ = random.choice(["Movie", "TV Show"])
    release_year = random.randint(1980, 2024)
    date_added = fake.date_between(start_date="-5y", end_date="today")
    age_cert = random.choice(["TV-Y", "TV-G", "PG", "PG-13", "R", "TV-MA", None])
    runtime = random.randint(30, 150) if type_ == "Movie" else None
    seasons = random.randint(1, 8) if type_ == "TV Show" else None
    imdb_id = f"tt{random.randint(1000000, 9999999)}"
    imdb_score = round(random.uniform(1, 10), 1)
    imdb_votes = random.randint(1000, 500000)
    tmdb_popularity = round(random.uniform(0.1, 500.0), 4)
    tmdb_score = round(random.uniform(1, 10), 1)

    sql.append(f"""
INSERT INTO titles (
    id, show_id, title, type, description, release_year,
    date_added, age_certification, runtime, seasons,
    imdb_id, imdb_score, imdb_votes, tmdb_popularity, tmdb_score
) VALUES (
    {tid}, '{show_id}', '{title}', '{type_}', '{description}',
    {release_year}, '{date_added}', '{age_cert}',
    {runtime if runtime else 'NULL'},
    {seasons if seasons else 'NULL'},
    '{imdb_id}', {imdb_score}, {imdb_votes}, {tmdb_popularity}, {tmdb_score}
);
""")


sql.append("\n-- TITLE_GENRES")
for i in range(NUM_LINKS):
    genre_id = random.randint(1, len(GENRES))
    title_id = random.randint(1, NUM_TITLES)
    sql.append(f"INSERT INTO title_genres (id, title_id, genre_id) VALUES ({i+1}, {title_id}, {genre_id});")



sql.append("\n-- TITLE_COUNTRIES")
for i in range(NUM_LINKS):
    country_id = random.randint(1, 150)
    title_id = random.randint(1, NUM_TITLES)
    sql.append(f"INSERT INTO title_countries (id, title_id, country_id) VALUES ({i+1}, {title_id}, {country_id});")



sql.append("\n-- CREDITS")
for i in range(NUM_CREDITS):
    credit_id = i + 1
    title_id = random.randint(1, NUM_TITLES)
    person_id = f"P{random.randint(1, NUM_PERSONS)}"
    role = random.choice(["Actor", "Director", "Writer"])
    character = fake.first_name()

    sql.append(f"""
INSERT INTO credits (credit_id, title_id, person_id, role, character_name)
VALUES ({credit_id}, {title_id}, '{person_id}', '{role}', '{character}');
""")



with open("insert_data.sql", "w", encoding="utf-8") as f:
    f.write("\n".join(sql))

print("Файл insert_data.sql создан!")

