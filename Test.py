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
dataframe_sorted = menu.sorting.sort_group_by_function(["room_type"])
display(dataframe_sorted)
df_trout = dataframe["price"].value_counts().sort_index()
display(df_trout)

trout_max = df_trout.max()
step = menu.graph.percent_step_definition(10, trout_max, 0)
trout1 = df_trout.groupby(pd.cut(df_trout.index, np.arange(0, trout_max + step, step))).sum()
display(trout1)

plot = dataframe_sorted.plot.bar()
plt.show()

print(type(dataframe_sorted))
print((type(trout1)))
# df_room_trout = dataframe.value_counts("room_type").sort_index()
# display(df_room_trout)
# trout = dataframe_sorted["count"].value_counts().sort_index()
# display(trout)
# trout_index = dataframe.sort_index()
# display(trout_index)


# menu.graph.bar_diagram_creator(dataframe_sorted, "room_type")

# choice = menu.column_choice_menu()
# # test = menu.dataframe.groupby(choice).mean()
# df = menu.dataframe
# menu.group_by_menu(df)
# dataframe_group_by = dataframe[["room_type", "price"]].groupby("room_type").sum().copy()
# # print(dataframe_group_by)



