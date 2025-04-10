---
title: 'Install TeX Live in Ubuntu'
description: ''
date: 2025-04-10T21:00:00+09:00
lastmod: 
draft: false
---

## Install TeX Live

```bash
apt-get install -y cpanminus
cpan install Pod::Usage -y

wget https://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz

tar zxf install-tl-unx.tar.gz
cd install-tl-*
sudo perl ./install-tl
```

## Reference

- [Installing TeX Live over the Internet - tug.org](https://tug.org/texlive/acquire-netinstall.html)
- [TeX Live - Quick install for Unix - tug.org](https://tug.org/texlive/quickinstall.html)
