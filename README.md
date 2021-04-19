# analyze-that

## Levantar docker compose
docker-compose up -d --build

## Bajar docker compose
docker-compose down

## Conectar con la base de datos
docker-compose exec analyze_db psql -h localhost -U analyze_db_user --dbname=analyze
