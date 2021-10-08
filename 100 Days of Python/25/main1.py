import pandas
data = pandas.read_csv('225 weather-data.csv')
# print(data['condition'])
# data_dict = data.to_dict()
# print(data_dict)
#
# list = data['temp'].to_list()
# days = len(list)
# sum_of_temp = sum(list)
#
# print(f"Average temperature : {sum_of_temp/days}")
#
# print(data['day'].max())

#get data
# print(data['condition'])
# print(data.condition)

#get data in Row
print(data[data.day == 'Monday'])
print(data[data.temp == data.temp.max()])
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
print(monday_temp*9/5 + 32)

#dataframes
new_data = {"students":["anshuman", "jay", "ray"], "scores" : [76, 56, 45]
            }
data1 = pandas.DataFrame(new_data)
data1.to_csv("names.csv")