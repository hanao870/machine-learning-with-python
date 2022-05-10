# Python ではじめる機械学習

書籍 [Python ではじめる機械学習](https://www.oreilly.co.jp/books/9784873117980/) の写経リポジトリ

## 開発環境

以下の環境にて動作確認を実施

* Windows 10 pro Version 21H2
* Docker Desktop for Windows
  * Version: `4.8.1`
* Python Docker Official Image
  * `python:3.10.4`
* `Visual Studio Code`
  * 拡張機能: `Remote - Container`

`Visual Studio Code` の `Remote - Container` を用いてコンテナ内で実施

以下の `Visual Studio Code` の拡張機能がコンテナ内にインストールされる

* `Python`
* `Pylance`
* `markdownlint`
* `Git history`
* `autoDocstring - Python Docstring Generator`
* `indent-rainbow`

## Python の linter / formatter

以下の linter / formatter を使用

* linter
  * [flake8](https://github.com/PyCQA/flake8)
  * [bandit](https://github.com/PyCQA/bandit)
  * [pydocstyle](https://github.com/PyCQA/pydocstyle)
  * [mypy](https://github.com/python/mypy)
* formatter
  * [black](https://github.com/psf/black)
  * [isort](https://github.com/PyCQA/isort)

Ctrl + S でファイルを保存すると formatter が実行されるよう、コンテナ内の `Visual Studio Code` の設定を変更している
