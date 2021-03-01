---
layout: post
title: pyenvとvenvでの環境構築 # ページタイトル
tags: pyenv venv python # タグ
categories: python # カテゴリ. AtCoderの解説記事は atcoder で.
published: true # ここは必ずtrueにしてください.
---


* TOC
{:toc}

Author: Non　<!-- 自分の名前 -->

<!-- ↓↓↓↓↓ 記事内容 ↓↓↓↓↓ -->

## やりたいこと

前のこの[記事]:[venv]ではvenvを使用してシステムに入っているPythonでの独立したライブラリ環境を構築することをした。

しかし、これはあくまでシステムに入っているバージョンのPythonでの環境であり、venvのみでは複数のPythonバージョンでの独立したライブラリ環境を構築することはできない。

そこで、今回はpyenvというものとvenvを組み合わせることでマルチバージョンのPythonでそれぞれ独立したライブラリ環境の構築を行う。

## pyenv is 何

pyenvとは上記で説明したとおり、マルチバージョンのPython環境を構築できるものである。

ここで注意しておきたいことはWindowsなどのOSでは使う必要がないということである。

【参考】

> <a href="https://qiita.com/shibukawa/items/0daab479a2fd2cb8a0e7#%E5%89%8D%E6%8F%90%E7%9F%A5%E8%AD%98" target="_blank">pyenvが必要かどうかフローチャート</a>

ちなみに筆者のデスクトップ環境はUbuntu。

そして自然言語処理モデルを回す関係でTensorflowのバージョンなど参考記事によって異なってくるので今回、pyenvとvenvを使用した環境構築を行う。

また、必要な場合はpyenv自体はGitから落としてくるのでGitの設定など終わらせておくこと。

## pyenvをインストール

ここでは上記のpyenvを必要とするOSがLinuxなどに限られる関係からLinuxを前提とした解説を行う。

まず、Homeにpyenvを隠しフォルダとして落とす。

コマンド

```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

そして、環境変数設定を.bashrcなどにかいておく。

以下を.bash_profileや.bashrcに書く。

```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

```

そしてターミナルを立ち上げ直すか、`source ~/.bashrc`で.bashrcを実行して

コマンド

```
pyenv --version
```

で認識されていればおｋ。

## 任意のバージョンのPythonをインストール

ここでは、pyenvを使用して任意のバージョンのPythonをローカルに落とす作業を解説する。

まずは、現在インストールできるPythonなどのバージョンを確認する。

コマンド

```
pyenv install --list
```

確認して自分が入れたいバージョンがあったらインストールが可能である。

次に実際にPythonを落とす。

たとえば、`3.8.3`のPythonをローカルにインストールしたい場合、

コマンド

```
pyenv install 3.8.3
```

でできる。

ここで、インストールした時点では落としてきたバージョンのPythonは有効化されていないことに注意されたい。

## 落としてきたpythonを有効化

無事、自分が落としてきた任意のバージョンのPythonがインストールできているかどうかは

コマンド

```
pyenv versions
```

で確認できる。無事確認ができたら

コマンド（ここでは例として3.8.3を有効化）

```
pyenv shell 3.8.3
```

で有効化できる。

コマンド

```
python3 --version
```

で自分の有効化したバージョン担っていればおｋ。

## venvを使用して独立環境構築

前述した手順で有効化できたらそのまま[前回][venv]でやったように仮想環境を構築する。

コマンド

```
python3 -m venv 任意のディレクトリ
```

で作成して

```
source 任意のディレクトリ/bin/activate
```

で環境をアクティベート。環境に入る。

## インストールしたバージョンを削除

pyenvを使用してインストールした任意のバージョンのPythonが不要になり、削除したい場合

コマンド

```
pyenv uninstall 削除したいバージョン
```

とすれば削除できる。




[venv]:{{"/python/python-venv/"|prepend:site.url}}