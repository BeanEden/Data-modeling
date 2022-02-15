class View:

    def print_city_select(self):
        print(
            "===================================\n"
            "MAIN MENU\n"
            "===================================\n"
            " 1 - Start a tournament\n"
            " 2 - Add a player\n"
            " 3 - Update a player\n"
            " 4 - Consult a tournament / player / matches report\n"
            " 5 - Exit program\n"
            "===================================\n"
            "Enter a choice and press enter :\n")


    def print_dataframe_menu(self):
        print(
            "===================================\n"
            "DATAFRAME MENU\n"
            "===================================\n"
            " 1 - Visualize dataframe\n"
            " 2 - Save dataframe\n"
            " 3 - Dataframe info menu\n"
            " 4 - Dataframe sorting\n"
            " 5 - Dataframe operations\n"
            " 6 - Graphics\n"
            " 7 - Exit program\n"
            "===================================\n"
            "Enter a choice and press enter :\n")


    def print_dataframe_info_menu(self):
        print(
            "===================================\n"
            "DATAFRAME INFO MENU\n"
            "===================================\n"
            " 1 - Info()\n"
            " 2 - Describe()\n"
            " 3 - Exit program\n"
            "===================================\n"
            "Enter a choice and press enter :\n")


    def print_dataframe_sorting_menu(self):
        print(
            "===================================\n"
            "DATAFRAME SORTING MENU\n"
            "===================================\n"
            " 1 - Drop_Na()\n"
            " 2 - Sort by value\n"
            " 3 - Group by column\n"
            " 4 - Sort by index\n"
            " 5 - Remove a column\n"
            " 6 - Transposing lines and columns\n"
            " 7 - Exit to dataframe menu\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    def print_dropna_menu(self):
        print(
            "===================================\n"
            "DROP_NA MENU\n"
            "===================================\n"
            " 1 - Drop_all\n"
            " 2 - Drop_any\n"
            " 3 - Exit to sorting menu\n"
            "===================================\n"
            "Enter a choice and press enter :\n")

    def print_sort_value_menu(self):
        print(
            "===================================\n"
            "SORTING BY VALUE MENU\n"
            "===================================\n"
            " 1 - Drop_all\n"
            " 2 - Drop_any\n"
            " 3 - Exit to sorting menu\n"
            "===================================\n"
            "Enter a choice and press enter :\n")


    def print_graph_menu(self):
        print(
            "===================================\n"
            "GRAPH MENU\n"
            "===================================\n"
            " 1 - Pie chart\n"
            " 2 - Bar diagram\n"
            " 3 - Scatter diagram\n"
            " 4 - Geographic map\n"
            " 5 - Exit to main menu\n"
            "===================================\n"
            "Enter a choice and press enter :\n")


    def print_column_selection(self, column_dictionnary):
        print(
            "===================================\n"
            "COLUMN SELECT\n"
            "===================================")
            # " 1 - Info()\n"
            # " 2 - Describe()\n"
            # " 3 - Exit program\n"
        for i in column_dictionnary.items():
            print(i)
        print("00 - Exit selection\n"
              "===================================\n"
            "Enter a choice and press enter :\n")
    #
    # def print_type_select(self):
    #
    # def print_table(self):
    #
    # def print_graph(self):
    #
    # def print_graph_select(self:
    #
    # def print_tri_select(self):
    #
    # def print_filter_select(self):
    #
    # def print_save_select(self):

