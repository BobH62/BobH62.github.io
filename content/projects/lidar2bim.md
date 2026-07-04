---
title: 'LiDAR2BIM: Global LiDAR Registration on BIM via Pose Hough Transform'
date: 2025-03-01
order: 2
summary: Cross-modal registration that aligns a LiDAR submap with a BIM prior map from scratch (no pose prior) — using walls as the "same language" to bridge different modalities.
category: project
nda: false
image: /images/lidar2bim.png
tags:
  - Cross-Modal Registration
  - SLAM
  - BIM
role: Co-first author; method, implementation, experiments
stack:
  - C++
  - ROS
  - PCL
links:
  - { label: code, url: 'https://github.com/HKUST-Aerial-Robotics/LiDAR2BIM-Registration' }
  - { label: video, url: 'https://www.youtube.com/watch?v=SWbnsaRyL-M' }
  - { label: arXiv, url: 'https://arxiv.org/abs/2405.03969' }
gallery: []
---

How do you localize a robot inside a building using only the *as-designed* BIM, with no
prior pose? **LiDAR2BIM** estimates the global transformation between a LiDAR submap and a
BIM from scratch — a cross-modal registration problem (point cloud vs. CAD model). The
registration of digital maps and robot sensing is the fundamental operation that links
virtual design data with real-world observations — enabling BIM-based localization,
digital twins, and on-site monitoring.

::figure-block
---
src: /images/lidar2bim/lidar2bim-intro.jpg
n: 1
caption: Registration aligns the digital model with real-world sensor observations — a quadruped robot navigates a construction site.
---
::

Three challenges make this hard — **unbalanced size** (a submap covers one corridor, the
BIM covers a whole building), **construction inconsistency** (as-built differs from
as-designed), and **different modalities** (a noisy point cloud vs. a clean CAD model).
The core idea is to give both sides a **"same language"**: extract walls and corners from
each, then match on that shared representation.

::figure-block
---
src: /images/lidar2bim/lidar2bim-problem.jpg
n: 2
caption: Problem formulation — find the global transformation T that aligns a local LiDAR submap with the as-designed BIM.
---
::

On the LiDAR side, individual scans are accumulated using odometry into a submap and
voxel-downsampled to a uniform density; on the BIM side, walls and slabs are extracted
directly from the model. Both then reduce to the same 2D primitives — lines and corners.

::figure-block
---
src: /images/lidar2bim/lidar2bim-submap.jpg
n: 3
caption: A LiDAR submap is accumulated from handheld/robot-mounted scans via odometry, then voxel-downsampled.
---
::

The full pipeline runs two parallel feature-extraction tracks that converge into a
matching and estimation stage: walls → projection → 2D lines → corners → triangle
descriptors, one track per modality.

::figure-block
---
src: /images/lidar2bim/lidar2bim-pipeline.jpg
n: 4
caption: Registration pipeline — parallel wall/corner feature extraction, hash-based descriptor matching, and Pose Hough Transform voting.
---
::

For **data association**, every corner triplet is encoded as a 6D triangle descriptor
(three side lengths + three angles), and correspondences are retrieved by hash lookup in
*O(1)* per query — so the matcher scales to huge BIMs without scanning every triangle.

::figure-block
---
src: /images/lidar2bim/lidar2bim-data-assoc.jpg
n: 5
caption: Hash-based descriptor matching turns each query triplet into inliers (green) and outliers (pink) against the BIM.
---
::

This is what makes the method practical at building scale: **100K correspondences are
matched in ~50 ms**, and the hierarchical retrieval propagates matches from a local
submap out to the full building model.

::figure-block
---
src: /images/lidar2bim/lidar2bim-100k.jpg
n: 6
caption: Hierarchical data association — 100K correspondences retrieved in ~50 ms, scaled from a single submap to the whole-building BIM.
---
::

Finally, the **backend** treats estimation as consensus maximization: each triplet
correspondence casts a vote in Pose Hough space (x, y, yaw), the top voted cells are
merged and verified by a confidence score, and the winner's transformation is recovered
in closed form via SVD. Because voting aggregates evidence rather than committing to a
single hypothesis, it stays robust to extreme outlier ratios where RANSAC diverges.

::figure-block
---
src: /images/lidar2bim/lidar2bim-voting.jpg
n: 7
caption: Backend — hierarchical Hough voting with SVD recovery; higher votes indicate the more likely correct pose.
---
::

Published in *IEEE Transactions on Automation Science and Engineering (T-ASE)*. MPhil
thesis work.
