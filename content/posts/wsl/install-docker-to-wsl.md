---
title: "Install Docker to WSL"
description: ""
date: 2025-03-26T08:00:00+09:00
lastmod:
draft: false
---

## Prerequisites

- Install WSL2 and Ubuntu 22.04 to Windows (see [my previous post](https://tsuji.tech/install-uninstall-wsl/))

## Install Docker to WSL

Install Docker to WSL (see [Install Docker Engine on Ubuntu - Docker Docs](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)):

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Check docker command is valid:

```bash
sudo docker run hello-world
```

## Manage Docker as a non-root user

Check docker group is existing (see [Linux post-installation steps for Docker Engine - Docker Docs](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)):

```bash
grep docker /etc/group

# If there is docker group, following response will be shown:
# docker:x:999:

# If not, add docker group:
sudo groupadd docker
```

Add my user to the docker group:

```bash
sudo usermod -aG docker $USER
```

Reboot WSL on PowerShell (not on WSL):

```bash
wsl --shutdown
```

Activate the docker group on WSL:

```bash
newgrp docker
```

Then, check you can run docker command without sudo:

```bash
docker run hello-world
```

## References

- [Install Docker Engine on Ubuntu - Docker Docs](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)
- [Linux post-installation steps for Docker Engine - Docker Docs](https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user)
