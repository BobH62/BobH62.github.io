---
title: Point-Cloud Registration for a Robotic Welding Line
date: 2021-03-01
order: 0
summary: Registering the digital model and the as-scanned point cloud of steel components on a production line to guide robotic welding — my first bridge from architecture into robotics.
category: project
nda: true
image: /images/pc-reg/pcreg-cover.jpg
tags:
  - Point-Cloud Registration
  - 3D Vision
  - Robotics
role: Algorithm framework & experiments (intern, RoboticPlus.Tech)
stack:
  - Python
  - C++
  - Open3D
  - PCL
links:
  - { label: RoboticPlus.Tech, url: 'https://www.roboticplus.tech/' }
gallery: []
---

::media-text
---
n: 1
src: /images/pc-reg/pcreg-pipeline.jpg
mediaWidth: 22rem
caption: The concept — align the digital model's point cloud with the actual scanned cloud, then hand the transformation matrix to the robotic welding line.
---
An R&D project carried out during my internship at
[RoboticPlus.Tech](https://www.roboticplus.tech/) (大界智造), a Shanghai-based
design-build consultancy driven by digital fabrication and intelligent
construction: **register the point cloud of a digital model against the actual
scanned point cloud of a steel component**, then output the transformation
matrix to the assembly line for subsequent welding — optimizing the line's
calibration. Team: Gao, Huang; my contribution was the algorithm framework and
its modification. This was my first real bridge from architectural geometry
into robotics and 3D vision.

The welding line needed sub-millimetre placement but had no reliable way to
relate the as-designed CAD to the as-scanned component — a classic digital-twin
gap on the factory floor. Closing it meant solving registration under real
occlusion, scale drift between model and scan, and the deep symmetry of thin
steel plates, where generic feature descriptors blur into ambiguity.
::
