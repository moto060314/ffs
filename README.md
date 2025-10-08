# Docker Compose の使い方

## docker-compose.yml setting

```sh
# 絶対に、PassWordを設定してください。
# Errorの原因になります。
```

## compose から import する

```sh
docker compose up
```

## compose を down する

```sh
docker compose down
```

## compose を up する

```sh
docker compose up -d
```

## mysql の操作

### in

```sh
docker exec -it my_mariadb mariadb -u root -p
```

```sh
query.sql を貼り付け。
```

### out

```sh
quit
```

# FFS SetUp

## pip install

### Windows

```sh
py -m venv .venv
```

```sh
.\.venv\Scripts\activate
```

### Mac

```sh
python3 -m venv .venv
```

```sh
. ./.venv/bin/activate
```

## Library Install

```sh
pip install -r requirements.txt
```

## Program Start

```sh
uvicorn app:asgi_app --reload
```

## Connect

```sh
http://localhost:8000
```
