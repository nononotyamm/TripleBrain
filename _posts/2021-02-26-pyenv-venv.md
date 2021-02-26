---
layout: post
title: pyenvとvenvを使用してPythonマルチバージョン環境構築 # ページタイトル
tags: pyenv venv python command # タグ
categories: python # カテゴリ. AtCoderの解説記事は atcoder で.
published: false # ここは必ずTrueにしてください.
---


* TOC
{:toc}

Author: Non　<!-- 自分の名前 -->

<!-- ↓↓↓↓↓ 記事内容 ↓↓↓↓↓ -->

# pyenvってなに

[この記事][python-venv]でvenvを使用したマルチPip環境を構築したが、これはあくまでライブラリなどのインストールを独立して行う仮想環境だった。

つまり、システムでPython3.6.3を使用していて、そこから独立したPython3.8.7の仮想環境の構築はvenvだけではできないのである。

そこで、違うPythonのバージョンのvenvで独立したPython環境を用意するためにpyenvを使用する。

<br>

単純に言えば、ローカルの環境に何個でも違うバージョンのPythonを入れられるのがpyenvである。

<br>

# pyenvをインストール

pyenvをインストールするには<a href="" target="_blank">このpyenvのGithubレポジトリ</a>をまるっとクローンし、中にあるファイルのパスを通す。





[python-venv]:{{"/python/python-venv/"|prepend:site.url}}