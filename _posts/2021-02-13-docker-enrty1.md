---
layout: post
title: Docker入門１
tags: docker
categories: docker
---


* TOC
{:toc}

Author：Non

# Dockerとは

Dockerとは何か。

一言で言えばDockerはコンテナ技術を使用したOSエミュレータである。

Dockerは今日のインフラを幅広く支える技術である。

<br>

## Dockerが役立つ時

例えば、A君がサーバーを構築したいとする。

A君はお金や過去にサーバーを自前で用意した経験がないので、レンタルサーバーを借りることにした。また、できるだけ安く済ませたいのでWindowsサーバーではなく、無料のOSであるCentOS（Linux）サーバーを借りることにした。

しかし、A君のパソコンはUbuntu（Linux）なので、例えA君のローカルの環境でプログラムを完成させても、おそらくCentOSレンタルサーバーでは数多くの不具合、エラーが起きることが予想される。

そこで、ローカルの環境をCentOSにしたいと考えるのは当然の発想である。

ローカルでCentOSを回すには

- 実際にパソコンを新調して、CentOSをインストール。レンタルサーバーと同じ環境をハードウェアから構築する。

- A君の持っているパソコンにVMWareのような仮想OSソフトを入れて、Ubuntu上でCentOSをエミュレートする。

などが考えられる。

前者はパソコンを新調するコストもかかるし、OSインストールなどかなり面倒である。それに比べて後者は比較的簡単で、無料で行うことができるがVMWareが重いなどの問題が出てくるかもしれない。

そこで、VMWareではなく、Docker（コンテナ）を使用することで軽い動作で違うOSをエミュレートすることができるのだ。

<br>

## なぜ、軽い

なぜ軽く動作させることが出来のかと言うと、DockerはホストOS（自分のマシンのOS）がLinuxの場合、Linuxカーネル（Linuxシステムの核）を共有して動かすからである。

ホストOSがLinuxではない人は恩恵が受けられないと思うかもしれないが、ホストOSがLinuxではなくてもDockerクライアントをインストールした際に、Linuxカーネルがインストールされるため、複数のLinuxをDockerコンテナをインストールする際にはVMWareで同等のことを行うより遥かに軽い動作で実現することができる。

<br>

# Dockerイメージを取得して動かしてみる

<br>

公開されているDockerイメージを取得し、ローカルのDockerクライアントで動かしてみる。

今回は例としてLinuxディストリビューションの一つであるUbuntuを取得し、動かす。

<br>

## イメージの取得

まず、Ubuntuの取得は

```
docker pull ubuntu
```

でできる。

出力（Authorは何回かやったので出力が違うかも、ごめんなさい）
```
Using default tag: latest
latest: Pulling from library/ubuntu
83ee3a23efb7: Already exists
db98fc6f11f0: Already exists
f611acd52c6c: Already exists
Digest: sha256:703218c0465075f4425e58fac086e09e1de5c340b12976ab9eb8ad26615c3715
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
```

<br>

ちゃんとイメージを落としてこれてるかどうか確認

```
docker images
```

出力
```
REPOSITORY                   TAG       IMAGE ID       CREATED       SIZE
ubuntu                       latest    f63181f19b2f   3 weeks ago   72.9MB
```

<br>

## コンテナを作成してみる

コンテナを作成し、接続するには`docker run`コマンドを使用する。

今回はUbuntuなので`-it`オプションをつけて、対話モードで立ち上げてみる。

```
docker run -it ubuntu
```

実行すると、Ubuntuのターミナル内に入る。試しに`ls`コマンドを打ってみる。

```
root@f938234cede6:/# ls
```

Ubuntu出力

```
bin   dev  home  lib32  libx32  mnt  proc  run   srv  tmp  var
boot  etc  lib   lib64  media   opt  root  sbin  sys  usr
```

無事、Ubuntuコンテナを起動できているようだ。

ここでは一度、Ubuntuから抜け出してホストOSに戻る。

```
root@f938234cede6:/# exit
```

出力
```
exit
```

<br>

## コンテナを確認する

起動コンテナを確認するコマンド

```
docker ps
```

を打つと、先ほどUbuntuコンテナは終了させたはずなので

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

となっているはずである。

<br>

ここで先のコマンドにオプション`-a`（Allの意）をつけると

```
docker ps -a
```

出力
```
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                     PORTS     NAMES
f938234cede6   ubuntu    "/bin/bash"   11 minutes ago   Exited (0) 6 minutes ago             funny_lumiere
```

となって停止中のコンテナが表示できた。

<br>

## 起動中のコンテナを外部から停止する

<br>

先のセクションで対話モードのUbuntu内に入って`exit`コマンドを打つことによって、Ubuntuコンテナを停止させたが

外部のターミナルからでも`docker stop`コマンドを使用すれば停止できる。

<br>

先ほど、`docker ps -a`コマンドで確認したコンテナのIDを用いて（今回の場合は`f938234cede6`)

```
docker start f938234cede6
```

を実行すると先ほど`docker run -it ubuntu`で作成したコンテナを起動できる。

ここで一度、`docker ps`で起動中のコンテナを確認すると

出力
```
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS         PORTS     NAMES
f938234cede6   ubuntu    "/bin/bash"   24 minutes ago   Up 4 seconds             funny_lumiere
```

となっているはずだ。しかし、このままでは先ほどのように対話モードでUbuntuに入ることができない。

そこで

```
docker attach f9
```

（＊`f9`というのは正確には`f938234cede6`）

を実行することで対話モードとしてUbuntuコンテナに入ることができる。

<br>

> ＊`f9`というのは正確には`f938234cede6`

＊DockerでのイメージやコンテナのIDは、このようにIDを全て打たなくても一意に決まる桁数までなら省略できる。

<br>

ここで、別のターミナルを立ち上げて

```
docker stop f9
```

とすると元のターミナルではUbuntuコンテナが終了していて

```
docker ps
```

を実行すると

```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
```

となっていて、どのコンテナも現在起動していないことがわかる。

<br>

## コンテナを削除してみる

ここではコンテナの削除の仕方を紹介する。

先ほどまで使っていた`f938234cede6`のコンテナの削除は

```
docker rm f9
```

を実行することで行うことができる。

`docker ps -a`で確認してみるとしっかりとコンテナが削除されていることがわかるはずである。

<br>

## イメージを削除する

コンテナの削除と同様にして、イメージを削除することも可能である。

先ほどまで使用していたUbuntuのイメージの削除は

```
docker rmi ubuntu
```

で行うことができる。`docker images`で確認してみるとしっかりと削除されているのかわかるはずである。

<br>

<br><br>

---

# よく出るエラー

<br>

## rmi時

```
Error response from daemon: conflict: unable to delete f63181f19b2f (cannot be forced) - image is being used by running container f6e2efc6b0b7
```

削除しようとしているイメージは起動中のコンテナで使用されている

→該当のコンテナの削除

<br>

```
Error response from daemon: conflict: unable to delete f63181f19b2f (must be forced) - image is being used by stopped container 1f04c9093d41
```

削除しようとしているイメージは停止中のコンテナで使用されている

→該当の停止中のコンテナの削除

<br>

```
Error response from daemon: conflict: unable to delete e7d08cddf791 (cannot be forced) - image has dependent child images
```

削除しようとしているイメージに依存関係がある。→依存しているイメージを削除してから削除。

＊Mac, Linuxの場合、以下のシェルスクリプトで依存関係のあるイメージを取得できる。

dependence-images.sh
```bash
for i in $(docker images -q)
do
        docker history $i | grep -q $1 && echo $i
done | sort -u
```

今回の場合の実行コマンド（e7のところは調べたいイメージID）
```
dependence-images.sh e7
```

出力（依存関係のあるイメージのIDたち）
```
d42ff4b4901d
e7d08cddf791
f6d0b4767a6c
```