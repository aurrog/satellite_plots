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

        btn = tk.Button(text='Далее', command=self.create_plot)
        btn.place(x=200, y=270)

    def create_plot(self):
        responce = self.graph_type_combobox.get()
        if responce == graph_types[0]:
            plot_builder.coordinates_evolution_graph('navdata/'+self.path, self.satellite_number_combobox.get())
            plt.show()
        elif responce == graph_types[1]:
            pass
        elif responce == graph_types[1]:
            pass

    def to_table(self):
        pass

# file = open('navdata/Sta30s22322.sp3')
# n = 1
# j = 27
# # df = pd.DataFrame(columns=['sattelite_id', 'satellite_type', 'X', 'Y', 'Z', 'TIME_CHECK', 'DATE'])
# #
# # sattelite_id = []
#
# for i in os.listdir('navdata'):
#     l = []
#     file = open('navdata/'+i)
#     for j in file:
#         if len(j.split()) == 5:
#             # print(j[0])
#             l.append(j[:4])
#     print(sorted(set(l)))

