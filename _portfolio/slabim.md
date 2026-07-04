---
title: "SLABIM: A SLAM-BIM Coupled Dataset"
date: 2025-05-01
excerpt: "An open dataset coupling a large-scale HKUST BIM with multi-session, multi-sensor SLAM data — 164K+ LiDAR scans and 3,900+ RGB images — with benchmarks for LiDAR-to-BIM registration, pose tracking, and semantic mapping.
<br/>
<br/>
<img src='/images/slabim.png' width='500'>"
collection: portfolio
---

**SLABIM** bridges the data gap between SLAM research and BIM/digital-twin research. Existing indoor SLAM datasets focus on robot sensing but lack corresponding building models; **SLABIM** couples a large-scale HKUST main-building BIM with multi-session, multi-sensor data:

- **164,000+ LiDAR scans** and **3,900+ high-resolution RGB images** across 12 sessions / multiple floors.
- Handheld multi-sensor suite (LiDAR, stereo cameras, IMU, RTK-GPS).
- Three benchmark tasks: **LiDAR-to-BIM registration**, **robot pose tracking on BIM**, and **semantic mapping** (evaluated vs. BIM-derived ground truth, mIoU ~64–65%).

Published at *IEEE ICRA 2025*. Open dataset & code released.

- **Role**: Lead author; dataset design, collection, benchmarks
- **Stack**: C++, ROS, Python
- **Links**: [dataset / code](https://github.com/HKUST-Aerial-Robotics/SLABIM) / [arXiv](https://arxiv.org/abs/2502.16856)
