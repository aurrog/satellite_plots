import matplotlib.pyplot as plt

import functions
import tkinter as tk

import plot_builder
from config import*
from tkinter import ttk


class File:
    def __init__(self, path):
        self.path = path
        self.ids = functions.satellite_id_unique(self.path)[1:]
        self.systems = sorted(set([i[1] for i in self.ids]))
        self.names = [system_types_dict[i] for i in self.systems]
        self.types_dict = {}

    def type_list(self):
        label = tk.Label(text='Тип системы ')
        label.place(x=200, y=15, width=150, height=30)

        self.system_combobox = ttk.Combobox(values=self.names)
        self.system_combobox.place(x = 200, y=60, width=150, height = 50)

        btn = tk.Button(text='Далее', command=self.create_number_combobox)
        btn.place(x = 200, y=120)

    def numbers_dict(self):
        if not self.types_dict:
            for satellite_type in system_types_dict.keys():
                types_list = []
                file = open('navdata/' + self.path)
                for row in file:
                    if row[1] == satellite_type:
                        types_list.append(row[:4])
                types_list.append('Все спутники системы')
                self.types_dict[satellite_type] = sorted(set(types_list))
        return self.types_dict

    def create_number_combobox(self):
        self.types_dict = self.numbers_dict()
        isz_type = self.system_combobox.get()

        label = tk.Label(text='Номер спутника')
        label.place(x=400, y=15, width=170, height=30)
        self.satellite_number_combobox = ttk.Combobox(values=self.types_dict[system_types_dict_reverse[isz_type]])
        self.satellite_number_combobox.place(x=400, y=60, width=170, height = 50)

        btn = tk.Button(text='Далее', command=self.type_graph_choice)
        btn.place(x=400, y=120)

    def type_graph_choice(self):
        label = tk.Label(text='Тип графика')
        label.place(x=200, y=185, width=320, height=30)

        self.graph_type_combobox = ttk.Combobox(values=graph_types)
        self.graph_type_combobox.place(x=200, y=210, width=370, height=50)

        btn = tk.Button(text='Далее', command=self.choice_date_interval)
        btn.place(x=200, y=270)

    def choice_date_interval(self):
        lbl = tk.Label(text='начало')
        lbl.place(x=200, y=340, width=150)
        self.starting_combobox_date = ttk.Combobox(values=dates_by_hours)
        self.starting_combobox_date.place(x=200, y=370, width=150)

        lbl = tk.Label(text='начало')
        lbl.place(x=400, y=340, width=150)
        self.ending_combobox_date = ttk.Combobox(values=dates_by_hours)
        self.ending_combobox_date.place(x=400, y=370, width=150)

        btn = tk.Button(text='Далее', command=self.create_plot)
        btn.place(x=200, y=420)

    def create_plot(self):
        graph_response = self.graph_type_combobox.get()
        satellite_type_response = self.satellite_number_combobox.get()

        date_start = int(self.starting_combobox_date.get()[:2])
        date_end = int(self.ending_combobox_date.get()[:2])

        types = self.types_dict[system_types_dict_reverse[self.system_combobox.get()]][:-1] \
            if satellite_type_response == 'Все спутники системы' else [satellite_type_response]

        if graph_response == graph_types[0]:
            plot_builder.coordinates_evolution_graph('navdata/'+self.path, types,
                                                     date_start, date_end, earth_rotation=True)

        elif graph_response == graph_types[1]:
            plot_builder.motion_trajectory_projection_graph('navdata/'+self.path, types,
                                                            date_start, date_end, earth_rotation=False)

        elif graph_response == graph_types[2]:
            plot_builder.motion_trajectory_projection_graph_3d('navdata/'+self.path, types,
                                                               date_start, date_end, earth_rotation=False)

        plt.show()
