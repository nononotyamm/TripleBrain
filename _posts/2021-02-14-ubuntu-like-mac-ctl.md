---
layout: post
title: UbuntuのコントロールをMacライクにする
tags: unix linux ubuntu gnome macos
categories: linux 
---


* TOC
{:toc}

Author: Non

# 環境

Ubuntu 20.04 LTS

<br>

# やりたいこと

ここでは、Macのコントロール、とくにSuuperキーの位置やmission control、SpotlightなどをUbuntuでもできるようにする。

つまり

- left Super Keyとleft Ctrl Keyの入れ替え（MacにWinキーボードをつないだときの挙動と同じにするため）
- キーボードのスペースキーの左右にある変換・無変換キーで英字入力、日本語入力を可能にする
- Albertを導入することでSpotlightのようなCommand+Spaceでコマンドを入力できるようにする
- mission controlのような挙動を可能にする（Ctrl+↑でアプリケーションを一覧させる）

ということをやる。

<br>

---

# Super入れ替え

```
sudo apt-get install gnome-tweak-tool
```

でgnomeのtweaksをいれて起動

「キーボードとマウス」→「追加のレイアウトオプション」→「Ctrlキーの位置」→「Swap Left Win key with Left Ctrl key」

で入れ替える。

参考：<a href="https://qiita.com/teppeitherock/items/113be4c5270f1d5e2f4c" target="_blank">UbuntuでキーボードのCtrlの位置を変える</a>

<br>

# 変換・無変換割当

Ubuntuのステータスバーのキーボード欄で

「ツール」→「プロパティ」→「一般」→「キー設定」→「キー設定の選択」→「編集」

で

1. 「入力キー」がHenkana、Muhenkanのものをすべて削除
2. 「コマンド」が「IMEを無効化」のものすべての「入力キー」をMuhenkanに
3. 「コマンド」が「IMEを有効化」のものすべての「入力キー」をHenkanに

参考：<a href="https://yaruki-strong-zero.hatenablog.jp/entry/ubuntu_switching_ja_ime" target="_blank">Ubuntuにてmacの英数・かなキーで日本語入力切り替えするための設定方法</a>

<br>

# Albertをいれる

ターミナルで

```
echo 'deb http://download.opensuse.org/repositories/home:/manuelschneid3r/xUbuntu_20.04/ /' | sudo tee /etc/apt/sources.list.d/home:manuelschneid3r.list
```

を実行。次に

```
curl -fsSL https://download.opensuse.org/repositories/home:manuelschneid3r/xUbuntu_20.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/home_manuelschneid3r.gpg > /dev/null
```

そして

```
sudo apt-get update
sudo apt-get install albert
```

参考：<a href="https://wonwon-eater.com/ubuntu-albert/" target="_blank">【サクッと解決】Ubuntu ランチャーアプリにAlbertをインストールする</a>

完了したらAlbertを起動して設定する。

設定はデフォルトのままだとなにもできないので書きを参考に自分の好みの設定に変更する。

参考：<a href="https://ich.hatenadiary.com/entry/launcher_on_ubuntu" target="_blank">Linuxでアプリの起動やファイル検索などができる軽快なランチャー"Albert"</a>

<br>

# mission control

ミッションコントロールのアクティブ画面の表示のみを再現する（その他のミッションコントロールの再現は難しいか不可能のため）。

設定は簡単で

「設定」→「キーボードショートカット」→「アクティビティ画面を表示する」

で`Super+Up`を設定する。また２個目の「アクティビティ画面を表示する」は無効にしておく。

＊MacのSpacesはUbuntuのワークスペースに対応していると思われるが、挙動がかなり違うためUbuntuでは仮想デスクトップのような機能はしようしないようにした。

<br>

# 参考

これからやってみたいこと：<a href="https://tech.recruit-mp.co.jp/dev-tools/good-bye-mac/" target="_blank">仕事用マシンをMacBookProからUbuntuデスクトップに乗り換えて1ヶ月運用してみました
</a>