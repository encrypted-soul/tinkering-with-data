import pandas as pd
import contextlib
from metpy.io.metar import ParseError
from metpy.io.metar import parse_metar
import pandas as pd
import datetime

file_path = './METAR_2014_2023.csv'
df = pd.read_csv(file_path)

metars = []
# Assuming 'date' is the column in df that contains the dates
for index, row in df.iterrows():
    metar = row['metar']
    airport_id = row['airport_id']
    date = row['date']
    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    # Extract the year and month
    year = date_obj.year
    month = date_obj.month
    with contextlib.suppress(ParseError):
        # Parse the string of text and assign to values within the named tuple
        parsed_metar = parse_metar(metar, year=year, month=month)
        metars.append(parsed_metar)
df = pd.DataFrame(metars)
df.to_csv('metar.csv', index=False)