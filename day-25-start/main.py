# with open("weather_data.csv") as file:
#     data = file.readlines()
#
# clean_data = []
#
# for i in data:
#     i = i.replace("\n", "")
#     clean_data.append(i)
#
# print(clean_data)

# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperature = []
#     for i in data:
#         if i[1] != "temp":
#             temperature.append(int(i[1]))
#     print(temperature)

import pandas as pd

# data = pd.read_csv("weather_data.csv")
#
# # data_dict = data.to_dict()
# # print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# print(round(data["temp"].mean(), 2))
# print(data["temp"].max())

# Get data in column
# print(data.condition)

# Get data in row
# monday = data[data.day == "Monday"]
# temp_monday = monday.temp[0]
# c_to_f = ((9/5) * temp_monday) + 32
# print(c_to_f)
#
# # Create dataframe
# data_dict = {
#     "name": ["Shivam", "Prachi", "Aditi"],
#     "score": [78, 80, 98]
# }
# new_df = pd.DataFrame(data_dict)
# print(new_df)
# new_df.to_csv("new_df.csv")

data_squirrel = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Grey"])
cinnamon = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Cinnamon"])
black = len(data_squirrel[data_squirrel["Primary Fur Color"] == "Black"])

new_data = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray, cinnamon, black]
}

squirrel_fur_color = pd.DataFrame(new_data)
squirrel_fur_color.to_csv("squirrel_count.csv")
