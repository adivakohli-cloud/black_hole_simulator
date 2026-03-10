## Spacetime Curvature & Black Hole Simulator

A real-time 3D physics simulation built with VPython that visualizes the interaction between light (photons) and the extreme gravitational environment of a Schwarzschild Black Hole.

### Scientific Overview

This simulator utilizes principles from Albert Einstein's General Theory of Relativity to represent how massive objects influence the geometry of the universe.

### Spacetime Curvature & the Gravity Well

According to General Relativity, gravity is not a force but a consequence of the curvature of four-dimensional spacetime. In this simulation, the 3D grid represents the "fabric" of spacetime. The vertical displacement ($z$-axis) visualizes the Gravity Well, showing how the presence of mass "stretches" the coordinate system.

### The Schwarzschild Metric

The simulation is an approximation of the Schwarzschild Metric, which describes the gravitational field outside a spherical, non-rotating mass. It provides the mathematical foundation for understanding the "shape" of space around the black hole.

### Geodesics and Light Bending

In the simulator, photons follow Geodesics—the shortest paths between two points in curved space. While the photons move at a constant speed, their paths appear curved to an observer because the underlying space itself is warped.

### Relativistic Motion
The physics engine includes a $1/r^3$ correction term ($3G/r^3$) to account for general relativistic effects that are absent in classical Newtonian physics.

### The Event Horizon

The cyan ring represents the Event Horizon. This is the mathematical "point of no return" where the escape velocity required to leave the black hole exceeds the speed of light. Any photon that crosses this boundary ($r < 2.5$) is effectively captured and disappears into the singularity.

### Accretion Disk Dynamics

The orange particles represent the Accretion Disk, a structure of diffuse material orbiting the black hole. These particles follow orbital mechanics where their angular velocity ($\omega$) is determined by their radial distance from the center, creating a realistic swirling motion.

### Installation & Setup

### Prerequisites

Ensure you have Python installed on your system. You will need the vpython and numpy libraries.

### Installation

You can install the necessary dependencies using pip:

pip install vpython numpy

### Running the Simulator

Simply run the script using Python

### Interaction Guide

The simulation runs in a web-based canvas provided by VPython. You can interact with the 3D environment using the following controls:

Rotate Camera: Right-click and drag the mouse.

Zoom In/Out: Use the mouse scroll wheel.

Pan Camera: Shift + Left-click and drag.

Automatic Restart: The simulation automatically spawns a new wave of photons once the current set has either been captured or flown out of range.

### Key Parameters

M

Mass: Controls the depth of the spacetime curvature.

G

Bending Strength: Determines how aggressively light paths are deflected.

event_horizon_radius

The radius at which photons are "captured" (rendered as 2.5).

dt

Delta Time: The time-step for the numerical integration.

### Project Structure 
black-hole-simulator
│
├── black_hole_simulator.py
├── README.md
├── requirements.txt
|── references.txt


### License


This project is open-source and intended for educational purposes in the fields of physics and computational modeling.
