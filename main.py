import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

average = sum(temp_list)/ len(temp_list)
print(average)

average_temp = data["temp"].mean()
print(average_temp)

max_temp = data["temp"].max()
print(max_temp)

# Get Data in columns
print(data["condition"])
print(data.condition)

#get data in Row
my_row = data[data.day == "Monday"]
print(my_row)

print(data[data.temp == data.temp.max()])

#create dataframe from scratch

data_dict = {
    "students":["Shanaya","Shantanu", "Sunil"],
    "scores":[90,99,60]
}
dataframe = pandas.DataFrame(data_dict)
print(dataframe)

dataframe.to_csv("new_file.csv")



