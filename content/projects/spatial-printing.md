---
title: Collaborative Spatial Printing
date: 2020-11-01
order: 0
summary: FDM 3D printing of complex structural nodes with collaborative robot arms — an extruder end-effector that deposits variable layer thickness on curved surfaces.
category: project
nda: false
image: /images/other/spatial-printing.jpg
tags:
  - Robotic Fabrication
  - FDM 3D Printing
  - Digital Fabrication
role: Framework coding
stack:
  - Python
  - KRL
  - Arduino
links:
  - { label: Archi-Solution Workshop, url: 'https://www.archi-solutions.com/' }
  - { label: project page, url: 'https://www.archi-solutions.com/2021-geometry-based-robotic-3d-printing-course-at-bfu/' }
gallery: []
---

A workshop project at **[Dr. Lei Yu's Archi-Solution Workshop (ASW)](https://www.archi-solutions.com/)**,
exploring **collaborative robotic FDM** for printing complex
**structural nodes** — the branching joints that connect a tubular space-frame.

A robot-mounted **extruder end-effector** deposits filament in **accumulations
with varying layer thickness on curved surfaces**, so the same tool can build
both the bulk of a node and its finer features. Two arms collaborate on a single
print, coordinated through a digital operation system (Arduino-based control,
air-pump and temperature modules) with gesture/head/eye user-input for live
interaction.

::figure-block
---
n: 1
src: /images/other/spatial-printing-workflow.jpg
caption: The project spread — reversed 3D printing process, system setup, printed nodes, and the full collaborative-printing workflow (dual-arm collaboration, Arduino-based digital operation system, interaction panel, and user-behaviour input).
---
::

The output: white 3D-printed joints that connect clear acrylic tubes into
branching structures — a small, physical demonstration of human-robot
collaboration in spatial printing.

Team: Huang, et al. — my contribution was the **framework coding**.
