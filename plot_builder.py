import numpy as np
import matplotlib.pyplot as plt
import re
from satellite_plots.config import *
from satellite_plots import functions


def get_coordinates(path, satellite_type, ds, de, earth_rotation):
    file = open(path)

    x = np.array([])
    y = np.array([])
    z = np.array([])
    time = np.array([])

    for row in file:
        if re.search(date_pattern, row):
            time_now = row.split()

        if satellite_type in row:
            if ds <= int(time_now[4]) < de:
                row = row.split()
                if earth_rotation:
                    a = -2 * np.pi * (float(time_now[6]) +
                                      float(time_now[5]) * 60 +
                                      float(time_now[4]) * 3600 +
                                      float(row[4]) / 1000000)
                    x_t = functions.rotation_on_the_earth(a=a,
                                                          X=np.array([float(row[1]), float(row[2]), float(row[3])]))

                    x = np.append(x, x_t[0])
                    y = np.append(y, x_t[1])
                    z = np.append(z, x_t[2])
                    time = np.append(time, functions.to_julian(time_now))
                else:
                    x = np.append(x, float(row[1]))
                    y = np.append(y, float(row[2]))
                    z = np.append(z, float(row[3]))
                    time = np.append(time, functions.to_julian(time_now))

    return x, y, z, time


def coordinates_evolution_graph(path, satellite_types, ds, de, earth_rotation):
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].set_title('X(T)')
    axs[0, 1].set_title('Y(T)')
    axs[1, 0].set_title('Z(T)')

    for element in satellite_types:
        x, y, z, time = get_coordinates(path, element, ds, de, earth_rotation)
        axs[0, 0].plot(time, x)
        axs[0, 1].plot(time, y)
        axs[1, 0].plot(time, z)


def motion_trajectory_projection_graph(path, satellite_types, ds, de, earth_rotation):
    fig, axs = plt.subplots(2, 2)

    axs[0, 0].set_title('XZ')
    axs[0, 1].set_title('XY')
    axs[1, 0].set_title('YZ')

    for element in satellite_types:
        x, y, z, time = get_coordinates(path, element, ds, de, earth_rotation)
        axs[0, 0].plot(x, z)
        axs[0, 1].plot(x, y)
        axs[1, 0].plot(y, z)


def motion_trajectory_projection_graph_3d(path, satellite_types, ds, de, earth_rotation):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for element in satellite_types:
        x, y, z, time = get_coordinates(path, element, ds, de, earth_rotation)
        ax.plot(x, y, z)

    plt.legend(functions.generate_legend(len(satellite_types)))

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = 6301 * np.outer(np.cos(u), np.sin(v)) + 0
    y = 6301 * np.outer(np.sin(u), np.sin(v)) + 0
    z = 6301 * np.outer(np.ones(np.size(u)), np.cos(v)) + 0

    ax.plot_surface(x, y, z, color='r')
