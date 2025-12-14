---
title: "GPU Resources for Machine Learning"
description: ""
date: 2024-07-27T15:43:49+09:00
lastmod:
draft: false
---

## Free Resources

### University Laboratory

- Pros:
  - It'd be the easiest and most flexible way to use.
  - There'd be a manual, member's support or something in laboratory.
- Cons:
  - The GPU quality depends on the laboratory's budget.
  - You may need to wait until resources become available during busy season.
  - The project would be less reproducible. Documentation must be carefully prepared when source code is to be public.

### Google's TPU Research Cloud

[TPU Research Cloud](https://sites.research.google/trc/about/) offers cloud machine resources to researchers for free.

- Pros:
  - Tensor Processing Unit (TPU) is available free of charge.
- Cons:
  - Free 30-days access to TPU requires application and approval.
  - TPUs are free, but other Google Cloud Platform services such as storage for dataset are charged.
  - Pytorch (by Meta) can be used, but it is said that TensorFlow (by Google) is better than it, because tensorflow natively supports TPUs.

### Google Colab (Free Plan)

[Google Colab](https://colab.research.google.com/).

- Pros:
  - High reproducibility of your project.
- Cons:
  - Free plan has poor machine power and time limits.

## Paid Resources

### My Own GPU

- Pros:
  - It's free to use except for electricity once you purchase a GPU.
  - Always available.
- Cons:
  - GPUs are easily outdated because GPUs evolve so quickly.
  - Low GPU utilization is less cost-effective than on-demand use of cloud resources.
  - GPU can be broken.
  - Low reproducibility of your source code.

### Cloud Services

Consider costs.

- [Google Colab (Paid Plan)](https://colab.research.google.com/)
- [GCP (Google Cloud Platform)](https://console.cloud.google.com/welcome)
- [AWS (Amazon Web Service)](https://aws.amazon.com/)
- [Microsoft Azure](https://portal.azure.com/)
- etc.
