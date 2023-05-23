import pandas

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

column_name = 'Primary Fur Color'

filtered_df = squirrel_data.dropna(subset=column_name)

fur_colors = filtered_df[column_name].unique()
fur_count = []

for color in fur_colors:
    fur_count.append(len(squirrel_data[squirrel_data[column_name] == color]))

output_list = {
    "Fur": fur_colors,
    "Count": fur_count
}

output = pandas.DataFrame(output_list)
output_file_name = "output.csv"

output.to_csv(output_file_name, index=True)
