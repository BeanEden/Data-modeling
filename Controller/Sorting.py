class SortingClass:

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def sort_values_function(self, column_choice, ascending_choice=False, axis_choice=0):
        dataframe_sorted = self.dataframe.sort_values(by=column_choice,
                                                      ascending=ascending_choice,
                                                      axis=axis_choice)
        return dataframe_sorted

    def sort_index_function(self, ascending_choice=True, axis_choice=0):
        dataframe_sorted = self.dataframe.sort_index(ascending=ascending_choice,
                                                     axis=axis_choice)
        return dataframe_sorted

    def sort_group_by_function(self, column_choice, axis_choice=0, drop_na_choice=False):
        dataframe_group_by = self.dataframe[column_choice].groupby(
                                                    by=column_choice[0],
                                                    axis=axis_choice,
                                                    sort=False,
                                                    dropna=drop_na_choice).mean().copy()
        count = self.dataframe[column_choice[0]] = self.dataframe[column_choice[0]].value_counts()
        dataframe_group_by["count"] = count
        return dataframe_group_by

    def dataframe_transposing_function(self):
        dataframe_transposed = self.dataframe.T
        return dataframe_transposed

    def dataframe_column_suppression(self, column):
        self.dataframe.pop(column)
        return self.dataframe
