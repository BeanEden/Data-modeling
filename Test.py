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

index = ["id", "room_type", "price", "minimum_nights", "neighbourhood"]

dataframe = df.fast_dataframe_creation(index)

# print(dataframe)
# dataframe.head(10)
view = View()
menu = DataCreation(dataframe, view)
# menu.column_coice_menu()