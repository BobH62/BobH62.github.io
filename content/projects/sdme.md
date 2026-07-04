---
title: 'Solar Decathlon Middle East 2021 — Overall Champion'
date: 2021-06-01
order: 0
summary: A student-led full-size solar house, designed and built in Dongguan and shipped to Dubai for Expo 2020 — Overall Champion of Solar Decathlon Middle East 2021, the Olympics of international architecture student competitions. I built its smart-home system and robotically fabricated its furniture.
category: project
nda: false
image: /images/sdme/sdme-cover.jpg
tags:
  - Solar Decathlon
  - Smart Home
  - Robotic Fabrication
  - Full-Scale Construction
role: Smart-home system & robotic furniture fabrication
stack:
  - Home Assistant
  - Python
  - Raspberry Pi
  - Zigbee/MQTT/Modbus
  - Robotic milling
links:
  - { label: project page, url: 'https://solarchitecture.ch/sdme-2021-team-x-house/' }
gallery: []
---

**Solar Decathlon Middle East (SDME)** is the Olympics of international
architecture student competitions — a real, student-led contest where each team
takes a full-size solar house from design to construction and then lives in it
under competition conditions. Our **X House** was designed and prefabricated in a
Dongguan factory, shipped to Dubai, and assembled on the Mohammed bin Rashid Al
Maktoum Solar Park site during Expo 2020. We won **Overall Champion**.

My contributions sat at the intersection of building and technology: I built the
**smart-home system** that ran the house during competition, and I
**robotically fabricated its unconventional GRC furniture**.

::figure-block
---
n: 1
src: /images/sdme/sdme-construction.jpg
caption: On-site assembly in Dubai — prefabricated modules lifted into place by crane, with rooftop PV installed against the backdrop of the Mohammed bin Rashid Al Maktoum Solar Park Innovation Centre.
---
::

## From factory to Dubai: modular construction

The house is a kit of shipping-container-sized modules — bedroom, dining,
living, service, and a 20-ft atrium — prefabricated in Dongguan and bolted
together on site. The 9-step sequence below reads like an industrial assembly
manual: hoist modules, close the ring around the atrium, lay the upper roof
frame, finish the PV roof, then deck and enclose.

::figure-block
---
n: 2
src: /images/sdme/sdme-assembly.jpg
caption: Nine-step modular assembly sequence — from module hoisting and atrium closure to the PV roof and external deck.
---
::

Fault tolerance was designed into every joint: limit bolts, enlarged gaskets,
and elliptical holes absorbed fabrication and shipping inaccuracies, while
elastic butyl/rubber connections between wood keel and steel survived the
ocean freight. The result was an airtight, transportable building.

## A house that reconfigures itself

Sliding doors let three rooms merge into one. The same atrium becomes a party
hall, a home gym, a quiet office, or a cinema — a small house that behaves like
a large one.

::figure-block
---
n: 3
src: /images/sdme/sdme-flex-configs.jpg
caption: Four functional configurations of the same space — PARTY, GYM, OFFICE, and THEATER — enabled by sliding doors and automated scenarios.
---
::

## Smart-home system (my contribution)

The competition judged indoor environment in real time — temperature, humidity,
CO₂ — so the house needed precise, scriptable control. I built the system on
**Home Assistant** running on a **Raspberry Pi**, integrating appliances over
**Zigbee / MQTT / Modbus** and automating scenarios (blinds, skylights, climate)
in **YAML**. A **Zerotier VPN** let us monitor and operate the house in Dubai
from Guangzhou, 24/7, from phones and laptops.

::figure-block
---
n: 4
src: /images/sdme/sdme-smarthome-section.jpg
caption: Architectural section with the smart-home overlay — a Raspberry Pi running Home Assistant wired to sensors, actuators, and appliances across the house.
---
::

::figure-block
---
n: 5
src: /images/sdme/sdme-smarthome-ui.jpg
caption: The Home Assistant dashboard — tablet and mobile layouts with live climate gauges, AC toggles, and lighting scenes.
---
::

## Robotic fabrication of furniture (my contribution)

For the furniture I wanted the ethereal essence of Chinese landscapes — gentle
curves of rolling hills, the serene stability of ancient mountains — translated
into concrete. I designed a tea table and a washstand and used the laboratory's
robotic arm to mill their molds; the uniquely shaped GRC (glass-fibre reinforced
concrete) pieces were then cast in a factory and shipped overseas.

::figure-block
---
n: 6
src: /images/sdme/sdme-fabrication.jpg
caption: Digital fabrication — the robotic arm milling organic-curved molds, and the finished GRC tea table and washstand in place.
---
::

## A lived-in house

The smartest part of the project is that people actually lived in it. The
interior below is the living room as used during the contest — modular
furniture, a vertical garden, and the atrium glazing that turns the whole house
into one continuous, daylit space.

::figure-block
---
n: 7
src: /images/sdme/sdme-interior-living.jpg
caption: The finished living room during competition — minimalist modular furniture, living wall, and atrium glazing.
---
::

## A global stage

SDME 2021 ran alongside Expo 2020 Dubai, putting student-built solar houses in
front of an international audience of visitors, officials, and industry. It was
the moment a factory-built house I had helped design, automate, and furnish
stood on a world stage — and won.

::figure-block
---
n: 8
src: /images/sdme/sdme-expo.jpg
caption: The X House open to the public at Expo 2020 Dubai — visitors, officials, and the living wall under the atrium skylight.
---
::
