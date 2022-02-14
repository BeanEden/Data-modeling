from Controller.ItemCreation import DataCreation
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

# header = pd.read_csv(file_cwd_test, index_col=0, nrows=0)
headers = {
        0: "id",
        1: "name",
        2: "host_id",
        3: "host_name",
        4: "neighbourhood_group",
        5: "neighbourhood",
        6: "latitude",
        7: "longitude",
        8: "room_type",
        9: "price",
        10: "minimum_nights",
        11: "number_of_reviews",
        12: "last_review",
        13: "reviews_per_month",
        14: "calculated_host_listings_count",
        15: "availability_365",
        16: "number_of_reviews_ltm",
        17: "license"
}


column_list_geo = [0, 6, 7, 8, 9]
column_list_quality = [0, 8, 9, 10, 11]

selected_header = []

for i in column_list_quality:
    selected_header.append(headers[i])

# file_cwd_test = "C:\opc finis\Projet perso\data\Amsterdam\listings.csv"
#
#
# test_df = Database(file_cwd_test)
# index = test_df.select_header()
#
# test_try = test_df.fast_dataframe_creation(index)
# test_try = test_try.dropna(how="any")

# shape []
# format{}
# datetimeIndex.year
# .copy


# def

# index_print = (lambda x: print(x), index.items())
# print(index_print)
# pd.read_csv(file_cwd_test, index_col=0, nrows=100)
# with concurrent.futures.ThreadPoolExecutor() as executor:
#     tables_images = list(executor.map(lambda x: telechargement_images(directory, x), ecriture_livre))
file_cwd_test = "C:\opc finis\Projet perso\data\Amsterdam\listings.csv"
df = Database(file_cwd_test)

# index = ["id", "room_type", "price", "minimum_nights", "neighbourhood"]
index_map = ["id", "room_type", "price", "longitude", "latitude"]

dataframe = df.fast_dataframe_creation(index_map)

# print(dataframe)
# dataframe.head(10)
view = View()
menu = DataCreation(dataframe, view)
# choice = menu.column_choice_menu()
# test = menu.dataframe.groupby(choice).mean()
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
menu.pie_chart_creator(sizes, labels)
# size_two = menu.dataframe.groupby("room_type").mean()
# print(size_two)
# df = pd.DataFrame({'mass': [0.330, 4.87 , 5.97],
#                    'radius': [2439.7, 6051.8, 6378.1]},
#                   index=['Mercury', 'Venus', 'Earth'])
#
# labels_two = menu.dataframe["room_type"]
# print(menu.dataframe)

# dataframe_grouped = menu.dataframe.groupby(by="room_type")
# print(dataframe_grouped)


# duration_analysis=pd.DataFrame(dataframe["price"].value_counts()).sort_index()
# duration_analysis.columns=["price"]
# duration_analysis1=duration_analysis.groupby(pd.cut(duration_analysis.index, np.arange(0, 200, 10))).sum()
# graph = duration_analysis1.plot.bar()
# plt.show()
# duration_analysis2=duration_analysis.groupby(pd.cut(duration_analysis.index, np.arange(60, 80, 1))).sum()
# duration_analysis2.plot.bar()
# plt.show()

menu.scatter_map_creator("price", 500)

# dataframe_test = dataframe_grouped["room_type"]


# df = dataframe_test.plot.pie(y='room_type', figsize=(5, 5))

# labels_two.groupby(by = ["room_type"])
# print(labels_two)

#
# label_list = []
# for i in labels_two:
#         label_list.append(i)
# print(label_list)


# labels_two = menu.dataframe["room_type"]
# print(labels_two)
# labels_two = labels_two.groupby(by=["room_type"])


# chart = menu.pie_chart_creator(menu.dataframe.groupby("room_type").mean(), menu.dataframe["room_type"])
# test = pd.DataFrame(menu.dataframe[choice])

