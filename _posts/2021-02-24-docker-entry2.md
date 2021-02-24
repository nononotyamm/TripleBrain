---
layout: post
title: Docker入門２
tags: docker
categories: docker
publish: false
---


* TOC
{:toc}

Author：Non

---

# Dockerでブログ環境を構築

今回は[前回][docker-entry1]の復習も兼ねてDockerを使用してこのブログのコンテナ(とコンテナイメージ)を作成してみる。

<br>

## Dockerコンテナ・イメージの作成

とりあえず、ベースとしてUbuntuのコンテナイメージをPull。（筆者がこのブログをJekyllで立ち上げるときはホストOSがUbuntuのマシンを使用することが多いのでUbuntuにしました。）

```
docker pull ubuntu
```

出力
```
Using default tag: latest
latest: Pulling from library/ubuntu
83ee3a23efb7: Pull complete 
db98fc6f11f0: Pull complete 
f611acd52c6c: Pull complete 
Digest: sha256:703218c0465075f4425e58fac086e09e1de5c340b12976ab9eb8ad26615c3715
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
```

そしてUbuntuを対話モードで立ち上げる。

```
docker run -it ubuntu
```

一応、アップデートとアップグレードをしておく

```
apt-get update
apt-get upgrade
```

そして、このブログを立ち上げるのに必要なものをインストール

```
apt-get -y install git gcc g++ make zlib1g-dev ruby ruby-dev
```

```
gem install jekyll bundler
gem install github-pages
```

ここで一旦、コンテナから出る。

別のターミナルで

```
docker ps
```

でコンテナIDを確認後（今回は`c0c7f49bd594`でした。）

```
docker stop c0
```

でUbuntuを閉じる。

そして今回はこのイメージをDockerhub（GithubのDockerイメージ版）に上げることにする。

＊ここではDockerhubのアカウントの作成等は説明しないので他の解説サイトを参照されたい。

では、最初に先ほど作成したコンテナを新規のイメージとしてCommitする。

```
docker commit -m "create TripleBrain docker image" c0 triplebrain
```

ここで`-m`オプションはGithubのコミットと同様、コミットする際にコメントをつけてコミットするオプションである。（明らかではあるがダブルコートの部分がコメントである。）

また、コメントに続く`c0`がイメージにしたいコンテナのID、`tiplebrain`というのが設定したいイメージの名前である。

完了したら`docker images`で確認してみると

出力

```
REPOSITORY    TAG       IMAGE ID       CREATED          SIZE
triplebrain   latest    482223e7543b   23 seconds ago   433MB
ubuntu        latest    f63181f19b2f   4 weeks ago      72.9MB
```

となっていて新規に`triplebrain`というイメージが作成できていることがわかる。

ここで、一旦、上げるイメージのヒストリーを確認してみる。

```
docker history triplebrain:latest
```

出力

```
IMAGE          CREATED         CREATED BY                                      SIZE      COMMENT
482223e7543b   2 minutes ago   /bin/bash                                       360MB     create TripleBrain docker image
f63181f19b2f   4 weeks ago     /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B        
<missing>      4 weeks ago     /bin/sh -c mkdir -p /run/systemd && echo 'do…   7B        
<missing>      4 weeks ago     /bin/sh -c [ -z "$(apt-get indextargets)" ]     0B        
<missing>      4 weeks ago     /bin/sh -c set -xe   && echo '#!/bin/sh' > /…   811B      
<missing>      4 weeks ago     /bin/sh -c #(nop) ADD file:2a90223d9f00d31e3…   72.9MB  
```

実際に上げる前にイメージにタグをつける必要がある。

タグをつけるには

```
docker tag 48 arinie/triplebrain:test
```

を実行する。

この`48`がイメージID（今回の場合は正確には`482223e7543b`）、`arinie`というのがDockerhubのアカウント名、`triplebrain`がイメージの名前、`test`がタグ名

となっている。

では、自分のDockerhubリポジトリにPushしてみる。

```
docker push arinie/triplebrain:test 
```

＊この操作はコマンドライン上で`docker login`してから行うこと。

出力

```
The push refers to repository [docker.io/arinie/triplebrain]
ce6306baf06e: Pushed 
02473afd360b: Mounted from library/ubuntu 
dbf2c0f42a39: Mounted from library/ubuntu 
9f32931c9d28: Mounted from library/ubuntu 
test: digest: sha256:672eb2c489f307dadc98e6e032b44ff04afb1305c5a605bbeed1364cb27e6776 size: 1156
```

今回作成したイメージ：<a href="https://hub.docker.com/repository/docker/arinie/triplebrain" target="_blank">DockerHub</a>


[docker-entry1]:{{"/docker/docker-enrty1/"|prepend:site.url}}