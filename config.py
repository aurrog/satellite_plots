system_types_dict = {
    'R': 'ГЛОНАСС',
    'G': 'GPS',
    'E': 'Galileo',
    'C': 'BeiDou',
    'J': 'QZSS'
}

system_types_dict_reverse = {
    'ГЛОНАСС': 'R',
    'GPS': 'G',
    'Galileo': 'E',
    'BeiDou': 'C',
    'QZSS': 'J'
}

graph_types = [
    'Эволюция координат во времени (X(T),Y(T),Z(T))',
    'Проекция траектории движения на плоскости XZ,XY,YZ',
    'Траектория движения на трехмерной координатной плоскости'
]

date_pattern = r'  [0-9][0-9][0-9][0-9] [0-12]'

dates_by_hours = [f'{i if len(str(i)) == 2 else f"0{i}"}:00' for i in range(0, 25)]
