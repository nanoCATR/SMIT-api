# Methods
## rate
Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`/rate/` | GET | READ | Получить всё из таблицы InsuranceRate
`/rate/load-rates` | POST | CREATE | Загрузить тарифы
`/rate/insurance`| POST | READ | Узнать стоимость страхования

# Build and run docker containers
Зайти в папку проекта, написать следующую команду:
```sh
docker-compose up -d
```

# Swagger docs url
`127.0.0.1/docs`
