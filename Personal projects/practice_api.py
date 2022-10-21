import requests
import json
import pyodbc
from datetime import date

Today = date.today()

state = [[1, 'LASST010000000000003'], [2, 'LASST020000000000004'], [3, 'LASST050000000000003'], [4, 'LASST090000000000003'], [5, 'LASST120000000000003'], [6, 'LASST130000000000003'], [7, 'LASST150000000000003'], [8, 'LASST160000000000003'], [9, 'LASST180000000000003'], [10, 'LASST190000000000003'], [11, 'LASST200000000000003'], [12, 'LASST210000000000003'], [13, 'LASST220000000000003'], [14, 'LASST270000000000003'], [15, 'LASST280000000000003'], [16, 'LASST300000000000003'], [17, 'LASST310000000000003'], [18, 'LAUST320000000000003'], [19, 'LAUST330000000000003'], [20, 'LASST370000000000003'], [21, 'LASST380000000000003'], [22, 'LASST390000000000003'], [23, 'LASST400000000000003'], [24, 'LAUST410000000000003'], [25, 'LASST420000000000003'], [26, 'LASST450000000000003'], [27, 'LASST460000000000003'], [28, 'LASST470000000000003'], [29, 'LASST480000000000003'], [30, 'LASST490000000000003'], [31, 'LASST540000000000003'], [32, 'LASST550000000000003'], [33, 'LASST560000000000003'], [34, 'LASST040000000000003'], [35, 'LASST080000000000003'], [36, 'LASST230000000000003'], [37, 'LASST250000000000003'], [38, 'LASST260000000000003'], [39, 'LASST240000000000003'], [40, 'LASST290000000000003'], [41, 'LASST360000000000003'], [42, 'LASST440000000000003'], [43, 'LASST500000000000003'], [44, 'LASST530000000000003'], [45, 'LASST060000000000003'], [46, 'LASST170000000000003'], [47, 'LASST100000000000003'], [48, 'LASST350000000000003'], [49, 'LASST510000000000003'], [50, 'LASST340000000000003']]

cnxn = pyodbc.connect(Trusted_Connection='yes', driver = '{SQL Server}',server = 'localhost\SQLEXPRESS' , database = 'Econ')

cursor = cnxn.cursor()

#headers = {'Content-Type': 'application/json'}
#data = json.dumps({"seriesid": ['LASST060000000000003'], "startyear":"2022", "endyear":"2022"})

#p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data = data, headers = headers)
#json_data = json.loads(p.text)

months = []
rates = []

#for series in json_data['Results']['series']:
#    for item in series['data']:
#        month = item['period']
#        rate = float(item['value'])
#        months.append(month)
#        rates.append(rate)

for i in range(25, 49):
    stateID = state[i][1]
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"seriesid": [f'{stateID}'], "startyear":"2022", "endyear":"2022"})

    p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data = data, headers = headers)
    json_data = json.loads(p.text)
    print(json_data)
    for series in json_data['Results']['series']:
        for item in series['data']:
            rate = float(item['value'])
            month = item['period']
            rates.append(rate)
            months.append(month)
        cursor.execute(f"INSERT INTO Unemployment_Rate(StateID, Unemployment_Rate, Date) Values({i + 1}, {rates[1]}, '2022/06/16')")
        cursor.execute(f"INSERT INTO Unemployment_Rate(StateID, Unemployment_Rate, Date) Values({i + 1}, {rates[2]}, '2022/05/16')")
        cursor.execute(f"INSERT INTO Unemployment_Rate(StateID, Unemployment_Rate, Date) Values({i + 1}, {rates[3]}, '2022/04/16')")
        cursor.execute(f"INSERT INTO Unemployment_Rate(StateID, Unemployment_Rate, Date) Values({i + 1}, {rates[4]}, '2022/03/16')")
        cursor.execute(f"INSERT INTO Unemployment_Rate(StateID, Unemployment_Rate, Date) Values({i + 1}, {rates[5]}, '2022/02/16')")
        cursor.execute(f"INSERT INTO Unemployment_Rate(StateID, Unemployment_Rate, Date) Values({i + 1}, {rates[6]}, '2022/01/16')")
        rates = []





print(months)
print(rates)
cnxn.commit()
