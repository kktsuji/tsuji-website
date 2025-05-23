---
title: 'Prompting Medical Large Vision-Language Models to Diagnose Pathologies by Visual Question Answering'
description: ''
date: 2024-08-07T09:00:00+09:00
lastmod: 
draft: false
---

Title: Prompting Medical Large Vision-Language Models to Diagnose Pathologies by Visual Question Answering

Authors: Danfeng Guo, Demetri Terzopoulos

Published: Jul 31 2024

Link: [https://arxiv.org/abs/2407.21368](https://arxiv.org/abs/2407.21368)

Summary:

- Authors introduced two prompting methods to reduce hallucinations on medical large vision-language model (LVLMs) and improve visual question answering (VQA) tasks:
    1. Provide detailed pathological descriptions to the question queries.
    2. Introduce “weak learner” to provide its prediction results to the question queries as a reference opinion.
- Proposed method improves the diagnostic F1 score by up to 0.27 on the MIMIC-CXR-JPG and Chexpert dataset.

Summary (Generated by Microsoft Copilot):

Here is a summary of the page:

- **Introduction**: The paper discusses the application of Large Vision-Language Models (LVLMs) in medical Visual Question Answering (VQA) tasks, focusing on diagnosing pathologies from medical images.

- **Challenges**: LVLMs suffer from hallucination problems and struggle with minority pathologies due to imbalanced training data.

- **Methods**: Two prompting strategies are proposed: providing detailed explanations of pathologies and using a weak learner model to improve VQA performance.

- **Novelties**: The study introduces cost-effective prompting strategies to reduce hallucination and improve diagnostic accuracy.

- **Results**: The proposed methods significantly improve the diagnostic F1 score, with the highest increase being 0.27.

- **Performances**: The strategies enhance Recall by approximately 0.07 and reduce false negative predictions.

- **Limitations**: The strategies are less effective for pathologies with extremely scarce data.

- **Discussion**: Future research could explore strategies like Retrieval Augmented Generation (RAG) to handle rare categories.
