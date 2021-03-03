# -*- coding: utf-8 -*-
# 標準入力からヘッダー有りカンマ区切りのCSVを読み込み
# コマンドライン引数に指定した項目をカラム名とみなし
# その順番でヘッダーになるように再構成して標準出力へ書き出す
import csv
import sys

header = tuple([arg for i, arg in enumerate(sys.argv) if i > 0])
cin = csv.DictReader(sys.stdin)
cout = csv.writer(sys.stdout, dialect='unix')
isFirstRow = True
for row in cin :
    if isFirstRow :
        isFirstRow = False
        for col in header :
            assert col in row, "Column '{}' is NOT in row {}".format(col, row.keys())

        cout.writerow(header)

    cout.writerow([row[col] for col in header])
