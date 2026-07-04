---
title: 'Visual-link Chinatown — Urban-Scene Image Classification & Segmentation'
date: 2020-03-01
order: 0
summary: A visual study of how Chinatowns represent China — street-view imagery composited into a Chinese gate, paired with a CNN pipeline (VGG / AlexNet / ResNet) and semantic segmentation (KITTI / ADE20K) for quantitative urban-feature analysis.
category: project
nda: false
image: /images/other/chinatown.jpg
tags:
  - Visual Analysis
  - Image Mosaic
  - Deep Learning
  - Semantic Segmentation
role: Methodology and experiments
stack:
  - PyTorch
  - Keras
links: []
gallery: []
---

A research study asking: **to what extent does Chinatown represent China, and in
what terms?** The prototype of a Chinatown might come from very different
regions of China — yet the exported image converges on a familiar vocabulary of
gates, tiles, and signage.

The cover is a **mosaic of street-view imagery (SVI)** — hundreds of small photos
of Chinatowns worldwide, tiled into the silhouette of a traditional Chinese
*paifang* gate. The piece is both a visualisation and an argument: the Chinatown
we recognise is an aggregate of fragments, each borrowed from somewhere else.

To probe that argument computationally, I built a **computer-vision pipeline**
over the same street-view imagery:

- **Classification** — trained and compared **AlexNet, VGG, and ResNet** on an
  urban-scene dataset (e.g. predicting a scene as "attractions"), tracking
  training/validation loss and accuracy across epochs.
- **Similarity ranking** — given a query scene, retrieve the nearest
  street-view images by **MSE** feature distance.
- **Feature analysis** — ran **semantic segmentation** with pretrained models
  (**KITTI**, **ADE20K**) to score how much each urban element — road,
  sidewalk, vegetation, sky, signboard — contributes to the predicted label.

::figure-block
---
n: 1
src: /images/other/classification.jpg
caption: The classification and segmentation pipeline — similarity ranking by MSE, a convolutional encoder–decoder, and semantic segmentation masks (KITTI / ADE20K) scoring urban features.
---
::

The mosaic says *this is what Chinatown looks like*; the model says *this is
which fragments it is made of*. Together they turn a cultural question into
something measurable.

Team: Huang, et al. — my contribution was methodology and experiments.
