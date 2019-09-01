import gc

import gspread
import os

import pprint
from oauth2client.service_account import ServiceAccountCredentials

name = ""
filename = "_stats_lvl_"
lvl = 1
extension = ".txt"



scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('STATSTFT-2133776c086c.json', scope)
client = gspread.authorize(creds)

gc = gspread.authorize(creds)
sh = gc.open('STATS TFT')
worksheet = sh.get_worksheet(0)


#sheet = client.open('STATS TFT').sheet1
#tft_stats_scheet = sheet.cell(4, 3).value

#print(tft_stats_scheet)
pp = pprint.PrettyPrinter()

#pp.pprint(tft_stats_scheet)

#cell.row, cell.col

for column in range(3, 58):

    lvl = 1

    name = worksheet.cell(4, column).value
    pp.pprint(str(name))
    StatSheet = open(str(name) + filename + str(lvl) + str(extension), "w")
    StatSheet.write(str(name))

    while lvl < 4:

        for row in range(3 + lvl, 28, 3):
            value = worksheet.get_all_values()
            print(type(value))

            fullStr = '_'.join([str(elem) for elem in value ])
            print(type(fullStr))
            StatSheet.write(fullStr)


            StatSheet.close
            StatSheet = open(str(name) + filename + str(lvl) + str(extension), "r")
            print(StatSheet.read())

        lvl = lvl + 1
