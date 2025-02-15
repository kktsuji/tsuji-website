---
title: 'Use Docker in Google Colab'
description: 
date: 2025-02-15T18:00:00+09:00
lastmod: 
draft: false
---

## Summary

- Docker is not allowed to run in Google Colab.
- We can use docker-in-colab (udocker) to run docker in Colab but it can't access the GPU.

## Use docker-in-colab (udocker)

### Installation

[drengskapur/docker-in-colab](https://github.com/drengskapur/docker-in-colab) provides a script to install [indigo-dc/udocker](https://github.com/indigo-dc/udocker) in Google Colab.

```python
# Install
def udocker_init():
    import os
    if not os.path.exists("/home/user"):
        !pip install udocker > /dev/null
        !udocker --allow-root install > /dev/null
        !useradd -m user > /dev/null
    print(f'Docker-in-Colab 1.1.0\n')
    print(f'Usage:     udocker("--help")')
    print(f'Examples:  https://github.com/indigo-dc/udocker?tab=readme-ov-file#examples')

    def execute(command: str):
        user_prompt = "\033[1;32muser@pc\033[0m"
        print(f"{user_prompt}$ udocker {command}")
        !su - user -c "udocker $command"

    return execute

udocker = udocker_init()
```

```python
# Confirm
udocker("run hello-world")

# user@pc$ udocker run hello-world
# Info: creating repo: /home/user/.udocker
# Info: udocker command line interface 1.3.17
# Info: searching for udockertools >= 1.2.11
# Info: installing udockertools 1.2.11
# Info: installation of udockertools successful
# Info: downloading layer sha256:74cc54e27dc41bb10dc4b2226072d469509f2f22f1a3ce74f4a59661a1d44602
# Info: downloading layer sha256:e6590344b1a5dc518829d6ea1524fc12f8bcd14ee9a02aa6ad8360cce3a9a9e9
# Warning: check container content: 0dab5d39-3709-376c-b86c-3680ea1226d5
 
#  ****************************************************************************** 
#  *                                                                            * 
#  *               STARTING 0dab5d39-3709-376c-b86c-3680ea1226d5                * 
#  *                                                                            * 
#  ****************************************************************************** 
#  executing: hello

# Hello from Docker!
# This message shows that your installation appears to be working correctly.

# To generate this message, Docker took the following steps:
#  1. The Docker client contacted the Docker daemon.
#  2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
#     (amd64)
#  3. The Docker daemon created a new container from that image which runs the
#     executable that produces the output you are currently reading.
#  4. The Docker daemon streamed that output to the Docker client, which sent it
#     to your terminal.

# To try something more ambitious, you can run an Ubuntu container with:
#  $ docker run -it ubuntu bash

# Share images, automate workflows, and more with a free Docker ID:
#  https://hub.docker.com/

# For more examples and ideas, visit:
#  https://docs.docker.com/get-started/
```

### Usage

```python
udocker("images")
udocker("ps")
udocker("pull nvidia/cuda:12.1.0-cudnn8-runtime-ubuntu20.04")
udocker("--help")
```

### Limitations

The containers created by docker-in-colab doesn't to seem to be able to access the GPU in spite of their GPU setup option.

```python
udocker("setup --help")

# user@pc$ udocker setup --help

#         setup: change container execution settings
#         setup [options] <container-id>
#         --execmode=<mode>       :select execution mode from below
#         --force                 :force setup change
#         --purge                 :clean mountpoints and files created by udocker
#         --fixperm               :attempt to fix file permissions
#         --nvidia                :add NVIDIA libraries and binaries

#         <mode> is one of the following execution modes:
#         P1: proot accelerated mode using seccomp filtering (default)
#         P2: proot accelerated mode disabled
#         F1: fakechroot starting executables via direct loader invocation
#         F2: like F1 plus protected environment and modified ld.so
#         F3: fakechroot plus patching of elf headers in binaries and libs
#         F4: like F3 plus support for newly created executables via
#             dynamic patching of elf headers in binaries and libs
#         R1: runc using rootless namespaces, requires recent kernel
#             with user namespace support enabled
#         R2: proot with root emulation running on top of runc to avoid
#             most of the errors related to change of uid or gid
#         R3: same as R2 but with proot accelerated mode disabled
#         S1: singularity, requires a local installation of singularity,
#             if singularity is available in the PATH udocker will use
#             it to execute the container
```

``setup --nvidia`` option doesn't work as expected in colab.

```python
udocker("setup --nvidia container-id")

# user@pc$ udocker setup --nvidia container-id
# Error: host nvidia libraries not found
```

I guess this is because the colab's limitation. I cannot find a solution this problem on the internet.

## Install docker directly

[mwufi/install_docker_in_colab.sh](https://gist.github.com/mwufi/6718b30761cd109f9aff04c5144eb885) also provides a script to directly install docker in colab.

```python
!curl -fsSL https://gist.githubusercontent.com/mwufi/6718b30761cd109f9aff04c5144eb885/raw/install_docker_in_colab.sh | sh
```

Installation looks to be a success, but it doesn't work.

```python
!docker run hello-world

# docker: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?.
# See 'docker run --help'.
```

These commands don't work due to the colab's limitation, I guess.

```python
!sudo service docker start
# mkdir: cannot create directory ‘cpuset’: Read-only file system

!sudo systemctl status docker
# System has not been booted with systemd as init system (PID 1). Can't operate.
# Failed to connect to bus: Host is down
```
