import json

#open json file
with open('precipitation.json', encoding='utf8') as file:
    data = json.load(file)

#select Seattle measurements
seattle = 'GHCND:US1WAKG0038'
monthly_sum_measurement = [0]*12
for measurement in data:
    if measurement ['station'] == seattle:
        measurement_date = measurement['date'].split('-')
        # list sum of measurements per month 
        month = int(measurement_date[1])-1
        monthly_sum_measurement[month] += measurement['value']
print(monthly_sum_measurement)

# save as json file 
with open('python_assignment.json', 'w', encoding='utf8') as file:
    json.dump(monthly_sum_measurement, file)