---
title: "Point-Cloud Registration for a Robotic Welding Line"
date: 2021-03-01
excerpt: "Registering the digital model and the as-scanned point cloud of steel components on a production line to guide robotic welding — FPFH + Fast Global Registration + ICP with a scale-factor genetic search. My first bridge from architecture into robotics.
<br/>
<br/>
<img src='/images/pc-registration.png' width='500'>"
collection: portfolio
---

An R&D project in an architectural R&D lab: **register the point cloud of a digital model against the actual scanned point cloud of a steel component**, then output the transformation matrix to the assembly line for subsequent welding — optimizing the line's calibration.

- **Pipeline**: downsample → **FPFH** features → **Fast Global Registration** → **ICP** refinement, with a **genetic-algorithm search over a scale factor** to handle size mismatch, and an **iterative range-narrowing** strategy to avoid divergence.
- **Hardware**: Mechmind RGBD camera; addressed single-sided occlusion by analyzing FPFH behavior on thin steel plates (discarding the back layer to improve matching).
- **Results**: 47 groups tested, ~12 s average per registration.

This was my first real bridge from architectural geometry into robotics and 3D vision — the seed of the cross-modal registration work I later did in my MPhil.

- **Role**: Algorithm framework & experiments
- **Stack**: Python, C++, Open3D, PCL
- **Links**: internal R&D project
