---
title: "Google Colabで特定のCUDAバージョンをインストールする"
description:
date: 2025-02-05T9:00:00+09:00
lastmod:
draft: false
---

## Google Colabで特定のCUDAバージョンをインストールする

以下のコードスニペットは、Google Colabでcuda-12.1をインストールする方法を示している。

（オプション）現在のOSバージョンを表示する。

```bash
!cat /etc/os-release

# PRETTY_NAME="Ubuntu 22.04.4 LTS"
# NAME="Ubuntu"
# VERSION_ID="22.04"
# VERSION="22.04.4 LTS (Jammy Jellyfish)"
# VERSION_CODENAME=jammy
# ID=ubuntu
# ID_LIKE=debian
# HOME_URL="https://www.ubuntu.com/"
# SUPPORT_URL="https://help.ubuntu.com/"
# BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
# PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
# UBUNTU_CODENAME=jammy
```

（オプション）インストールされているCUDAを表示する。

```bash
!nvcc --version

# nvcc: NVIDIA (R) Cuda compiler driver
# Copyright (c) 2005-2024 NVIDIA Corporation
# Built on Thu_Jun__6_02:18:23_PDT_2024
# Cuda compilation tools, release 12.5, V12.5.82
# Build cuda_12.5.r12.5/compiler.34385749_0
```

```bash
!ls -d /usr/local/cuda-*

# /usr/local/cuda-12  /usr/local/cuda-12.5
```

[NVIDIA公式ダウンロードサイトの指示](https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local)に従って特定のCUDAバージョンをインストールする。

注意：`sudo apt-get -y install cuda`ではなく`sudo apt-get -y install cuda-12-1`を使用する。前者は最新バージョンのCUDAをインストールする。

```bash
!wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
!sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
!wget https://developer.download.nvidia.com/compute/cuda/12.1.0/local_installers/cuda-repo-ubuntu2204-12-1-local_12.1.0-530.30.02-1_amd64.deb
!sudo dpkg -i cuda-repo-ubuntu2204-12-1-local_12.1.0-530.30.02-1_amd64.deb
!sudo cp /var/cuda-repo-ubuntu2204-12-1-local/cuda-*-keyring.gpg /usr/share/keyrings/
!sudo apt-get update

# Modify
# !sudo apt-get -y install cuda
!sudo apt-get -y install cuda-12-1
```

## シンボリックリンクを変更する

（オプション）cuda-12-1がインストールされ、現在のシンボリックリンクがcuda-12-5を指していることを確認する。

```bash
!ls -dl /usr/local/cuda*

# lrwxrwxrwx  1 root root   22 Jul 10  2024 /usr/local/cuda -> /etc/alternatives/cuda
# lrwxrwxrwx  1 root root   25 Jul 10  2024 /usr/local/cuda-12 -> /etc/alternatives/cuda-12
# drwxr-xr-x 15 root root 4096 Feb  5 00:39 /usr/local/cuda-12.1
# drwxr-xr-x  1 root root 4096 Jul 10  2024 /usr/local/cuda-12.5
```

```bash
!ls -l /etc/alternatives/cuda*

# lrwxrwxrwx 1 root root 20 Jul 10  2024 /etc/alternatives/cuda -> /usr/local/cuda-12.5
# lrwxrwxrwx 1 root root 20 Jul 10  2024 /etc/alternatives/cuda-12 -> /usr/local/cuda-12.5
```

CUDAのシンボリックリンクをcuda-12-5からcuda-12-1に変更する。

```bash
!unlink /etc/alternatives/cuda
!ln -s /usr/local/cuda-12.1 /etc/alternatives/cuda

!unlink /etc/alternatives/cuda-12
!ln -s /usr/local/cuda-12.1 /etc/alternatives/cuda-12
```

環境変数を追加する。

```bash
!export PATH="/usr/local/cuda-12.1/bin:$PATH"
!export LD_LIBRARY_PATH="/usr/local/cuda-12.1/lib64:$LD_LIBRARY_PATH"
```

シンボリックリンクが変更されたことを確認する。

```bash
!ls -l /etc/alternatives/cuda*

# lrwxrwxrwx 1 root root 20 Feb  5 01:08 /etc/alternatives/cuda -> /usr/local/cuda-12.1
# lrwxrwxrwx 1 root root 20 Feb  5 01:08 /etc/alternatives/cuda-12 -> /usr/local/cuda-12.1
```

```bash
!nvcc --version

# nvcc: NVIDIA (R) Cuda compiler driver
# Copyright (c) 2005-2023 NVIDIA Corporation
# Built on Mon_Apr__3_17:16:06_PDT_2023
# Cuda compilation tools, release 12.1, V12.1.105
# Build cuda_12.1.r12.1/compiler.32688072_0
```

## 参考文献

- [Cannot install cuda - NVIDIA Developer Forum](https://forums.developer.nvidia.com/t/cannot-install-cuda/287079)
- [How can I install CUDA 12.1 on Ubuntu 22.04. I'm going insane here - NVIDIA Developer Forum](https://forums.developer.nvidia.com/t/how-can-i-install-cuda-12-1-on-ubuntu-22-04-im-going-insane-here/293738)
