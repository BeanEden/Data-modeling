import pandas as pd

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

    def __init__(self, dataframe, view):
        self.dataframe = dataframe
        self.view = view

    def dataframe_menu(self):
        self.view.print_dataframe_menu()
        input_number = 0
        while input_number != 5:
            input_number = int(input())
            if input_number == 1:
                print(self.dataframe.head(10))
                input("press a key to continue")
                self.dataframe_menu()
            elif input_number == 2:
                self.save_dataframe()
                input("press a key to continue")
                self.dataframe_menu()
            elif input_number == 3:
                self.dataframe_info_menu()
            # elif input_number == 4:


    def save_dataframe(self):
        file_name=input("enter file name : \n")
        self.dataframe.to_csv(str(file_name+".csv"))
        print(str(file_name) + ".csv saved")


    def dataframe_info_menu(self):
        self.view.print_dataframe_info_menu()
        input_number = 0
        while input_number != 3:
            input_number = int(input())
            if input_number == 1:
                self.dataframe.info()
                input("press a key to continue")
                self.dataframe_info_menu()
            elif input_number == 2:
                print(self.dataframe.describe())
                input("press a key to continue")
                self.dataframe_info_menu()
            # elif input_number == 4 :
        return self.dataframe_menu()

    def panda_dropna(self):
        input_number = 0
        while input_number != 3:
            input_number = int(input())
            if input_number == 1:
                self.dataframe = self.dataframe.dropna(how="all")
                input_number = 3
            elif input_number == 2:
                self.dataframe = self.dataframe.dropna(how="any")
                input_number = 3
        return self.dataframe_menu()


    def dataframe_sorting_menu(self):
        input_number = 0
        while input_number != 6:
            input_number = int(input())
            if input_number == 1:
                self.panda_dropna()
            # elif input_number == 2:
                # self.sort_value_menu()
            # elif input_number == 3
            #     self.groupby_menu()
            # elif input_number == 4:
            #     self.sort_index_menu()
            # elif input_number == 5:
            #     self.dataframe.T

        # self.dataframe_menu()

    # def sort_value_menu(self):
    #     input_number = 0
    #     while input_number != 6:
    #         input_number = int(input())
    #         if input_number == 1:
    #             self.

    def column_coice_menu(self):
        column_list = tuple(self.dataframe.columns)
        count = 0
        column_index = {}
        for i in column_list:
            count += 1
            column_index[count] = i
            print(column_index[count])
        column_length = len(column_list)
        input_number = 0
        column_choice = []
        while input_number != (int(column_length)+1):
            input_number = int(input())
            choice = column_index[input_number]
            column_choice.append(choice)
            print(str(choice) + " selected\n")







    # df.T
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


### graphs
#     def plot_scatter(ax, prng, nb_samples=100):
#         """Scatter plot."""
#         for mu, sigma, marker in [(-.5, 0.75, 'o'), (0.75, 1., 's')]:
#             x, y = prng.normal(loc=mu, scale=sigma, size=(2, nb_samples))
#             ax.plot(x, y, ls='none', marker=marker)
#         ax.set_xlabel('X-label')
#         ax.set_title('Axes title')
#         return ax
#
#     def plot_bar_graphs(ax, prng, min_value=5, max_value=25, nb_samples=5):
#         """Plot two bar graphs side by side, with letters as x-tick labels."""
#         x = np.arange(nb_samples)
#         ya, yb = prng.randint(min_value, max_value, size=(2, nb_samples))
#         width = 0.25
#         ax.bar(x, ya, width)
#         ax.bar(x + width, yb, width, color='C2')
#         ax.set_xticks(x + width, labels=['a', 'b', 'c', 'd', 'e'])
#         return ax
#
#
# #####
#     fig, ax = plt.subplots()
#
#     p1 = ax.bar(ind, menMeans, width, yerr=menStd, label='Men')
#     p2 = ax.bar(ind, womenMeans, width,
#                 bottom=menMeans, yerr=womenStd, label='Women')
#
#     ax.axhline(0, color='grey', linewidth=0.8)
#     ax.set_ylabel('Scores')
#     ax.set_title('Scores by group and gender')
#     ax.set_xticks(ind, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
#     ax.legend()
#
#     # Label with label_type 'center' instead of the default 'edge'
#     ax.bar_label(p1, label_type='center')
#     ax.bar_label(p2, label_type='center')
#     ax.bar_label(p2)
#
#     plt.show()
# ####
# fig, ax = plt.subplots()
#
# hbars = ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')
#
# # Label with specially formatted floats
# ax.bar_label(hbars, fmt='%.2f')
# ax.set_xlim(right=15)  # adjust xlim to fit labels
#
# plt.show()
# ####
#
# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
# fig1, ax1 = plt.subplots()
# ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()