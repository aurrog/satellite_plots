import numpy as np
import math
import matplotlib.pyplot as plt
import re
from config import *
import functions


def rotation_on_the_earth():
    pass


def coordinates_evolution_graph(path, satellite_type):
    file = open(path)

    x = np.array([])
    y = np.array([])
    z = np.array([])
    time = np.array([])

    if satellite_type != 'Все спутники системы':
        for row in file:
            if re.search(date_pattern, row):
                time_now = row
                time = np.append(time, functions.to_julian(time_now.split()))
            if satellite_type in row:
                row = row.split()
                a = -2*np.pi*(float(time_now[6]) + float(time_now[5])*60 + float(time_now[4])*3600)
                x_t = functions.rotation_on_the_earth(a=a, X=np.array([float(row[1]), float(row[2]), float(row[3])]))
                x = np.append(x, x_t[0])
                y = np.append(y, x_t[1])
                z = np.append(z, x_t[2])
    else:


        plt.plot(y, z)


# text = '*  2022 10 18  0  0  0.00000000'
# pattern = r'  [0-9][0-9][0-9][0-9] [0-12]'
#
# match = re.search(pattern, text)
# print(match)
