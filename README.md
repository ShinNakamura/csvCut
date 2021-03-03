# csvCut.py

- 標準入力からヘッダー有りカンマ区切りのCSVを読み込み
- コマンドライン引数に指定した項目をカラム名とみなし
- その順番でヘッダーになるように再構成して標準出力へ書き出す

`sample/csvCut_test.csv`

```csv
No,Name,Age
1,John,29
2,Marry,31
3,Ken,42
```

```shell
$ cat sample/csvCut_test.csv | python3 src/csvCut.py "No" "Name"
"No","Name"
"1","John"
"2","Marry"
"3","Ken"

$ cat sample/csvCut_test.csv | python3 src/csvCut.py "id" "Name"
Traceback (most recent call last):
  File "src/csvCut.py", line 16, in <module>
      assert col in row, "Column '{}' is NOT in row {}".format(col, row.keys())
AssertionError: Column 'id' is NOT in row dict_keys(['No', 'Name', 'Age'])
```
