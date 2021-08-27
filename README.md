# analyze-that

## Levantar docker compose

<code>docker-compose up -d --build</code>


## Bajar docker compose

<code>docker-compose down</code>


## Conectar con la base de datos

<code>docker-compose exec analyze_db psql -h localhost -U analyze_db_user --dbname=analyze</code>

## pgAdmin

- http://localhost
- user: analyze@that.com
- pass: admin1234

