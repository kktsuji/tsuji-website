---
title: 'Domain-Specific Language Model Pretraining for Biomedical Natural Language Processing'
description: ''
date: 2024-09-14T09:30:00+09:00
lastmod: 
draft: false
---

Title: BioGPT: Generative Pre-trained Transformer for Biomedical Text Generation and Mining

Authors: Yu Gu, Robert Tinn, Hao Cheng, Michael Lucas, Naoto Usuyama, Xiaodong Liu, Tristan Naumann, Jianfeng Gao, Hoifung Poon

Published: Jul 31 2020

Link: [https://arxiv.org/abs/2007.15779](https://arxiv.org/abs/2007.15779)

Summary (Generated by Microsoft Copilot):

**Introduction:**
- The paper investigates the effectiveness of domain-specific pretraining for biomedical NLP tasks, challenging the assumption that starting from general-domain models is beneficial.

**Challenges:**
- Mixed-domain pretraining may not be advantageous for domains with abundant in-domain text, like biomedicine, due to potential negative transfer from general-domain text.

**Methods:**
- The study involves pretraining language models from scratch using solely biomedical text and comparing it with continual pretraining of general-domain models.

**Novelties:**
- The research introduces a comprehensive biomedical NLP benchmark and demonstrates that domain-specific pretraining from scratch outperforms mixed-domain approaches.

**Results:**
- Domain-specific pretraining leads to new state-of-the-art results across various biomedical NLP tasks.

**Performances:**
- The study shows significant improvements in tasks such as named entity recognition, relation extraction, and question answering.

**Limitations:**
- The paper does not explore the impact of domain-specific pretraining in domains with less abundant in-domain text.

**Discussion:**
- The findings suggest rethinking common practices in NLP, such as the use of complex tagging schemes, and highlight the potential of domain-specific pretraining for specialized fields.

**BLURB**
- **Benchmark**: BLURB stands for **Biomedical Language Understanding & Reasoning Benchmark**. It is a comprehensive biomedical NLP benchmark compiled from publicly available datasets.
- **Tasks**: It includes a wide range of tasks such as **named entity recognition (NER)**, **evidence-based medical information extraction (PICO)**, **relation extraction**, **sentence similarity**, **document classification**, and **question answering**.
- **Leaderboard**: A leaderboard featuring the BLURB benchmark has been created to help accelerate research in biomedical NLP.
- **Purpose**: The benchmark aims to facilitate the evaluation of domain-specific pretraining and task-specific fine-tuning in biomedical NLP.