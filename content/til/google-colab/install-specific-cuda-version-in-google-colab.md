---
title: "Install Specific CUDA Version in Google Colab"
description:
date: 2025-02-05T9:00:00+09:00
lastmod:
draft: false
---

## Install Specific CUDA Version in Google Colab

Following code snippets show how to install cuda-12.1 in Google Colab.

(Optional) Show the current OS version.

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

(Optional) Show the installed cuda.

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

Install specific CUDA version according to [NVIDIA official download site's instruction](https://developer.nvidia.com/cuda-12-1-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local).

Note: Use `sudo apt-get -y install cuda-12-1` instead of `sudo apt-get -y install cuda`. Later one will install the latest version of CUDA.

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

## Change Symbolic Links

(Optional) Confirm the cuda-12-1 was installed and the the current symbolic links to cuda-12-5.

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

Change the symbolic links of cuda from cuda-12-5 to cuda-12-1.

```bash
!unlink /etc/alternatives/cuda
!ln -s /usr/local/cuda-12.1 /etc/alternatives/cuda

!unlink /etc/alternatives/cuda-12
!ln -s /usr/local/cuda-12.1 /etc/alternatives/cuda-12
```

Add the environment variables.

```bash
!export PATH="/usr/local/cuda-12.1/bin:$PATH"
!export LD_LIBRARY_PATH="/usr/local/cuda-12.1/lib64:$LD_LIBRARY_PATH"
```

Confirm the symbolic links was changed.

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

## References

- [Cannot install cuda - NVIDIA Developer Forum](https://forums.developer.nvidia.com/t/cannot-install-cuda/287079)
- [How can I install CUDA 12.1 on Ubuntu 22.04. I’m going insane here - NVIDIA Developer Forum](https://forums.developer.nvidia.com/t/how-can-i-install-cuda-12-1-on-ubuntu-22-04-im-going-insane-here/293738)
