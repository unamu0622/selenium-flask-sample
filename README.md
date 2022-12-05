# selenium-flask-sample

## 実行手順
1. Docker コンテナの起動
```sh
docker compose up -d
```

2. logの表示
```sh
docker compose logs -ft
```

3. localhostに対してリクエスト
```sh
curl http://localhost:9090/
```

## コンテナの終了
```sh
docker compose down
```

## docker composeを使わない場合のDockerコンテナの起動
dockerを使う場合
```sh
docker build -t selenium-flask-sample .
PORT=8080 && finch run -p 9090:${PORT} -e PORT=${PORT} --name selenium-flask-sample -it --rm selenium-flask-sample:latest
```

## TODO
- seleniumのメジャーバージョンがまだ3なので4に移行
  - [webdriver-managerのREADME.md](https://github.com/SergeyPirogov/webdriver_manager#use-with-chrome)に記載