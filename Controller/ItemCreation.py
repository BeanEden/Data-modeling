import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import folium
from Controller.Sorting import SortingClass
from Controller.Graph import GraphCreatorClass
from IPython.display import display

class DataCreation:

    def __init__(self, dataframe, view):
        self.dataframe = dataframe
        self.view = view
        self.sorting = SortingClass(self.dataframe)
        self.graph = GraphCreatorClass(self.dataframe)

    def dataframe_menu(self, dataframe_sorted):
        self.view.print_dataframe_menu()
        input_number = 0
        while input_number != 5:
            input_number = int(input())
            if input_number == 1:
                print(dataframe_sorted)
                input("press a key to continue")
                self.dataframe_menu(dataframe_sorted)
            elif input_number == 2:
                self.save_dataframe(dataframe_sorted)
                input("press a key to continue")
                self.dataframe_menu(dataframe_sorted)
            elif input_number == 3:
                self.dataframe_info_menu(dataframe_sorted)
            elif input_number == 4:
                self.dataframe_sorting_menu(dataframe_sorted)
            elif input_number == 5:
                self.dataframe_operations_menu(dataframe_sorted)
            elif input_number ==6:
                self.dataframe_graphs_menu(dataframe_sorted)



    def save_dataframe(self, dataframe_sorted):
        file_name=input("enter file name : \n")
        dataframe_sorted.to_csv(str(file_name+".csv"))
        print(str(file_name) + ".csv saved")


    def dataframe_info_menu(self,dataframe_sorted):
        self.view.print_dataframe_info_menu()
        input_number = 0
        while input_number != 3:
            input_number = int(input())
            if input_number == 1:
                self.dataframe.info()
                input("press a key to continue:\n")
                self.dataframe_info_menu(dataframe_sorted)
            elif input_number == 2:
                print(self.dataframe.describe())
                input("press a key to continue:\n")
                self.dataframe_info_menu(dataframe_sorted)
        return self.dataframe_menu(dataframe_sorted)

    def dataframe_sorting_menu(self, dataframe_selected):
        self.view.print_dataframe_sorting_menu()
        input_number = 0
        while input_number != 7:
            input_number = int(input())
            if input_number == 1:
                self.panda_dropna_menu(dataframe_selected)
            elif input_number == 2:
                self.sort_value_menu(dataframe_selected)
            elif input_number == 3:
                self.sort_group_by_menu(dataframe_selected)
            elif input_number == 4:
                self.sort_index_menu(dataframe_selected)
            elif input_number == 5:
                self.sort_column_suppression_menu(dataframe_selected)
            elif input_number == 6:
                self.dataframe.T(dataframe_selected)
        self.dataframe_menu(dataframe_selected)

    def panda_dropna_menu(self, dataframe_selected):
        self.view.print_dropna_menu()
        input_number = 0
        while input_number != 3:
            input_number = int(input())
            if input_number == 1:
                self.dataframe = self.dataframe.dropna(how="all")
                input_number = 3
            elif input_number == 2:
                self.dataframe = self.dataframe.dropna(how="any")
                input_number = 3
        return self.dataframe_menu(dataframe_selected)

    def sort_value_menu(self, dataframe_selected):
        self.sorting.dataframe = dataframe_selected
        column_choice = self.column_selection_menu()
        ascending_choice = self.boolean_choice_menu()
        axis_choice = self.axis_choice_menu()
        dataframe_sorted = self.sorting.sort_values_function(column_choice=column_choice,
                                                             ascending_choice=ascending_choice,
                                                             axis_choice=axis_choice)
        print(dataframe_sorted)
        self.save_item_selection(dataframe_sorted)
        next_dataframe = self.continue_with_dataframe(dataframe_sorted)
        self.dataframe_sorting_menu(next_dataframe)

    def sort_group_by_menu(self, dataframe_selected):
        self.sorting.dataframe = dataframe_selected
        column_choice = self.column_selection_menu()
        drop_na_choice = self.boolean_choice_menu()
        axis_choice = self.axis_choice_menu()
        dataframe_sorted = self.sorting.sort_group_by_function(column_choice=column_choice,
                                                               axis_choice=axis_choice,
                                                               dropna_choice=drop_na_choice)
        print(dataframe_sorted)
        self.save_item_selection(dataframe_sorted)
        next_dataframe = self.continue_with_dataframe(dataframe_sorted)
        self.dataframe_sorting_menu(next_dataframe)

    def sort_index_menu(self, dataframe_selected):
        self.sorting.dataframe = dataframe_selected
        ascending_choice = self.boolean_choice_menu()
        axis_choice = self.axis_choice_menu()
        dataframe_sorted = self.sorting.sort_index_function(ascending_choice=ascending_choice,
                                                            axis_choice=axis_choice)
        print(dataframe_sorted)
        self.save_item_selection(dataframe_sorted)
        next_dataframe = self.continue_with_dataframe(dataframe_sorted)
        self.dataframe_sorting_menu(next_dataframe)

    def sort_column_suppression_menu(self, dataframe_selected):
        self.sorting.dataframe = dataframe_selected
        column_choice = self.column_selection_menu()
        dataframe_sorted = self.sorting.dataframe_column_suppression(column_choice)
        print(dataframe_sorted)
        self.save_item_selection(dataframe_sorted)
        next_dataframe = self.continue_with_dataframe(dataframe_sorted)
        self.dataframe_sorting_menu(next_dataframe)

    def sort_transposing_menu(self, dataframe_selected):
        self.sorting.dataframe = dataframe_selected
        dataframe_sorted = self.sorting.dataframe_transposing_function()
        print(dataframe_sorted)
        self.save_item_selection(dataframe_sorted)
        next_dataframe = self.continue_with_dataframe(dataframe_sorted)
        self.dataframe_sorting_menu(next_dataframe)

    def dataframe_graphs_menu(self, dataframe_selected):
        self.view.print_dataframe_sorting_menu()
        input_number = 0
        while input_number != 5:
            input_number = int(input())
            if input_number == 1:
                self.pie_chart_menu(dataframe_selected)
            elif input_number == 2:
                self.bar_diagram_menu(dataframe_selected)
            elif input_number == 3:
                self.scatter_diagram_menu(dataframe_selected)
            elif input_number == 4:
                self.geographic_map_menu(dataframe_selected)
        self.dataframe_menu(dataframe_selected)


    def pie_chart_menu(self, dataframe_selected):
        self.sorting.dataframe = dataframe_selected
        column_choice = self.column_selection_menu()
        graph = self.graph.pie_chart_creator(column_choice[0])
        self.graph.save_item_selection(graph)
        self.dataframe_graphs_menu(dataframe_selected)

    def bar_diagram_menu(self, dataframe_selected):
        self.sorting.dataframe = dataframe_selected
        column_choice = self.column_selection_menu()
        graph = self.graph.bar_diagram_creator(column_choice[0])
        self.graph.save_item_selection(graph)
        self.dataframe_graphs_menu(dataframe_selected)

    def scatter_diagram_menu(self, dataframe_selected):
        self.sorting.dataframe = dataframe_selected
        column_choice = self.column_selection_menu()
        graph = self.graph.scatter_diagram_creator(color_argument=column_choice[0])
        self.graph.save_item_selection(graph)
        self.dataframe_graphs_menu(dataframe_selected)

    def geographic_map_menu(self, dataframe_selected):
        self.sorting.dataframe = dataframe_selected
        column_choice = self.column_selection_menu()
        graph = self.graph.scatter_map_creator(column_data_name=column_choice[0])
        self.graph.save_item_selection(graph,"map")
        self.dataframe_graphs_menu(dataframe_selected)


    def column_selection_menu(self):
        column_list = tuple(self.dataframe.columns)
        count = 0
        column_index = {}
        for i in column_list:
            count += 1
            column_index[count] = i
        self.view.print_column_selection(column_index)
        column_length = len(column_list)
        input_number = 0
        column_choice = []
        exit_choice = int(column_length)+1
        while input_number != "00":
            input_number = input()
            try:
                choice = column_index[int(input_number)]
                column_choice.append(choice)
                print(str(column_choice) + " selected\n")
            except KeyError:
                input_number = "00"
        print(column_choice)
        return column_choice

    def boolean_choice_menu(self):
        user_choice = input("0 = False\n"
                       "1 = True \n")
        if int(user_choice) == 0:
            return False
        elif int(user_choice) == 1:
            return True
        else:
            self.boolean_choice_menu()

    def axis_choice_menu(self):
        user_choice = input("0 = axis on columns\n"
                       "1 = axis on lines \n")
        if int(user_choice) == 0:
            return 0
        elif int(user_choice) == 1:
            return 1
        else:
            self.axis_choice_menu()

    def save_item_selection(self, dataframe_sorted):
        user_choice = input("Save dataframe as csv ? (Y/N)\n")
        if user_choice.upper() == "Y":
            self.save_dataframe(dataframe_sorted)
        elif user_choice.upper() == "N":
            pass
        else:
            self.save_item_selection(dataframe_sorted)

    def continue_with_dataframe(self, dataframe_sorted):
        user_choice = input("Continue with this dataframe ? (Y/N)\n")
        if user_choice.upper() == "Y":
            return dataframe_sorted
        elif user_choice.upper() == "N":
            return self.dataframe
        else:
            self.continue_with_dataframe(dataframe_sorted)
#
#     def dataframe_operations(self):
#     # df.sum()
#     # df.mean()
#     # df.mean(1)
#     # df.apply(lambda x : x.max - x.min)
#       df.value_counts()
#     def column_operations(self):
#     # dataset[dataset[column]]
#     # column operation(column_one, column_two, operation)


    def check_(self, dataframe, column, input_number):
        if input_number == 1:
            dataframe.groupby(column)
        elif input_number == 2:
            dataframe.info()
        elif input_number == 3:
            dataframe.describe()
        # elif input_number == 4:






