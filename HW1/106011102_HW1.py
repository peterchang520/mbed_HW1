# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106011102.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================


# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))


# Remove the data whose value of WDSD is -99.000 or -999.000
data_update = []
for data_idx in data:
    if (data_idx['WDSD']!='-99.000' and data_idx['WDSD']!='-999.000'):
        data_update.append(data_idx)

# Generate the station_id dictionary (include WDSD dictionaries)
station_id = {}
for data_idx in data:
    if data_idx['station_id'] not in station_id:
        id = data_idx['station_id']
        WDSD = {}
        WDSD['max'] = 'None'
        WDSD['min'] = 'None'
        WDSD['range'] = 'None'
        station_id[id] = WDSD

# Find out the maximum value and the minimum value of WDSD of each station
for id in station_id:
    for data_idx in data_update:
        if data_idx['station_id']==id:
            if station_id[id]['max']=='None' and station_id[id]['min']=='None':
                station_id[id]['max'] = float(data_idx['WDSD'])

            elif station_id[id]['min']=='None' and float(data_idx['WDSD'])>station_id[id]['max']:
                station_id[id]['min'] = station_id[id]['max']
                station_id[id]['max'] = float(data_idx['WDSD'])

            elif station_id[id]['min']=='None' and float(data_idx['WDSD'])<=station_id[id]['max']:
                station_id[id]['min'] = float(data_idx['WDSD'])
            
            else:
                if float(data_idx['WDSD'])>station_id[id]['max']:
                    station_id[id]['max'] = float(data_idx['WDSD'])
                elif float(data_idx['WDSD'])<station_id[id]['min']:
                    station_id[id]['min'] = float(data_idx['WDSD'])

    if station_id[id]['max']!='None' and station_id[id]['min']!='None':
        station_id[id]['range'] =  (station_id[id]['max']) - (station_id[id]['min'])
         

# output data
data_out = []
target_station = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
for station in target_station:
    list = []
    list.append(station)
    list.append(station_id[station]['range'])
    data_out.append(list)

print(data_out)

# debug
# for id in station_id:
#     if(station_id[id]['range']<0):
#         print('There are some bugs...')

# print station_id['C0AC40']['max']
# print station_id['C0AC40']['min']


# print station_id['CM0170']['range']
# print data_out[-1]

# for id in station_id:
#     print station_id[id]['range']


# Retrive ten data points from the beginning.
# target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
# print(target_data)
#========================================
