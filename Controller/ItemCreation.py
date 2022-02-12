import panda as pd

# class ItemCreation:
#
#     def database_creation(self):
#
#     def create_table
#
#     def create_graph
#
#     def create_map

# def chemin_acces():
#     """Récupère le chemin d'accès du directoire
#     Création d'un dossier data si non existant"""
#     cwd = os.getcwd()
#     cwd_data = cwd + "/data/"
#     return cwd_data
#
# cwd = chemin_acces()
# city = "/Amsterdam/"
# file_cwd = cwd + city + "listing.csv"
# file_cwd_test = "C:\opc finis\Projet perso\data\Amsterdam\listings.csv"
#
# frame_csv = pd.read_csv(file_cwd_test, index_col=0, nrows=20, usecols=selected_header)
# full_frame_csv = pd.read_csv(file_cwd_test, index_col=0, usecols=selected_header)
# frame_csv.info()
# test = full_frame_csv.describe()


class DataCreation:

    def __init__(self, dataframe):
        self.dataframe = dataframe


    def dataframe_menu(self):
        input_number = 0
        while input_number != 5:
            input_number = int(input())
            if input_number == 1:
                self.dataframe.head(10)
            elif input_number == 2:
                self.save_dataframe(self.dataframe)
            elif input_number == 3:
                self.dataframe_info_menu(self.dataframe)
            # elif input_number == 4:


    def save_dataframe(self):
        file_name=input("enter file name : \n")
        self.dataframe.to_csv(file_name)
        print(str(file_name) + ".csv registered")
        self.dataframe_menu()

    def dataframe_info_menu(self):
        input_number = 0
        while input_number != 4:
            input_number = int(input())
            if input_number == 1:
                self.dataframe.columns()
                self.dataframe_info_menu()
            elif input_number == 2:
                self.dataframe.info()
                self.dataframe_info_menu()
            elif input_number == 3:
                self.dataframe.describe()
                self.dataframe_info_menu()
            # elif input_number == 4 :
        return self.dataframe_menu(self.dataframe)

    def panda_dropna(self):
        input_number = 0
        while input_number != 4:
            input_number = int(input())
            if input_number == 1:
                self.dataframe = self.dataframe.dropna(how="all")
                input_number = 4
            elif input_number == 2:
                self.dataframe = self.dataframe.dropna(how="any")
                input_number = 4
        return self.dataframe_menu(self.dataframe)


#     def dataframe_sorting_menu(self):
#         # df.T
# # df.sort_index(axis=1, ascending= False)
# # df.sort_values(by = "column_delected")
# # .groupby("index")
#
#
#     def dataframe_operations(self):
#     # df.sum()
#     # df.mean()
#     # df.mean(1)
#     # df.apply(lambda x : x.max - x.min)
#
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