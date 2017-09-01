#前処理ツール
written by @kakira9618

## AR.sh
引数で指定したWRからARを抜き出し、標準出力に表示する。

### 使い方
```bash
./AR.sh xxx.mes.utf
```

## detect_AR.sh
このシェルスクリプトが置いてあるディレクトリ内にあるWR全てについて、
ARを抜き出し、標準出力に表示する。
```bash
./detect.sh
```

## parseWR.py
引数で指定したWRを解析し、jsonに変換して表示する。
```bash
./parseWR.py xxx.mes.utf
```

## marge.py
parseWR.pyで出力されたjsonファイルを結合する。
調査するディレクトリはソースコード内で指定している。
```bash
./marge.py
```
