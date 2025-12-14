---
title: "Valid Combinations of CUDA, CuDNN and Tensorflow"
description: ""
date: 2025-02-16T08:00:00+09:00
lastmod:
draft: false
---

## Valid Combination List

[Tested Build Configurations - tensorflow.org](https://www.tensorflow.org/install/source#tested_build_configurations) provides a list of valid combinations of CUDA, CuDNN and Tensorflow versions.

| TensorFlow Version | CuDNN | CUDA |
| ------------------ | ----- | ---- |
| tensorflow-2.18.0  | 9.3   | 12.5 |
| tensorflow-2.17.0  | 8.9   | 12.3 |
| tensorflow-2.16.1  | 8.9   | 12.3 |
| ...                | ...   | ...  |

## Confirm Versions

Tensorflow

```bash
pip list | grep tensorflow

# tensorflow                         2.18.0
# tensorflow-datasets                4.9.7
# tensorflow-hub                     0.16.1
# tensorflow-io-gcs-filesystem       0.37.1
# tensorflow-metadata                1.16.1
# tensorflow-probability             0.25.0
# tensorflow-text                    2.18.1
```

CUDA

```bash
nvcc -V

# nvcc: NVIDIA (R) Cuda compiler driver
# Copyright (c) 2005-2023 NVIDIA Corporation
# Built on Mon_Apr__3_17:16:06_PDT_2023
# Cuda compilation tools, release 12.1, V12.1.105
```

CuDNN

```bash
cat /usr/include/cudnn.h | grep CUDNN_MAJOR -A 2

# Build cuda_12.1.r12.1/compiler.32688072_0
# Sat Feb 15 06:32:54 2025
```

NVIDIA Driver

```bash
nvidia-smi

# +-----------------------------------------------------------------------------------------+
# | NVIDIA-SMI 550.54.15              Driver Version: 550.54.15      CUDA Version: 12.4     |
# |-----------------------------------------+------------------------+----------------------+
# | GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
# | Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
# |                                         |                        |               MIG M. |
# |=========================================+========================+======================|
# |   0  Tesla T4                       Off |   00000000:00:04.0 Off |                    0 |
# | N/A   43C    P8              9W /   70W |       0MiB /  15360MiB |      0%      Default |
# |                                         |                        |                  N/A |
# +-----------------------------------------+------------------------+----------------------+

# +-----------------------------------------------------------------------------------------+
# | Processes:                                                                              |
# |  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
# |        ID   ID                                                               Usage      |
# |=========================================================================================|
# |  No running processes found                                                             |
# +-----------------------------------------------------------------------------------------+

```
