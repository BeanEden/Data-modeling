from View.View import View
from Controller.Menu import DataCreation
from Model.Model import Database

file = "C:\opc finis\Projet perso\data\Amsterdam\listings.csv"

def main():
    view = View()
    df = Database(file)
    # index = df.select_header()
    index = ["latitude", "longitude", "price", "room_type"]
    dataframe = df.fast_dataframe_creation(index)
    menu = DataCreation(dataframe, view)
    menu.dataframe_menu(dataframe)


if __name__ == '__main__':
    main()
else:
    pass

# http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2022-01-06/data/listings.csv.gz
# http://data.insideairbnb.com/the-netherlands/north-holland/amsterdam/2021-12-05/data/listings.csv.gz