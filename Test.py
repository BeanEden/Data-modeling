from Controller.Menu import DataCreation
# from Controller.Menu import *
#
from Model.Model import *
#
from View.View import View

import pandas as pd
import concurrent.futures
import os
import matplotlib.pyplot as plt
import numpy as np
# tables_images = list(executor.map(lambda x: telechargement_images(directory, x), ecriture_livre))
file_cwd_test = "C:\opc finis\Projet perso\data\Amsterdam\listings.csv"
df = Database(file_cwd_test)

# index = ["id", "room_type", "price", "minimum_nights", "neighbourhood"]
index_map = ["id", "room_type", "price", "longitude", "latitude"]

dataframe = df.fast_dataframe_creation(index_map)

# print(dataframe)
# dataframe.head(10)
view = View()
menu = DataCreation(dataframe, view)
# menu.view.print_dataframe_menu()
dataframe_sorted = menu.sorting.sort_group_by_function(column_choice="room_type",
                                                               axis_choice=0,
                                                               drop_na_choice=False)
# choice = menu.column_choice_menu()
# # test = menu.dataframe.groupby(choice).mean()
# df = menu.dataframe
# menu.group_by_menu(df)
# dataframe_group_by = dataframe[["room_type", "price"]].groupby("room_type").sum().copy()
# # print(dataframe_group_by)



