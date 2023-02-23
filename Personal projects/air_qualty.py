import pandas
is_on = True
hawthorne_data = pandas.read_csv("personal projects\\air-quality\\ad_viz_tile_data.csv")
uintah_data = pandas.read_csv("personal projects\\air-quality\\ad_viz_tile_data-3.csv")

hawthorne_data_index = []
uintah_data_index = []

for x in uintah_data["Ozone AQI Value"]:
    uintah_data_index.append(x)

for y in hawthorne_data["Ozone AQI Value"]:
    hawthorne_data_index.append(y)

uintah_dict = {"Good": [],
               "Moderate": [],
               "Unhealthy for Sensitive Groups": [],
               "Unhealthy":[],
               "Very Unhealthy":[],
               "Hazardous":[]
               }

hawthorne_dict = {"Good": [],
               "Moderate": [],
               "Unhealthy for Sensitive Groups": [],
               "Unhealthy":[],
               "Very Unhealthy":[],
               "Hazardous":[]
               }

for values in uintah_data_index:
    if values < 54:
        uintah_dict["Good"].append(values)
    elif values >= 54 and values < 71:
        uintah_dict["Moderate"].append(values)
    elif values > 70 and values < 86:
        uintah_dict["Unhealthy for Sensitive Groups"].append(values)
    elif values > 86 and values < 106:
        uintah_dict["Unhealthy"].append(values)
    elif values > 106 and values < 201:
        uintah_dict["Very Unhealthy"].append(values)
    else:
        uintah_dict["Hazardous"].append(values)

for values in hawthorne_data_index:
    if values < 54:
        hawthorne_dict["Good"].append(values)
    elif values >= 54 and values < 71:
        hawthorne_dict["Moderate"].append(values)
    elif values > 70 and values < 86:
        hawthorne_dict["Unhealthy for Sensitive Groups"].append(values)
    elif values > 86 and values < 106:
        hawthorne_dict["Unhealthy"].append(values)
    elif values > 106 and values < 201:
        hawthorne_dict["Very Unhealthy"].append(values)
    else:
        hawthorne_dict["Hazardous"].append(values)





def give_values():
    health_level = input("What level do you want to see? ")
    station = input("What station do you want to see? ")
    if station == "Hawthorne":
        print(f'The percent air quality for {health_level} at Hawthorne is {round(len(hawthorne_dict[health_level]) / len(hawthorne_data_index) * 100)}%')
        print(hawthorne_data.describe())
    elif station == "Uintah":
        print(f'The percent air quality for {health_level} at Uintah is {round(len(uintah_dict[health_level]) / len(uintah_data_index) * 100)}%')
        print(uintah_data.describe())


while is_on:
     give_values()
     cont = input("Would you like to continue? ")
     if cont == "Yes":
         is_on = True
     else:
         is_on = False


def year_to_year():
    pass
    yearly_aqi = []
    year = input("What year would you like to see?(2013/2023) ")
    iter_year = year[2] + year[3]
    print(iter_year)
    try:
        for row in hawthorne_data.iterrows():
                index_date = row[1]["Date"][8]+row[1]["Date"][9]
                if index_date == iter_year:
                    yearly_aqi.append(row[1]["Ozone AQI Value"])
    except:
        pass

    print(yearly_aqi)



year_to_year()

df = pandas.DataFrame(hawthorne_data)
for ind in df.index:
    print(df["Date"][ind], df["Ozone AQI Value "][ind])