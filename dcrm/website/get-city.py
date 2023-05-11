import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://en.wikipedia.org/wiki/List_of_largest_cities_and_towns_in_Turkey'
table_class = 'wikitable sortable jquery-tablesorter'

def get_list_of_city(save=False, save_name='city', column= 'Province (İl)') -> set:
    """

    Purpose:
        to get list of cities of Turkiye as set form iterable from wikipedia

    Parameters:
        save: if True, will save return as .txt at main page
        save_name: name of the file which will be saved
        column: which column of table (dataframe) will be saved

    ------------------------------------------------------------------------

    Return:
        Column which setted will be saved as .txt file and set iterable, 
            set used to get rid off duplicates

    """

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    city_table=soup.find('table', {'class':"wikitable"})


    headers = [header.text.strip() for header in city_table.find_all('th')]

    rows = []

    # Find all `tr` tags
    data_rows = city_table.find_all('tr')

    for row in data_rows:
        value = row.find_all('td')
        beautified_value = [i.text.strip() for i in value]
        # Remove data arrays that are empty
        if len(beautified_value) == 0:
            continue
        rows.append(beautified_value)

    df = pd.DataFrame(data=rows, columns=headers)

    city_of_turkey = set(df[column].to_list())

    if save:
        with open(f"{save_name}.txt", "w", encoding='utf-8') as output:
            output.write(str(city_of_turkey))

    return city_of_turkey



# get_list_of_city(save=True)