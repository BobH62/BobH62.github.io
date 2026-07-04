---
title: 'SLABIM: A SLAM-BIM Coupled Dataset'
date: 2025-05-01
order: 1
summary: An open dataset coupling a large-scale HKUST BIM with multi-session, multi-sensor SLAM data — 164K+ LiDAR scans and 3,900+ RGB images — with benchmarks for LiDAR-to-BIM registration, pose tracking, and semantic mapping.
category: project
nda: false
image: /images/slabim.png
tags:
  - Dataset
  - SLAM
  - BIM
  - Semantic Mapping
role: Lead author; dataset design, collection, benchmarks
stack:
  - C++
  - ROS
  - Python
links:
  - { label: dataset / code, url: 'https://github.com/HKUST-Aerial-Robotics/SLABIM' }
  - { label: arXiv, url: 'https://arxiv.org/abs/2502.16856' }
gallery: []
---

**SLABIM** bridges the data gap between SLAM research and BIM/digital-twin research.
Existing indoor SLAM datasets focus on robot sensing but lack corresponding building
models — FusionPortable has no CAD, uHumans2 is synthetic, CubiCasa5K has floor plans but
no real sensor data. None couple *SLAM-oriented data* with *the corresponding building
architecture*.

::figure-block
---
src: /images/slabim/slabim-motivation.jpg
n: 1
caption: Existing indoor SLAM datasets each miss a piece — no CAD models, synthetic-only data, or no real sensor data — leaving the SLAM–BIM coupling gap open.
---
::

SLABIM is built from the HKUST main-building BIM and multi-session, multi-sensor data,
covering **164,000+ LiDAR scans** and **3,900+ high-resolution RGB images** across multiple
floors and indoor scenes. Real-world photos are paired with the corresponding BIM
renderings, so the same space is available both as sensed and as designed.

::figure-block
---
src: /images/slabim/slabim-overview.jpg
n: 2
caption: SLABIM overview — large-scale BIM, multi-session/multi-sensor data, and various indoor scenes; real-world photos paired with their BIM digital twins.
---
::

Data is collected with a handheld multi-sensor suite — a Livox Mid-360 LiDAR, a fish-eye
camera, a built-in IMU, and an RTK unit — walked through the building to capture dense,
timestamped scans and images.

::figure-block
---
src: /images/slabim/slabim-sensor.jpg
n: 3
caption: Handheld sensor suite (Livox Mid-360 LiDAR, fish-eye camera, IMU, RTK) used for data acquisition.
---
::

In total, **12 sessions** were collected across four floors and three regions, spanning
corridors, offices, lift lobbies, lounges, and an indoor garden — giving a variety of
indoor geometries for benchmarking.

::figure-block
---
src: /images/slabim/slabim-sessions.jpg
n: 4
caption: Multi-session coverage — 12 sessions across floors/regions, with statistics and the diverse indoor scenes captured.
---
::

To demonstrate practicality, SLABIM ships benchmarks for three tasks: **global
LiDAR-to-BIM registration**, **robot pose tracking on BIM**, and **semantic mapping**
(evaluated against BIM-derived ground truth, mIoU ~64–65%).

::figure-block
---
src: /images/slabim/slabim-tasks.jpg
n: 5
caption: Three benchmark tasks enabled by SLABIM — global LiDAR-to-BIM registration, robot pose tracking on BIM, and semantic mapping.
---
::

Published at *IEEE ICRA 2025*. Open dataset & code released.
