---
layout: post
title: Venvについて
tags: python command
categories: python
---


* TOC
{:toc}

Author：Non

# venv入門

windowsユーザならAnacondaGUIでPythonの仮想環境を構築し、仮想環境上で様々なけしからんことを実行したことがあるだろうが、如何せんAnacondaは重いのである。

そしてMacユーザやUbuntuユーザならCUI上で仮想環境を構築して動かしたいのである。（Anacondaでもできるけど

そこで登場するのがPython付属の`venv`である。

<br>

# venvでの仮想環境の構築

venvで仮想環境を構築する場合、任意の場所でPythonカーネルフォルダを作成することになる。

よって、まずは仮想環境フォルダを作成しても構わない任意のワークディレクトリに行って

```
python3 venv 仮想環境名
```

を実行する。（仮想環境名は`.Unko`のような隠しフォルダとして作成するのが一般的である。

<br>

# venvで仮想環境を立ち上げ

先ほど作成した仮想環境を立ち上げてみよう

立ち上げるには、そのさっきのワークディレクトリで

```
source ./仮想環境名/bin/activate
```

を実行すれば良い。

```
(仮想環境名)xxx $
```
となっていたら成功である。

<br>

# venvで仮想環境から戻る

仮想環境から抜け出すには

```
deactivate
```

を実行すれば良い。

仮想環境を削除したい場合はPythonカーネルが入っているディレクトリごと削除すれば良い。