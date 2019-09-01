import gspread
import os
import xlrd
import pprint
from oauth2client.service_account import ServiceAccountCredentials

name = ""
filename = "_stats_lvl_"
lvl = 1
extension = ".txt"


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('STATS_TFT-721b6911624d.json', scope)
client = gspread.authorize(creds)

sheet = client.open('STATS TFT').sheet1
tft_stats_scheet = sheet.cell(4, 3).value

print(tft_stats_scheet)
pp = pprint.PrettyPrinter()

pp.pprint(tft_stats_scheet)

for column in range(2, 58):

    lvl = 1

    name = sheet.cell(3, column)
    print(name)
    StatSheet = open(str(name) + str(filename) + str(lvl) +str(extension), "w")
    StatSheet.write(name)

    while lvl < 4:

        for row in range(3 + lvl, 28, 3):
            value = sh.cell_value(row, column)
            print(value)
            StatSheet.write(value)

            StatSheet.close
            StatSheet = open(name + filename + str(lvl) + extension, "r")
            print(StatSheet.read())

        lvl = lvl + 1
