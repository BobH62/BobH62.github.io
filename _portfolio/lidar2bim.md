---
title: "LiDAR2BIM: Global LiDAR Registration on BIM via Pose Hough Transform"
date: 2025-03-01
excerpt: "Cross-modal registration that aligns a LiDAR submap with a BIM prior map from scratch (no pose prior) — using walls as the \"same language\" to bridge different modalities.
<br/>
<br/>
<img src='/images/lidar2bim.png' width='500'>"
collection: portfolio
---

How do you localize a robot inside a building using only the *as-designed* BIM, with no prior pose? **LiDAR2BIM** estimates the global transformation between a LiDAR submap and a BIM from scratch — a cross-modal registration problem (point cloud vs. CAD model).

Three challenges — **unbalanced size**, **construction inconsistency**, and **different modalities** — are tackled with three ideas:

- **Wall-based "same language"**: extract walls/corners from both LiDAR and BIM as a shared representation.
- **Triangle descriptors + hash matching**: build corner-triplet descriptors and retrieve correspondences via hash lookup in ~50 ms for 100K correspondences.
- **Pose Hough Transform**: a parallel, robust estimator that votes in pose-Hough space and verifies by confidence score — robust to extreme outlier ratios where RANSAC diverges.

Published in *IEEE Transactions on Automation Science and Engineering (T-ASE)*. MPhil thesis work.

- **Role**: Co-first author; method, implementation, experiments
- **Stack**: C++, ROS, PCL
- **Links**: [code](https://github.com/HKUST-Aerial-Robotics/LiDAR2BIM-Registration) / [video](https://www.youtube.com/watch?v=SWbnsaRyL-M) / [arXiv](https://arxiv.org/abs/2405.03969)
