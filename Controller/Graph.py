import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium
from IPython.display import display

class GraphCreatorClass:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    # ,cmap = plt.get_cmap(("Blues"))
    def scatter_diagram_creator(self, color_argument=None, point_size=1,
                                latitude_column_name="latitude", longitude_column_name="longitude"):
        graph = plt.scatter(longitude_column_name, latitude_column_name, data=self.dataframe, s=point_size,
                         c=color_argument)
        plt.colorbar()
        plt.show()
        a = self.save_graph_selection_yn()
        if a == 1:
            self.save_graph(graph)

    def percent_step_definition(self, percent_arg=10, end=100, start=0):
        detail = end - start
        step_try = detail / percent_arg
        return step_try

    def bar_diagram_creator(self, dataframe_selected, argument):
        graph_data = ""
        if argument == "count":
            graph_data = dataframe_selected
        else:
            trout = dataframe_selected[argument].value_counts().sort_index()
            trout_max = trout.max()
            step = self.percent_step_definition(10, trout_max, 0)
            graph_data = trout.groupby(pd.cut(trout.index, np.arange(0, trout_max + step, step))).sum()
        graph = graph_data.plot.bar()
        plt.show()
        a = self.save_graph_selection_yn()
        if a == 1:
            self.save_graph(graph)

    def pie_chart_creator(self, dataframe_selected, column_y):
        # plot = self.dataframe.plot.pie(y=column_y, figsize=(5, 5))
        plot = dataframe_selected.plot.pie(y=column_y, figsize=(5, 5))
        plt.show()
        a = self.save_graph_selection_yn()
        if a == 1:
            self.save_graph(plot)
        return plot

    def scatter_map_creator(self, column_data_name="", filter_selected=0, latitude_column_name="latitude",
                            longitude_column_name="longitude"):
        latitude_center = self.dataframe[latitude_column_name].mean()
        longitude_center = self.dataframe[longitude_column_name].mean()
        map_test = folium.Map(location=[latitude_center, longitude_center], zoom_strat=12)
        print(type(map_test))
        # listing = self.dataframe[latitude_column_name,
        #                                                                                    longitude_column_name]
        listing = self.dataframe[self.dataframe[column_data_name] > int(filter_selected)][[latitude_column_name,
                                                                                           longitude_column_name,
                                                                                           column_data_name]]
        listing.apply(lambda liste: folium.Marker(location=[liste[latitude_column_name],
                                                            liste[longitude_column_name]]).add_to(map_test), axis=1)
        display(map_test)
        a = self.save_graph_selection_yn()
        if a == 1 :
            self.save_map(map_test)

    def save_map(self, map_test):
        map_name = input("Enter map name :\n")
        full_name = map_name + ".html"
        map_test.save(full_name)

    def save_graph(self, graph):
        map_name = input("Enter figure name :\n")
        format_choice = int(input("Select a format:\n"
                                  " 1 - jpg \n"
                                  " 2 - png \n"
                                  " 3 - html\n"))
        if format_choice == 1:
            full_name = map_name + ".jpg"
        elif format_choice == 2:
            full_name = map_name + ".png"
        else:
            full_name = map_name + ".html"
        graph.figure.savefig(full_name)

    def save_graph_selection(self, item, item_type="figure"):
        user_choice = input("Save the figure ? (Y/N)\n")
        if user_choice.upper() == "Y":
            if item_type == "map":
                self.save_map(item)
            else:
                self.save_graph(item)
        elif user_choice.upper() == "N":
            pass
        else:
            self.save_graph_selection(item, item_type)


    def save_graph_selection_yn(self):
        user_choice = input("Save the figure ? (Y/N)\n")
        choice = ""
        if user_choice.upper() == "Y":
            return 1
        elif user_choice.upper() == "N":
            return 0
        else:
            self.save_graph_selection()