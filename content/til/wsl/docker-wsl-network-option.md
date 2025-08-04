---
title: 'Network Option for Docker in WSL'
description: ''
date: 2025-08-04T22:00:00+09:00
lastmod:
draft: false
---

## Network Option for Docker in WSL

If the network of the Docker container in WSL is so slow, the ``--network=host`` option will help:

```bash
docker run --network=host ...
```
