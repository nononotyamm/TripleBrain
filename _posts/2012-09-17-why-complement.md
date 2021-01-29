---
layout: post
title: このサイトでの投稿について
tags: markdown
categories: common
---

このサイトでの投稿はMarkdownでなされ、各Markdownページは`YYYY-MM-DD-ページタイトル.md`というファイルである。
（YYYYは投稿年、MM、DDは投稿月と投稿日。ページタイトルは英語）

mdファイルのはじめに
```
---
layout: post
title: このサイトでの投稿について
tags: markdown
categories: markdown
---
```
を書かなければならない。（上のはこのページのもの）

```
---
layout: post
title: VIM
tags: VIM Linux
categories: special
published: false
---
```
のように`published: false`とすれば公開されない（下書き状態）。

ページのURLは`ベースURL/上で設定したcategories/mdファイル名で設定したページタイトル/`となるので、***ページタイトルは重複しないようにしなければならない。***

---

数字や式は
```
数字
`3.141592653`
式
`x^2+y^2=1`
```
とすることで
数字
`3.141592653`
式
`x^2+y^2=1`
となる。

また、

---

のような区切り線は
```
---
```
でできる。



