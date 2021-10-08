import pandas

data = pandas.read_csv('227 2018-Central-Park-Squirrel-Census-Squirrel-Data.csv')
gray_sq = len(data[data['Primary Fur Color']=='Gray'])
red_sq = len(data[data['Primary Fur Color']=='Cinnamon'])
black_sq = len(data[data['Primary Fur Color']=='Black'])
print(gray_sq)
print(red_sq)
print(black_sq)
data_dict = {"Fur Colour" : ["Gray","Cinnamon","Black"],"Count": [gray_sq, red_sq, black_sq]}
df = pandas.DataFrame(data_dict)
df.to_csv('squirells_data.csv')

