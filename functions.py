import numpy as np


def to_julian(text: list):
    year = int(text[1])
    month = int(text[2])
    day = int(text[3])
    hour = int(text[4])
    minute = int(text[5])
    second = float(text[6])

    a = (14 - month) // 12
    y = year + 4800 - a
    m = month + 12 * a - 3

    JDN = day + (153 * m + 2) / 5 + 365 * y + y / 4 - y / 100 + y / 400 - 32045
    JD = JDN + (hour - 12) / 24 + minute / 1440 + second / 86400

    return JD


def rotation_on_the_earth(a, X):
    rotate_matrix = np.array([
        [np.cos(a), np.sin(a), 0],
        [-np.sin(a), np.cos(a), 0],
        [0, 0, 1]
    ])

    return np.dot(rotate_matrix, X)


def satellite_id_unique(path):
    file = open('navdata/' + path)

    id_list = []
    n = 0
    for row in file:
        if len(row.split()) == 5:
            id_list.append(row[:4])
        n += 1
        if n > 400:
            break

    return sorted(set(id_list))


def generate_legend(len_list):
    return [f'Satellite {i + 1}' for i in range(len_list)]
