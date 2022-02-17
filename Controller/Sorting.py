class SortingClass:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def sort_values_function(self, column_choice, ascending_choice=False, axis_choice=0):
        dataframe_sorted = self.dataframe.sort_values(by=column_choice,
                                                      ascending=ascending_choice,
                                                      axis=axis_choice)
        return dataframe_sorted

    def sort_index_function(self, dataframe_selected, ascending_choice=True, axis_choice=0):
        dataframe_sorted = dataframe_selected.sort_index(ascending=ascending_choice,
                                                         axis=axis_choice)
        return dataframe_sorted

    def sort_group_by_function(self, dataframe_selected, column_choice, axis_choice=0, drop_na_choice=False):
        dataframe_group_by = dataframe_selected[column_choice].groupby(
                                                    by=column_choice[0],
                                                    axis=axis_choice,
                                                    sort=False,
                                                    dropna=drop_na_choice).mean().copy()
        count = dataframe_selected[column_choice[0]] = dataframe_selected[column_choice[0]].value_counts()
        dataframe_group_by["count"] = count
        return dataframe_group_by

    def dataframe_transposing_function(self, dataframe_selected):
        dataframe_transposed = dataframe_selected.T
        return dataframe_transposed

    def dataframe_column_suppression(self, dataframe_selected, column_choice):
        dataframe_selected.pop(column_choice[0])
        return dataframe_selected
