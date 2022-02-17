import pandas as pd
from IPython.display import display

class Database:

    def __init__(self, file):
        self.file = file

    def __repr__(self):
        display()

    def read_data(self, index_col=0):
        pd.read_csv(self.file, index_col=index_col)

    def column_index_creator(self):
        og_csv = pd.read_csv(self.file, nrows=2)
        a = tuple(og_csv.columns)
        count = 0
        column_index = {}
        for i in a:
            count += 1
            column_index[count] = i
        return column_index

    def select_header(self):
        index = self.column_index_creator()
        for i in index.items():
            print(i)
        index_order = []
        input_selected = ""
        while input_selected != "00":
            print("Column already selected : " + str(index_order))
            input_selected = int(input("Select a number, enter 00 to exit : \n"))
            try:
                index_order.append(index[int(input_selected)])
            except KeyError:
                input_selected = "00"
        return index_order

    def fast_dataframe_creation(self, index=None):
        dataframe = pd.read_csv(self.file, low_memory=False, usecols=index, index_col=None)
        return dataframe

    def dataframe_creation_full(self):
        dataframe = pd.read_csv(self.file,
                                sep=None, delimiter=None, header='infer',
                                names=None, index_col=None, usecols=None, squeeze=False,
                                prefix=None, mangle_dupe_cols=True, dtype=None,
                                engine=None, converters=None, true_values=None, false_values=None,
                                skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None,
                                na_values=None, keep_default_na=True, na_filter=True, verbose=False,
                                skip_blank_lines=True, parse_dates=False, infer_datetime_format=False,
                                keep_date_col=False, date_parser=None, dayfirst=False, cache_dates=True,
                                iterator=False, chunksize=None, compression='infer', thousands=None,
                                decimal='.', lineterminator=None, quotechar='"', quoting=0,
                                doublequote=True, escapechar=None, comment=None, encoding=None,
                                encoding_errors='strict', dialect=None, error_bad_lines=None,
                                warn_bad_lines=None, on_bad_lines=None, delim_whitespace=False,
                                low_memory=True, memory_map=False, float_precision=None,
                                storage_options=None)
        return dataframe
