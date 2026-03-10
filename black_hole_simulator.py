from vpython import *
import numpy as np

# setting up scene
scene = canvas(width=1500, height=700, background=color.black)
scene.title = "Spacetime Curvature Around Black Hole"
scene.range = 12
scene.center = vector(0, 0, -5)
scene.autoscale = False

# parameters
M = 20  # depth of gravity well
G = 22  # strength of bending
dt = 0.02
event_horizon_radius = 2.5


def spacetime_height(x, y):
    r = np.sqrt(x ** 2 + y ** 2) + 0.5
    return -M / max(r, 2)


# spacetime grid
grid_size = 16
step = 1

for x in np.arange(-grid_size, grid_size + step, step):
    pts = []
    for y in np.arange(-grid_size, grid_size + step, step):
        z = spacetime_height(x, y)
        pts.append(vector(x, y, z))
    curve(pos=pts, radius=0.03, color=color.white)

for y in np.arange(-grid_size, grid_size + step, step):
    pts = []
    for x in np.arange(-grid_size, grid_size + step, step):
        z = spacetime_height(x, y)
        pts.append(vector(x, y, z))
    curve(pos=pts, radius=0.03, color=color.white)

# black hole and event horizon
blackhole = sphere(
    pos=vector(0, 0, -3),
    radius=1.5,
    color=color.black
)

event_horizon = ring(
    pos=vector(0, 0, -3),
    axis=vector(0, 0, 1),
    radius=2.5,
    thickness=0.15,
    color=color.cyan,
    opacity=0.6
)

# accretion disk
disk_particles = []
for i in range(250):
    r_disk = np.random.uniform(3.2, 5.5)
    theta = np.random.uniform(0, 2 * np.pi)
    x = r_disk * np.cos(theta)
    y = r_disk * np.sin(theta)
    z = spacetime_height(x, y) + 0.05
    p = sphere(pos=vector(x, y, z), radius=0.08, color=vector(1, 0.5, 0.1), emissive=True)
    disk_particles.append(p)


# photons
def spawn_photons():
    new_photons = []
    for y0 in np.linspace(-10, 10, 18):
        start_x = -18
        start_y = y0
        start_z = spacetime_height(start_x, start_y)
        p = sphere(
            pos=vector(start_x, start_y, start_z),
            radius=0.16,
            color=vector(1, 0.8 - abs(y0) / 12, 0.2),
            make_trail=True,
            retain=150  # trails
        )
        p.velocity = vector(0.5, 0, 0)
        new_photons.append(p)
    return new_photons


photons = spawn_photons()

# main loop
while True:
    rate(45)

    # replay logic: if all photons are gone, sim restarts
    if len(photons) == 0:
        photons = spawn_photons()

    for photon in photons[:]:
        # physics calculations
        r_vec = vector(-photon.pos.x, -photon.pos.y, 0)
        r = mag(r_vec) + 0.1

        accel = (G / r ** 2) * norm(r_vec)
        relativistic_term = (3 * G) / (r ** 3)
        accel += relativistic_term * norm(r_vec)

        photon.velocity.x += accel.x * dt
        photon.velocity.y += accel.y * dt

        photon.pos.x += photon.velocity.x
        photon.pos.y += photon.velocity.y
        photon.pos.z = spacetime_height(photon.pos.x, photon.pos.y)

        # capture and cleanup logic
        # fade as it approaches event horizon
        if r < event_horizon_radius * 1.3:
            photon.opacity = r / (event_horizon_radius * 1.3)

        # remove if inside event horizon OR if it has flown far away
        if r < event_horizon_radius or photon.pos.x > 22 or abs(photon.pos.y) > 20:
            photon.visible = False
            photon.clear_trail()  # Prevents ghost trails in memory
            photons.remove(photon)
            continue

    # rotate accretion disk
    for p in disk_particles:
        r_p = mag(vector(p.pos.x, p.pos.y, 0))
        omega = 0.02 / np.sqrt(r_p)

        # rotation math
        new_x = p.pos.x * np.cos(omega) - p.pos.y * np.sin(omega)
        new_y = p.pos.x * np.sin(omega) + p.pos.y * np.cos(omega)

        p.pos.x = new_x
        p.pos.y = new_y
        p.pos.z = spacetime_height(new_x, new_y) + 0.05