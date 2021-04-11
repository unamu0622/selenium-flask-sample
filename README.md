# chrome-driver-manager-test

## 実行手順
```console
docker build -t chrome-driver-manager-test .
docker run --name chrome-driver-manager-test -it --rm chrome-driver-manager-test:latest
```

## 開発手順
```console
docker run -itd python:3.8-buster /bin/sh
docker exec -it b4348814affb94d642cca9289d3e001ec1184b80c1fe0c20944ba5b4388f43a3 /bin/sh
```

## 参考
- https://qiita.com/memakura/items/20a02161fa7e18d8a693
- https://q-three.com/archives/1031
- https://future-architect.github.io/articles/20200513/